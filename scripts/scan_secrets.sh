#!/usr/bin/env bash
# Scan files about to be committed for token / key patterns. Prints file names and line numbers only, never the matched value.
set -uo pipefail
cd "$(dirname "$0")/.."
# Token prefixes must sit on a word boundary so URL paths like risk-report do not trip sk-.
PAT='((?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{20,}|(?<![A-Za-z0-9_])github_pat_[A-Za-z0-9_]{20,}|(?<![A-Za-z0-9_])sk-[A-Za-z0-9_-]{20,}|(?<![A-Za-z0-9_])AKIA[0-9A-Z]{16}|(?<![A-Za-z0-9_])xox[abpors]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(CLOUDFLARE_API_TOKEN|CF_API_TOKEN|CHANNEL_ACCESS_TOKEN|CHANNEL_SECRET|API_KEY|SECRET|PASSWORD)\s*[:=]\s*["'"'"']?[A-Za-z0-9_\-]{12,})'
FILES=$(git ls-files --cached --others --exclude-standard)
hits=0
if [ -n "$FILES" ]; then
  if echo "$FILES" | xargs -d '\n' rg -n -o --pcre2 --no-heading -e "$PAT" -r '<redacted>' 2>/dev/null; then hits=1; fi
  for v in CLOUDFLARE_API_TOKEN CLOUDFLARE_ACCOUNT_ID GH_TOKEN GITHUB_TOKEN LINE_CHANNEL_ACCESS_TOKEN LINE_CHANNEL_SECRET; do
    val="${!v:-}"
    if [ -n "$val" ] && echo "$FILES" | xargs -d '\n' rg -l -F -- "$val" 2>/dev/null; then
      echo "The files above contain the value of env var $v"; hits=1
    fi
  done
fi
if [ "$hits" -ne 0 ]; then echo "Possible secret found. Not committing."; exit 1; fi
echo "Secret scan passed: no token or key patterns found."
