#!/usr/bin/env python3
"""Collect candidates for the daily digest. Reads RSS / Atom feeds in sources.json, scrapes the
LINE pages that have no feed (LINE Developers news, LY Corp newsroom, LINE Thailand newsroom,
LINE for Business TH), reads @line/liff on npm and queries HN Algolia. Writes items from the last
N hours to work/candidates-DATE.tsv (not committed). It only gathers candidates: read each
original page before writing the digest, and keep its URL and date.
Usage: python3 scripts/fetch_feeds.py [--hours 48]"""
import argparse, json, re, urllib.parse, urllib.request, concurrent.futures as cf
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
root = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument("--hours", type=int, default=48); a = ap.parse_args()
BKK = timezone(timedelta(hours=7))
cut = datetime.now(timezone.utc) - timedelta(hours=a.hours)
UA = {"User-Agent": "Mozilla/5.0 (line-bot-research)"}
src = json.loads((root / "sources.json").read_text(encoding="utf-8"))["sources"]
feeds = [s for s in src if s["fetch"].split()[0] in ("RSS", "Atom")]
seen_file = root / "work" / "seen.json"
seen = set(json.loads(seen_file.read_text())) if seen_file.exists() else set()
def get(u, t=25): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()
def fmt(d): return d.astimezone(BKK).strftime("%Y-%m-%d %H:%M")
def pd(s):
    s = (s or "").strip()
    for f in (parsedate_to_datetime, lambda x: datetime.fromisoformat(x.replace("Z", "+00:00"))):
        try:
            d = f(s); return d if d.tzinfo else d.replace(tzinfo=BKK)
        except Exception: pass
def run_feed(s):
    out = []
    try: rootel = ET.fromstring(get(s["url"]))
    except Exception as e: return [(s["name"], "ERR", str(e)[:80], s["url"])]
    for el in rootel.iter():
        if el.tag.split("}")[-1] not in ("item", "entry"): continue
        d = {c.tag.split("}")[-1]: c for c in el}
        title = (d["title"].text if "title" in d and d["title"].text else "").strip()
        link = ((d["link"].text or d["link"].get("href", "")) if "link" in d else "") or el.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")
        ds = next((pd(d[k].text) for k in ("pubDate", "published", "updated", "date") if k in d and d[k].text), None)
        if ds and ds >= cut: out.append((s["name"], fmt(ds), title, link.strip()))
    return out
def day(y, m, dd): return datetime(int(y), int(m), int(dd), tzinfo=BKK)
def scrape_devnews(lang):
    name = f"LINE Developers News ({lang.upper()})"
    try: h = get(f"https://developers.line.biz/{lang}/news/1/").decode("utf-8", "ignore")
    except Exception as e: return [(name, "ERR", str(e)[:80], "")]
    out = []
    for y, m, dd, slug in sorted(set(re.findall(rf'href="/{lang}/news/(\d{{4}})/(\d{{2}})/(\d{{2}})/([^"/]+)/"', h))):
        d = day(y, m, dd)
        if d >= cut - timedelta(days=1): out.append((name, fmt(d), slug.replace("-", " "), f"https://developers.line.biz/{lang}/news/{y}/{m}/{dd}/{slug}/"))
    return out
def scrape_lfb_th():
    name = "LINE for Business Thailand news"
    try: h = get("https://lineforbusiness.com/th/news").decode("utf-8", "ignore")
    except Exception as e: return [(name, "ERR", str(e)[:80], "")]
    out = []
    for slug in sorted(set(re.findall(r'/th/news/(\d{8}[^"\'<> ]*)', h))):
        d = day(slug[:4], slug[4:6], slug[6:8])
        if d >= cut - timedelta(days=1): out.append((name, fmt(d), slug, f"https://lineforbusiness.com/th/news/{slug}"))
    return out
def scrape_new_links(name, page, pattern, prefix):
    """Pages without dates in the URL: report links not seen in earlier runs (open them for the date)."""
    try: h = get(page).decode("utf-8", "ignore")
    except Exception as e: return [(name, "ERR", str(e)[:80], page)]
    links = [prefix + x for x in dict.fromkeys(re.findall(pattern, h))]
    new = [u for u in links if u not in seen]
    seen.update(links)
    return [(name, "NEW (check date)", "", u) for u in new[:15]]
def liff_npm():
    try:
        j = json.loads(get("https://registry.npmjs.org/@line/liff"))
        v = j["dist-tags"]["latest"]; d = pd(j["time"][v])
        return [("@line/liff on npm", fmt(d), f"@line/liff {v}", f"https://www.npmjs.com/package/@line/liff/v/{v}")] if d >= cut else []
    except Exception as e: return [("@line/liff on npm", "ERR", str(e)[:80], "")]
jobs = [lambda s=s: run_feed(s) for s in feeds] + [lambda: scrape_devnews("en"), lambda: scrape_devnews("ja"), scrape_lfb_th, liff_npm]
rows = []
with cf.ThreadPoolExecutor(12) as ex:
    for r in ex.map(lambda f: f(), jobs): rows += r
first_run = not seen
rows += scrape_new_links("LINE Thailand Newsroom", "https://linenewsroom.com/press-release", r'href="(/press-release/[a-z0-9-]+)"', "https://linenewsroom.com")
rows += scrape_new_links("LY Corporation newsroom (EN)", "https://www.lycorp.co.jp/en/news/", r'href="(?:https://www\.lycorp\.co\.jp)?(/en/news/(?:announcements|press|ir)/\d+/)"', "https://www.lycorp.co.jp")
if first_run: rows = [r for r in rows if not r[1].startswith("NEW")] + [("note", "first run", "seen.json was empty; newsroom links listed are the current front page, not necessarily new", "")]
for q in ['"LINE bot"', '"LINE Messaging API"', "LIFF LINE", '"LY Corporation"', '"LINE Official Account"']:
    u = "https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode({"query": q, "tags": "story", "numericFilters": f"created_at_i>{int(cut.timestamp())}", "hitsPerPage": 20})
    try:
        for h in json.loads(get(u, 20))["hits"]:
            if not re.search(r"\bLINE\b|LIFF|LY Corp", h["title"] or ""): continue  # Algolia matches loosely; keep titles that name LINE
            t = datetime.fromtimestamp(h["created_at_i"], timezone.utc)
            rows.append(("HN", fmt(t), f'{h["title"]} [{h["points"]} pts / {h["num_comments"]} comments] {h.get("url") or ""}', f'https://news.ycombinator.com/item?id={h["objectID"]}'))
    except Exception as e: rows.append(("HN", "ERR", str(e)[:80], ""))
rows = list(dict.fromkeys(rows))
(root / "work").mkdir(exist_ok=True)
seen_file.write_text(json.dumps(sorted(seen)))
date = datetime.now(BKK).strftime("%Y-%m-%d")
out = root / "work" / f"candidates-{date}.tsv"
out.write_text("\n".join("\t".join(r) for r in sorted(rows, key=lambda r: r[1], reverse=True)) + "\n", encoding="utf-8")
print(f"{len(rows)} candidates -> {out}")
