# LINE Bot Research: sources

40 sources. Reachability checked 2026-11-23 (Asia/Bangkok, UTC+7) with a plain HTTP GET; the status is the last column (X accounts are checked through X tools).

Priority: P0 read every day; P1 read every day, include when relevant; P2 scan weekly or when needed.

## Platform changelog

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE Developers News (EN) | https://developers.line.biz/en/news/1/ | Official | Messaging API, LIFF, LINE MINI App, LINE Login, OA API changes, deprecations, price notices | P0 | HTML scrape (RSS endpoints return 403) | 200 |
| LINE Developers News (JA) | https://developers.line.biz/ja/news/1/ | Official | Japanese edition; sometimes has Japan-only notices | P1 | HTML scrape | 200 |
| X: @LINE_DEV | https://x.com/LINE_DEV | X account | LINE Developers official account (JA); its bio points to @lycorptech_jp for new posts | P1 | X API user timeline | X-API-verified |

## Engineering

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LY Corporation Tech Blog (EN) | https://techblog.lycorp.co.jp/en/feed/index.xml | Official | LINE / LY engineering posts, DevRel, platform internals | P1 | RSS | 200 |
| LY Corporation Tech Blog (JA) | https://techblog.lycorp.co.jp/ja/feed/index.xml | Official | Japanese engineering posts, more frequent than EN | P1 | RSS | 200 |
| X: @lycorptech_jp | https://x.com/lycorptech_jp | X account | LY Corporation tech account (JA), successor to @LINE_DEV | P1 | X API user timeline | X-API-verified |

## Corporate

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LY Corporation newsroom (EN) | https://www.lycorp.co.jp/en/news/ | Official | Press releases, earnings, security incidents, policy | P1 | HTML scrape (announcement IDs) | 200 |
| LY Corporation press releases on PR TIMES (JA) | https://prtimes.jp/companyrdf.php?company_id=129774 | Official | All LY Corp Japanese press releases with dates (filter for LINE OA, LINE bot, AI) | P1 | RSS | 200 |

## Thailand

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE Thailand Newsroom | https://linenewsroom.com/press-release | Official | LINE Thailand press releases (DevCon, MKTCON, LINE for Business) | P0 | HTML scrape (slugs; open page for date) | 200 |

## Thailand / pricing

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE for Business Thailand news | https://lineforbusiness.com/th/news | Official | LINE OA packages, Reply API changes, Thai business notices | P0 | HTML scrape (date in slug) | 200 |

## Japan / pricing

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE for Business Japan (LY biz) news | https://www.lycbiz.com/jp/news/ | Official | LINE OA and LINE Ads notices for Japan | P1 | manual | 200 |

## Taiwan / pricing

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE Biz Taiwan | https://tw.linebiz.com/ | Official | LINE OA plans and notices for Taiwan | P2 | manual | 200 |

## Thailand dev

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LINE Developers Thailand (Medium) | https://medium.com/feed/linedevth | Official community | LINE Thailand DevRel tutorials and announcements | P1 | RSS | 200 |

## SDK

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| line/line-bot-sdk-python releases | https://github.com/line/line-bot-sdk-python/releases.atom | GitHub | Python SDK releases | P0 | Atom | 200 |
| line/line-bot-sdk-nodejs releases | https://github.com/line/line-bot-sdk-nodejs/releases.atom | GitHub | Node.js SDK releases | P0 | Atom | 200 |
| line/line-bot-sdk-go releases | https://github.com/line/line-bot-sdk-go/releases.atom | GitHub | Go SDK releases | P1 | Atom | 200 |
| line/line-bot-sdk-java releases | https://github.com/line/line-bot-sdk-java/releases.atom | GitHub | Java SDK releases | P1 | Atom | 200 |
| line/line-bot-sdk-php releases | https://github.com/line/line-bot-sdk-php/releases.atom | GitHub | PHP SDK releases | P1 | Atom | 200 |
| line/line-bot-sdk-ruby releases | https://github.com/line/line-bot-sdk-ruby/releases.atom | GitHub | Ruby SDK releases | P2 | Atom | 200 |

## AI / MCP

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| line/line-bot-mcp-server releases | https://github.com/line/line-bot-mcp-server/releases.atom | GitHub | Official LINE MCP server for AI agents | P0 | Atom | 200 |

## API spec

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| line/line-openapi commits | https://github.com/line/line-openapi/commits/main.atom | GitHub | OpenAPI spec changes that precede SDK releases | P1 | Atom | 200 |

## LIFF

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| line/liff-cli releases | https://github.com/line/liff-cli/releases.atom | GitHub | LIFF CLI releases | P2 | Atom | 200 |
| @line/liff on npm | https://registry.npmjs.org/@line/liff | Package registry | LIFF SDK version and publish time | P1 | JSON API (dist-tags.latest and time) | 200 |

## AI chatbot builders

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Dify releases | https://github.com/langgenius/dify/releases.atom | GitHub | Dify releases (LINE via marketplace plugin) | P1 | Atom | 200 |
| n8n releases | https://github.com/n8n-io/n8n/releases.atom | GitHub | n8n releases (LINE node; LINE Notify node is legacy) | P2 | Atom (filter for LINE) | 200 |
| Botpress releases | https://github.com/botpress/botpress/releases.atom | GitHub | Botpress releases and LINE integration | P2 | Atom | 200 |
| Dify Marketplace: LINE Connect plugin | https://marketplace.dify.ai/plugin/suphachok/line-connect | Marketplace | Community LINE channel plugin for Dify | P2 | manual | 200 |
| n8n LINE node docs | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line/ | Docs | n8n LINE integration status | P2 | manual | 200 |

## Japan dev

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Zenn topic: linebot | https://zenn.dev/topics/linebot/feed | Community | Japanese developer articles on LINE bots | P1 | RSS | 200 |
| Zenn topic: liff | https://zenn.dev/topics/liff/feed | Community | Japanese LIFF / MINI App articles | P2 | RSS | 200 |
| Qiita tag: linebot | https://qiita.com/tags/linebot/feed | Community | Japanese LINE bot articles | P2 | Atom | 200 |
| Qiita tag: LINEmessagingAPI | https://qiita.com/tags/linemessagingapi/feed | Community | Messaging API articles | P2 | Atom | 200 |

## Global dev

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Medium tag: line-bot | https://medium.com/feed/tag/line-bot | Community | LINE bot tutorials, mostly Thai and Taiwanese authors | P2 | RSS | 200 |
| Medium tag: line-messaging-api | https://medium.com/feed/tag/line-messaging-api | Community | Messaging API tutorials | P2 | RSS | 200 |
| dev.to tag: linebot | https://dev.to/feed/tag/linebot | Community | English LINE bot posts | P2 | RSS | 200 |
| Hacker News (Algolia API) | https://hn.algolia.com/api/v1/search_by_date?query=LINE%20bot&tags=story | Community | HN stories mentioning LINE bot / Messaging API / LIFF / LY Corp | P2 | JSON API | 200 |

## Global market

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Google News: LINE Messaging API (EN) | https://news.google.com/rss/search?q=%22LINE+Messaging+API%22+OR+%22LINE+bot%22+OR+%22LINE+Official+Account%22+when:7d&hl=en-US&gl=US&ceid=US:en | News search | English coverage of LINE bots and OA | P1 | RSS | 200 |

## Thailand market

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Google News: LINE OA / แชทบอท LINE (TH) | https://news.google.com/rss/search?q=%22LINE+OA%22+OR+%22LINE+Official+Account%22+OR+%22LINE+%E0%B9%81%E0%B8%8A%E0%B8%97%E0%B8%9A%E0%B8%AD%E0%B8%97%22+when:7d&hl=th&gl=TH&ceid=TH:th | News search | Thai business news on LINE OA, chatbots, LINE Thailand | P0 | RSS | 200 |

## Japan market

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Google News: LINE公式アカウント / LINEヤフー (JA) | https://news.google.com/rss/search?q=%22LINE%E5%85%AC%E5%BC%8F%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%22+OR+%22LINE+Bot%22+OR+%22LINE%E3%83%9F%E3%83%8B%E3%82%A2%E3%83%97%E3%83%AA%22+when:7d&hl=ja&gl=JP&ceid=JP:ja | News search | Japanese news on LINE OA, LINE MINI App, LINE bots | P0 | RSS | 200 |

## Taiwan market

| Name | URL / feed / API | Type | Purpose | Priority | Fetch | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Google News: LINE 官方帳號 (TW) | https://news.google.com/rss/search?q=%22LINE+%E5%AE%98%E6%96%B9%E5%B8%B3%E8%99%9F%22+OR+%22LINE+Bot%22+-%22LINE+TODAY%22+when:7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant | News search | Taiwanese news on LINE OA and bots | P1 | RSS | 200 |
