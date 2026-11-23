#!/usr/bin/env bash
# Daily pipeline: validate digest -> regenerate sources -> image -> build site -> secret scan -> git commit/push -> wrangler deploy to Cloudflare Pages.
# Prerequisite: digests/DATE.md and digests/DATE.json are written (run scripts/fetch_feeds.py first, read the originals, then write).
# Usage: bash scripts/daily.sh [YYYY-MM-DD]   (default: today in Asia/Bangkok)
# Needs: CLOUDFLARE_API_TOKEN (Pages edit); optional CLOUDFLARE_ACCOUNT_ID; gh logged in for push.
# Options: SKIP_DEPLOY=1 build and commit only; SKIP_PUSH=1 do not push; CHECK_SOURCES=1 re-check every source URL.
set -euo pipefail
cd "$(dirname "$0")/.."
DATE="${1:-$(TZ=Asia/Bangkok date +%F)}"
PROJECT="${CF_PAGES_PROJECT:-line-bot-research}"
[ -f "digests/$DATE.json" ] || { echo "Missing digests/$DATE.json; write the digest first"; exit 1; }
[ -f "digests/$DATE.md" ] || { echo "Missing digests/$DATE.md"; exit 1; }
python3 - "$DATE" <<'PY'
import json, sys
d = sys.argv[1]; j = json.load(open(f"digests/{d}.json", encoding="utf-8"))
assert j["date"] == d and j.get("items") and j.get("summary"), "invalid digest JSON"
bad = [i.get("title") for i in j["items"] if not (i.get("url", "").startswith("http") and i.get("date"))]
assert not bad, f"items missing url or date: {bad}"
txt = open(f"digests/{d}.json", encoding="utf-8").read() + open(f"digests/{d}.md", encoding="utf-8").read()
assert "\u2014" not in txt, "em dash found; rewrite without it"
print(f"digest OK: {len(j['items'])} items")
PY
python3 scripts/make_sources.py $([ "${CHECK_SOURCES:-0}" = 1 ] && echo --check)
python3 scripts/fetch_image.py "$DATE" || true
python3 site/build.py
bash scripts/scan_secrets.sh
git add -A
if git diff --cached --quiet; then echo "Nothing new to commit"; else git commit -q -m "digest: $DATE"; fi
[ "${SKIP_PUSH:-0}" = 1 ] || git push -q origin main
if [ "${SKIP_DEPLOY:-0}" != 1 ]; then
  [ -n "${CLOUDFLARE_API_TOKEN:-}" ] || { echo "CLOUDFLARE_API_TOKEN not set; skipping deploy"; exit 2; }
  cd site
  export WRANGLER_CACHE_DIR="${WRANGLER_CACHE_DIR:-/tmp/wrangler-cache}"
  WR=$(command -v wrangler || echo "npx --yes wrangler")
  $WR pages deploy dist --project-name "$PROJECT" --branch main --commit-dirty=true
  echo "Live: https://$PROJECT.pages.dev/"
fi
