#!/usr/bin/env python3
"""Generate sources.json and sources.md from sources_data.py.
--check: request every URL now and record the HTTP status in sources_check.txt (date stamped).
Usage: python3 scripts/make_sources.py [--check]"""
import json, sys, urllib.request, concurrent.futures as cf
from datetime import datetime, timezone, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sources_data import S
root = Path(__file__).resolve().parent.parent
keys = ["name", "url", "type", "area", "purpose", "priority", "fetch"]
rows = [dict(zip(keys, r)) for r in S]
vf = root / "scripts" / "sources_check.txt"
UA = {"User-Agent": "Mozilla/5.0 (line-bot-research)"}
def status(u):
    if "x.com/" in u: return "X-API-verified"
    try: return str(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25).status)
    except urllib.error.HTTPError as e: return str(e.code)
    except Exception: return "ERR"
if "--check" in sys.argv:
    today = datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d")
    with cf.ThreadPoolExecutor(8) as ex: codes = list(ex.map(status, [r["url"] for r in rows]))
    vf.write_text(f"# checked {today}\n" + "".join(f"{c} {r['url']}\n" for c, r in zip(codes, rows)))
checked, verify = "not checked", {}
if vf.exists():
    for l in vf.read_text().splitlines():
        if l.startswith("# checked "): checked = l[10:]; continue
        c, u = l.split(" ", 1); verify[u] = c
for r in rows: r["http_status"] = verify.get(r["url"], "not checked")
(root / "sources.json").write_text(json.dumps({"checked": checked, "count": len(rows), "sources": rows}, ensure_ascii=False, indent=2) + "\n")
order = list(dict.fromkeys(r["area"] for r in rows))
md = ["# LINE Bot Research: sources", "", f"{len(rows)} sources. Reachability checked {checked} (Asia/Bangkok, UTC+7) with a plain HTTP GET; the status is the last column (X accounts are checked through X tools).", "",
      "Priority: P0 read every day; P1 read every day, include when relevant; P2 scan weekly or when needed.", ""]
for a in order:
    md += [f"## {a}", "", "| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |", "| --- | --- | --- | --- | --- | --- | --- |"]
    md += [f"| {r['name']} | {r['url']} | {r['type']} | {r['purpose']} | {r['priority']} | {r['fetch']} | {r['http_status']} |" for r in rows if r["area"] == a]
    md.append("")
(root / "sources.md").write_text("\n".join(md))
print(len(rows), "sources")
