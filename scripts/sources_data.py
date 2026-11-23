# Source list for LINE Bot Research Daily. Edit only this file, then run make_sources.py.
# Fields: name, url, type, area, purpose, priority, fetch
# fetch: RSS / Atom are read by fetch_feeds.py; "HTML scrape" sources have a parser in fetch_feeds.py; "manual" are checked by reading the page.
S = [
# Official LINE / LY Corporation
("LINE Developers News (EN)","https://developers.line.biz/en/news/1/","Official","Platform changelog","Messaging API, LIFF, LINE MINI App, LINE Login, OA API changes, deprecations, price notices","P0","HTML scrape (RSS endpoints return 403)"),
("LINE Developers News (JA)","https://developers.line.biz/ja/news/1/","Official","Platform changelog","Japanese edition; sometimes has Japan-only notices","P1","HTML scrape"),
("LY Corporation Tech Blog (EN)","https://techblog.lycorp.co.jp/en/feed/index.xml","Official","Engineering","LINE / LY engineering posts, DevRel, platform internals","P1","RSS"),
("LY Corporation Tech Blog (JA)","https://techblog.lycorp.co.jp/ja/feed/index.xml","Official","Engineering","Japanese engineering posts, more frequent than EN","P1","RSS"),
("LY Corporation newsroom (EN)","https://www.lycorp.co.jp/en/news/","Official","Corporate","Press releases, earnings, security incidents, policy","P1","HTML scrape (announcement IDs)"),
("LY Corporation press releases on PR TIMES (JA)","https://prtimes.jp/companyrdf.php?company_id=129774","Official","Corporate","All LY Corp Japanese press releases with dates (filter for LINE OA, LINE bot, AI)","P1","RSS"),
("LINE Thailand Newsroom","https://linenewsroom.com/press-release","Official","Thailand","LINE Thailand press releases (DevCon, MKTCON, LINE for Business)","P0","HTML scrape (slugs; open page for date)"),
("LINE for Business Thailand news","https://lineforbusiness.com/th/news","Official","Thailand / pricing","LINE OA packages, Reply API changes, Thai business notices","P0","HTML scrape (date in slug)"),
("LINE for Business Japan (LY biz) news","https://www.lycbiz.com/jp/news/","Official","Japan / pricing","LINE OA and LINE Ads notices for Japan","P1","manual"),
("LINE Biz Taiwan","https://tw.linebiz.com/","Official","Taiwan / pricing","LINE OA plans and notices for Taiwan","P2","manual"),
("LINE Developers Thailand (Medium)","https://medium.com/feed/linedevth","Official community","Thailand dev","LINE Thailand DevRel tutorials and announcements","P1","RSS"),
# SDKs and official repos
("line/line-bot-sdk-python releases","https://github.com/line/line-bot-sdk-python/releases.atom","GitHub","SDK","Python SDK releases","P0","Atom"),
("line/line-bot-sdk-nodejs releases","https://github.com/line/line-bot-sdk-nodejs/releases.atom","GitHub","SDK","Node.js SDK releases","P0","Atom"),
("line/line-bot-sdk-go releases","https://github.com/line/line-bot-sdk-go/releases.atom","GitHub","SDK","Go SDK releases","P1","Atom"),
("line/line-bot-sdk-java releases","https://github.com/line/line-bot-sdk-java/releases.atom","GitHub","SDK","Java SDK releases","P1","Atom"),
("line/line-bot-sdk-php releases","https://github.com/line/line-bot-sdk-php/releases.atom","GitHub","SDK","PHP SDK releases","P1","Atom"),
("line/line-bot-sdk-ruby releases","https://github.com/line/line-bot-sdk-ruby/releases.atom","GitHub","SDK","Ruby SDK releases","P2","Atom"),
("line/line-bot-mcp-server releases","https://github.com/line/line-bot-mcp-server/releases.atom","GitHub","AI / MCP","Official LINE MCP server for AI agents","P0","Atom"),
("line/line-openapi commits","https://github.com/line/line-openapi/commits/main.atom","GitHub","API spec","OpenAPI spec changes that precede SDK releases","P1","Atom"),
("line/liff-cli releases","https://github.com/line/liff-cli/releases.atom","GitHub","LIFF","LIFF CLI releases","P2","Atom"),
("@line/liff on npm","https://registry.npmjs.org/@line/liff","Package registry","LIFF","LIFF SDK version and publish time","P1","JSON API (dist-tags.latest and time)"),
# AI chatbot builders with LINE integrations
("Dify releases","https://github.com/langgenius/dify/releases.atom","GitHub","AI chatbot builders","Dify releases (LINE via marketplace plugin)","P1","Atom"),
("n8n releases","https://github.com/n8n-io/n8n/releases.atom","GitHub","AI chatbot builders","n8n releases (LINE node; LINE Notify node is legacy)","P2","Atom (filter for LINE)"),
("Botpress releases","https://github.com/botpress/botpress/releases.atom","GitHub","AI chatbot builders","Botpress releases and LINE integration","P2","Atom"),
("Dify Marketplace: LINE Connect plugin","https://marketplace.dify.ai/plugin/suphachok/line-connect","Marketplace","AI chatbot builders","Community LINE channel plugin for Dify","P2","manual"),
("n8n LINE node docs","https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line/","Docs","AI chatbot builders","n8n LINE integration status","P2","manual"),
# Developer community
("Zenn topic: linebot","https://zenn.dev/topics/linebot/feed","Community","Japan dev","Japanese developer articles on LINE bots","P1","RSS"),
("Zenn topic: liff","https://zenn.dev/topics/liff/feed","Community","Japan dev","Japanese LIFF / MINI App articles","P2","RSS"),
("Qiita tag: linebot","https://qiita.com/tags/linebot/feed","Community","Japan dev","Japanese LINE bot articles","P2","Atom"),
("Qiita tag: LINEmessagingAPI","https://qiita.com/tags/linemessagingapi/feed","Community","Japan dev","Messaging API articles","P2","Atom"),
("Medium tag: line-bot","https://medium.com/feed/tag/line-bot","Community","Global dev","LINE bot tutorials, mostly Thai and Taiwanese authors","P2","RSS"),
("Medium tag: line-messaging-api","https://medium.com/feed/tag/line-messaging-api","Community","Global dev","Messaging API tutorials","P2","RSS"),
("dev.to tag: linebot","https://dev.to/feed/tag/linebot","Community","Global dev","English LINE bot posts","P2","RSS"),
("Hacker News (Algolia API)","https://hn.algolia.com/api/v1/search_by_date?query=LINE%20bot&tags=story","Community","Global dev","HN stories mentioning LINE bot / Messaging API / LIFF / LY Corp","P2","JSON API"),
# Market news (Google News searches, last 7 days)
("Google News: LINE Messaging API (EN)","https://news.google.com/rss/search?q=%22LINE+Messaging+API%22+OR+%22LINE+bot%22+OR+%22LINE+Official+Account%22+when:7d&hl=en-US&gl=US&ceid=US:en","News search","Global market","English coverage of LINE bots and OA","P1","RSS"),
("Google News: LINE OA / แชทบอท LINE (TH)","https://news.google.com/rss/search?q=%22LINE+OA%22+OR+%22LINE+Official+Account%22+OR+%22LINE+%E0%B9%81%E0%B8%8A%E0%B8%97%E0%B8%9A%E0%B8%AD%E0%B8%97%22+when:7d&hl=th&gl=TH&ceid=TH:th","News search","Thailand market","Thai business news on LINE OA, chatbots, LINE Thailand","P0","RSS"),
("Google News: LINE公式アカウント / LINEヤフー (JA)","https://news.google.com/rss/search?q=%22LINE%E5%85%AC%E5%BC%8F%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%22+OR+%22LINE+Bot%22+OR+%22LINE%E3%83%9F%E3%83%8B%E3%82%A2%E3%83%97%E3%83%AA%22+when:7d&hl=ja&gl=JP&ceid=JP:ja","News search","Japan market","Japanese news on LINE OA, LINE MINI App, LINE bots","P0","RSS"),
("Google News: LINE 官方帳號 (TW)","https://news.google.com/rss/search?q=%22LINE+%E5%AE%98%E6%96%B9%E5%B8%B3%E8%99%9F%22+OR+%22LINE+Bot%22+-%22LINE+TODAY%22+when:7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant","News search","Taiwan market","Taiwanese news on LINE OA and bots","P1","RSS"),
# X accounts (checked manually or via X tools)
("X: @LINE_DEV","https://x.com/LINE_DEV","X account","Platform changelog","LINE Developers official account (JA); its bio points to @lycorptech_jp for new posts","P1","X API user timeline"),
("X: @lycorptech_jp","https://x.com/lycorptech_jp","X account","Engineering","LY Corporation tech account (JA), successor to @LINE_DEV","P1","X API user timeline"),
]
