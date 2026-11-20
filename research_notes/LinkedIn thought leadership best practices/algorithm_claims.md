# LinkedIn feed algorithm: documented claims vs folklore (as of Nov 2026)

IMPORTANT LIMITATION: WebFetch could not resolve buffer.com, searchengineland.com, news.linkedin.com, socialmediatoday.com or others in this session (network allowlist). All findings below come from WebSearch result summaries, not from reading the pages. Nothing here was verified against a primary page. Evidence ratings are therefore provisional: "A (via secondary)" means a secondary source attributes it to LinkedIn but I did not open the LinkedIn page. Re-verify A-rated items by opening the LinkedIn URLs before encoding them as rules.

Evidence levels: A = stated by LinkedIn; B = large third-party dataset; C = practitioner folklore, no verifiable source. [Unverified] = no source found.

## What has LinkedIn officially said about feed ranking?

### Takeaway
LinkedIn has publicly described an LLM-based retrieval plus transformer ("Generative Recommender"/Feed SR) ranking rebuild (engineering post dated 12 March 2026) and a newsroom post saying it works to make engagement pods and comment automation ineffective. It has not published ranking weights, link penalties, hashtag-count rules, or a "golden hour". 360Brew is not confirmed as the feed model.

### Cited Findings
- LinkedIn Engineering published a post on 12 March 2026 on rebuilding the feed with LLM-based unified retrieval and a Generative Recommender sequential ranking model, replacing multiple heterogeneous retrieval sources and independent impression-based ranking. Summary only, primary not opened. [A via secondary] — [ZenML summary](https://www.zenml.io/llmops-database/next-generation-feed-ranking-with-llms-and-sequential-transformers); [Search Engine Land](https://searchengineland.com/linkedin-updates-feed-algorithm-llm-ranking-retrieval-471708); [ByteByteGo](https://blog.bytebytego.com/p/how-linkedin-feed-uses-llms-to-serve)
- LinkedIn research papers on the underlying systems: Feed SR sequential recommender replacing a DCNv2 ranker [arXiv 2602.12354](https://arxiv.org/html/2602.12354v1); LLM/causal-LM retrieval for Feed [arXiv 2510.14223](https://www.alphaxiv.org/abs/2510.14223.md); earlier "From Features to Transformers" [arXiv 2502.03417](https://arxiv.org/html/2502.03417v2). [A] (patent/paper-class sources; I saw titles only, not full text)
- LinkedIn newsroom post "How LinkedIn Is Improving the Feed to Show More Relevant, Authentic Professional Content" (2026) reportedly says LinkedIn is working to make engagement pods ineffective and curb comment automation and third-party tools creating fake conversations. [A via secondary; page not opened] — [news.linkedin.com/2026/ImprovingTheFeed](https://news.linkedin.com/2026/ImprovingTheFeed) (appeared in search results). A roundup attributes to Tim Jurka the statement that pod comments, automation and extensions are not allowed — [Search roundup via Sendible/PR-news results](https://www.sendible.com/insights/linkedin-algorithm?hs_amp=true) (weak secondary).
- Dwell time as a Feed signal was described by LinkedIn engineers in 2020 (May 2020 engineering post, per secondary) and sources note there is no single dwell threshold; it depends on content type. [A, 2020, via secondary] — [summary in 360Brew search results](https://authoredup.com/blog/linkedin-360brew). Specific thresholds in blogs (8s, 15s, 31-60s) are [Unverified] and mutually inconsistent — [Medium/HypergrowthSI-type results](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach).
- 360Brew: a secondary source states the March 2026 engineering post never uses the name 360Brew and LinkedIn has not confirmed it runs the feed; other blogs claim 150B-parameter model powers everything. Dates conflict (late 2024 vs 2026). Treat as [Unverified] for feed ranking — [Authoredup](https://authoredup.com/blog/linkedin-360brew); [DEV Community](https://dev.to/nicolasai/reverse-engineering-linkedins-360brew-from-their-engineering-blog-4jm6); [Substack](https://adilghazali.substack.com/p/a-150-billion-parameter-model-now)
- Hashtags: one report says LinkedIn confirmed hashtags help route content to audiences but do not increase reach. [A? weakly sourced, no primary found] — [search roundup](https://everything-pr.com/getting-more-visibility-on-linkedin)
- Early engagement: a newsletter claims Creator Mode guidance said early engagement is a strong signal; I could not confirm. [Unverified] — [LinkedIn's Golden Hour newsletter](https://thelunchbreak.beehiiv.com/p/linkedin-s-golden-hour)
- Earlier official engagement-signal expansion (personalization signals), date not confirmed — [Social Media Today](https://www.socialmediatoday.com/news/linkedin-expands-engagement-signals-to-better-personalize-user-feeds/691711/)

### Inferences
- Safe official-level rules: write substantive, authentic professional content; do not use pods/automation/engagement bait. Nothing official supports numeric rules (hashtag counts, link penalties percentages, time windows).

### Gaps
- Could not open any LinkedIn primary page (engineering.linkedin.com, news.linkedin.com, Help Center) or Search Engine Land/Buffer; need network allowlist. Did not find LinkedIn Help Center text on editing posts, tagging, or posting frequency. Creator Mode retirement / Post Quality details not found.

## Claim table

| Claim | Evidence | Source / note |
|---|---|---|
| Feed uses LLM retrieval + transformer sequential ranker (Mar 2026) | A (via secondary) | [ZenML](https://www.zenml.io/llmops-database/next-generation-feed-ranking-with-llms-and-sequential-transformers), [arXiv](https://arxiv.org/html/2602.12354v1) |
| Pods, comment automation, third-party engagement tools are targeted | A (via secondary) | [LinkedIn newsroom](https://news.linkedin.com/2026/ImprovingTheFeed) |
| Dwell time is a ranking signal | A (2020, secondary) | [Authoredup](https://authoredup.com/blog/linkedin-360brew); no official threshold |
| Specific dwell thresholds (8s/15s/31-60s) | C | [Zoomsphere](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach) |
| 360Brew runs the feed | C / [Unverified] | LinkedIn post does not name it ([Authoredup](https://authoredup.com/blog/linkedin-360brew)) |
| Comments count "2x" likes; weighted multipliers | C | [Medium](https://medium.com/@HypergrowthSI/5-steps-to-10x-your-linkedin-reach-in-2026-comments-now-count-2x-more-than-likes-aa6d5bedf60d); no LinkedIn source found |
| External links lower reach (direction) | B (moderate) | Buffer 2M+ posts: link posts lowest median engagement ([Buffer](https://buffer.com/resources/how-often-to-post-on-linkedin/)); MagicPost 865,980 posts ([study](https://magicpost.in/studies/linkedin-link-penalty)); small tests: Hootsuite 2021 (7 vs 177 posts) ([Hootsuite](https://blog.hootsuite.com/linkedin-engagement-experiment/)), CloudZero/Buffer single-company ([Buffer](https://buffer.com/resources/linkedin-posts)) |
| Link penalty is ~60% | C | [Bulldog Reporter](https://www.agilitypr.com/pr-news/social-media-influencer-marketing/the-linkedin-link-tax-why-sharing-your-blog-is-costing-you-60-percent-of-your-audience/); one roundup says figure appears in no LinkedIn source |
| Van der Blom: single external link ~18.8% cost (Apr 2025), since lower | C/B (practitioner dataset, not independently audited) | Reported secondhand in [search result](https://contentin.io/blog/should-you-put-links-in-linkedin-posts/) |
| Link in first comment avoids penalty | Contradicted/mixed | MagicPost: ~2% fewer impressions vs link in body (no measurable diff) ([study](https://magicpost.in/studies/linkedin-link-penalty)); others claim 2026 penalty with no data ([SocialSync](https://www.socialync.io/blog/links-in-captions-vs-first-comment-2026)). Treat as unresolved; click-through suffers either way |
| Exactly 3 hashtags is optimal | C | Single-company CloudZero data ([Buffer](https://buffer.com/resources/linkedin-posts)); LinkedIn says hashtags route, not boost reach |
| Golden hour (first 60 min decides reach) | C / contradicted | No official source; 427-post vendor dataset found first hour = ~7% of 30-day impressions ([ContentIn](https://contentin.io/glossary/golden-hour/)); others claim 3-8 hr evaluation, unverified |
| Post 2-5x/week | B | Buffer 2M+ posts, 94k+ accounts, controlled for account size ([Buffer](https://buffer.com/resources/how-often-to-post-on-linkedin/)) |
| Carousels/documents strongest format | B (vendor) | Buffer 2M posts; 6.60% doc engagement figure in a blog ([search result](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach)) |
| Native video +69% | C (single secondary) | [Writtenly](https://www.writtenlyhub.com/news/linkedin-engagement-down-50-algorithm-insights-report-2025) |
| Organic reach down ~50% YoY in 2025 | B/C (Van der Blom report via secondary; sample 1.3M-1.8M posts inconsistent across write-ups) | [Writtenly](https://www.writtenlyhub.com/news/linkedin-engagement-down-50-algorithm-insights-report-2025) |
| AI-generic content gets 47% less reach | C | single blog ([Zoomsphere](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach)) |
| Engagement pods work | Contradicted by A | [LinkedIn newsroom](https://news.linkedin.com/2026/ImprovingTheFeed) |
| Editing a post resets/kills reach | [Unverified] | no source found |
| Tagging people boosts/penalizes reach | [Unverified] | no source found |

## What do large third-party analyses say (dwell, comments, links, hashtags, tagging, editing, frequency, early window)?

### Takeaway
Only frequency, format and link-direction have sizeable datasets (Buffer 2M+ posts; MagicPost 866k posts). Comments-vs-reactions weights, tagging, editing, hashtag count and timing windows rest on small or vendor data.

### Cited Findings
- Buffer, 2M+ posts from 94,000+ accounts: 2-5 posts/week is the sweet spot; gains continue at 11+/week; carousels best; link posts lowest median engagement — [Buffer](https://buffer.com/resources/how-often-to-post-on-linkedin/)
- MagicPost, 865,980 posts, 15,719 creators, Jul 2024-Jul 2026: first-comment link ~2% fewer impressions than in-body link among 1,824 creators who did both — [MagicPost](https://magicpost.in/studies/linkedin-link-penalty). Vendor study, methodology not reviewed.
- Hootsuite 2021 experiment: no-link posts 6x reach, but 7 vs 177 posts — [Hootsuite](https://blog.hootsuite.com/linkedin-engagement-experiment/) (2021)
- CloudZero via Buffer, 400+ posts, one company: no-link posts 1.7x likes, 4.1x comments; 3-hashtag posts avg 15 likes vs ~1 for none — [Buffer](https://buffer.com/resources/linkedin-posts). Single account, correlational.
- Van der Blom Algorithm Insights Report 2025: views -50%, engagement -25%, follower growth -59% (secondary) — [Writtenly](https://www.writtenlyhub.com/news/linkedin-engagement-down-50-algorithm-insights-report-2025). Primary (richardvanderblom.com) not accessed.
- Link in first comment A/B tests exist (GrowthRocks) but results not read — [GrowthRocks](https://growthrocks.com/blog/linkedin-abtest-link-in-comment/)

### Inferences
- Reasonable defaults: avoid link in post body when reach is the goal; do not claim first-comment links are a proven workaround or a proven penalty; do not state hashtag counts or time windows as rules.

### Gaps
- No large dataset found for comments vs reactions weighting, tagging, editing. Socialinsider, Sprout and Authoredup studies not located in detail.

## Which popular claims are contradicted or unsupported?

### Takeaway
Pods: contradicted by LinkedIn. Golden hour, 3-hashtag rule, 60% link penalty, comment multipliers, edit/tag penalties: no official support. First-comment link: mixed data.

### Cited Findings
- See claim table rows above.

### Inferences
- A writing skill should phrase these as "tested heuristics" or omit them.

### Gaps
- Could not check Hootsuite/Sprout/Socialinsider primary pages.

## What changed in 2025-2026 that makes older advice obsolete?

### Takeaway
Ranking moved to LLM retrieval and sequential transformer ranking (publicly described Mar 2026) with stated crackdown on pods/automation; practitioner reports show reach declines through 2025 and favor topical authority and dwell over hashtag/timing tricks.

### Cited Findings
- Mar 2026 feed rebuild — [ZenML](https://www.zenml.io/llmops-database/next-generation-feed-ranking-with-llms-and-sequential-transformers)
- Pod/automation crackdown — [LinkedIn newsroom](https://news.linkedin.com/2026/ImprovingTheFeed)
- Reach down ~50% YoY in 2025 per Van der Blom report (secondary) — [Writtenly](https://www.writtenlyhub.com/news/linkedin-engagement-down-50-algorithm-insights-report-2025)
- Claims of link penalty shrinking since Apr 2025 are practitioner-sourced — [ContentIn](https://contentin.io/blog/should-you-put-links-in-linkedin-posts/)
- Practitioner claim that topic authority/semantic relevance now drives visibility (360Brew framing) — [Substack](https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority) [Unverified as LinkedIn policy]

### Inferences
- Pre-2025 rules (timing, hashtag counts, pods, first-comment links) should be considered stale or unproven.

### Gaps
- No official LinkedIn doc on Post Quality/Creator Mode changes; no confirmed 2026 link-penalty change.
