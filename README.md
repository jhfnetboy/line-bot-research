# LINE Bot Research Daily

Daily research digest on LINE bot development and the LINE platform, published as a static card site on Cloudflare Pages. Modeled on the Agent Research Bot setup (`site/build.py` is adapted from it, with English UI and a LINE green theme).

- Live site: https://line-bot-research.pages.dev/
- Repo: https://github.com/jhfnetboy/line-bot-research
- Time zone: Asia/Bangkok (UTC+7); updated each morning

## Layout

- `sources.md` / `sources.json`: source list, generated from `scripts/sources_data.py` (edit only that file)
- `preferences.md`: scope, style and what to skip
- `digests/YYYY-MM-DD.md`: the day's digest in full
- `digests/YYYY-MM-DD.json`: structured data the site is built from
- `weekly/`: optional weekly JSON (same format as Agent Research Bot); empty for now
- `site/build.py`: reads `digests/*.json` and `weekly/*.json`, writes static pages to `site/dist/` (Python 3, no dependencies)
- `site/assets/`: card images downloaded from real sources; the JSON records where each came from
- `site/wrangler.toml`: Pages project config (project `line-bot-research`)
- `scripts/fetch_feeds.py`: collects candidates from the last N hours into `work/` (not committed). Reads RSS/Atom feeds, scrapes LINE Developers news (EN/JA), LINE for Business TH news, LINE Thailand Newsroom and LY Corp newsroom, reads @line/liff on npm, and queries HN
- `scripts/make_sources.py [--check]`: regenerates `sources.*`; `--check` re-requests every URL and records HTTP status
- `scripts/fetch_image.py DATE`: saves the og:image of `image.source_url` to `site/assets/`
- `scripts/scan_secrets.sh`: scans for token or key patterns before every commit
- `scripts/daily.sh [DATE]`: validate, build, scan, commit, push, deploy

## JSON format

```json
{
  "date": "2026-11-23",
  "coverage": "2026-11-16 to 2026-11-23 (Asia/Bangkok, UTC+7)",
  "keywords": ["keyword one", "keyword two"],
  "summary": "Two or three sentences shown on the card.",
  "image": {"local_path": "assets/2026-11-23.jpg", "source_url": "https://original", "credit": "Publisher"},
  "items": [
    {"topic": "Topic", "title": "Title", "summary": "One or two sentences", "url": "https://original", "date": "2026-11-23",
     "keywords": ["..."], "links": [{"label": "Extra source", "url": "https://...", "date": "2026-11-22"}]}
  ]
}
```

## Daily procedure

```bash
cd /workspace/line-bot-research
git pull -q
python3 scripts/fetch_feeds.py --hours 48     # Monday: --hours 72. Output: work/candidates-DATE.tsv
# Read each candidate's original page (LINE Developers notices have full text at https://developers.line.biz/en/news/2026/).
# Google News links are redirects: search for the original article and cite that URL and its published date.
# Write digests/DATE.md and digests/DATE.json (English, no em dashes, every item with url + date).
bash scripts/daily.sh DATE                    # validates, builds, scans, commits, pushes, deploys
curl -s https://line-bot-research.pages.dev/days/DATE/ | grep -c '<article'   # confirm live
```

Deploying needs `CLOUDFLARE_API_TOKEN` (Cloudflare Pages edit; optional `CLOUDFLARE_ACCOUNT_ID`). The repo is public: never write credentials to files. `.gitignore` excludes `.env` and similar, and `daily.sh` runs `scan_secrets.sh` before every commit.

Local preview: `python3 site/build.py && python3 -m http.server 8765 --directory site/dist`

## Known source quirks

- LINE Developers RSS endpoints and LY Corp newsroom RSS return 403 to scripts, so `fetch_feeds.py` scrapes the HTML news lists instead.
- LINE Thailand Newsroom and LY Corp newsroom URLs carry no date. `fetch_feeds.py` lists links not seen before (state in `work/seen.json`); open each to get its date.
- Reddit RSS returns 429 from this machine, so Reddit is not in the list.
- Google News queries are noisy (any article mentioning "LINE OA" as a contact channel). Treat them as leads only.
