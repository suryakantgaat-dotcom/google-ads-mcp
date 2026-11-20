# Verification of algorithm_claims.md against primary pages (checked 2026-11-20)

Method: pages fetched with `curl -sL --max-time 30 -A "Mozilla/5.0"` through the agent proxy and HTML stripped with a small python3 -I script. No TLS verification was disabled and no bot protection was bypassed. Quotes below are copied from the fetched page text.

Evidence levels: A = stated by LinkedIn and read on a primary LinkedIn page this session; B = large dataset; C = folklore; [Unverified] = nothing found. Status column: CONFIRMED / CORRECTED / CONTRADICTED / NOT FOUND.

## 1. Host access log

| Host / URL | Result |
|---|---|
| news.linkedin.com/2026/ImprovingTheFeed | 200, read in full |
| news.linkedin.com/2026 (listing) | 200, no post list rendered (static shell only) |
| www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed | 200, read in full (engineering.linkedin.com/blog redirects to www.linkedin.com/blog/engineering) |
| www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time | 200, read in full |
| www.linkedin.com/help/linkedin/answer/a1339724 (LinkedIn relevance), 137371 -> a1340752 (false or misleading), 137372 -> a1338787 (spam), /legal/professional-community-policies | 200, read |
| www.linkedin.com/pulse/... (Tim Jurka "How Does the LinkedIn Feed Work?"; Oscar Rodriguez "Where Real Conversations Matter") | BLOCKED: HTTP 403, Cloudflare "Just a moment..." challenge. Not bypassed. Content NOT read |
| arxiv.org/abs/2602.12354, 2510.14223, 2502.03417; arxiv.org/html/2602.12354v1 | 200, read |
| searchengineland.com (article URL and homepage) | BLOCKED: HTTP 403 "Just a moment..." challenge |
| ppc.land | BLOCKED: HTTP 403 "Just a moment..." challenge |
| www.socialmediatoday.com and socialmediatoday.com | BLOCKED by agent proxy: `CONNECT tunnel failed, response 403` (host not allowed for this session despite the allowlist note) |
| www.contentgrip.com and contentgrip.com | BLOCKED by agent proxy: `CONNECT tunnel failed, response 403` |
| Several guessed Help Center answer IDs | 404 or unrelated pages; no Help Center page on editing, hashtags or external links was located |

Consequence: no trade-press page (Search Engine Land, Social Media Today, PPC Land, ContentGrip) could be read. Trade-press coverage remains "not verified"; the primary LinkedIn pages were enough to settle the core items.

## 2. Primary-page findings (exact quotes)

### 2a. LinkedIn Engineering, "Engineering the next generation of LinkedIn's Feed" (Hristo Danchev, March 12, 2026)
URL: https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed
- "we're rolling out a new advanced ranking system, powered by LLMs and GPUs, that better understands what a post is actually about and how it relates to a member's evolving interests and career goals."
- Retrieval: "For years, the LinkedIn Feed retrieval relied on a heterogeneous architecture... a chronological index of your network's activities, trending posts in your geography, collaborative filtering based on similar members' interests, industry-specific trending content, and several embedding-based retrieval systems." It is replaced by LLM-based retrieval (member and post "prompts" turned into embeddings, GPU nearest-neighbor search).
- Ranking: "So we built a Generative Recommender (GR) model for LinkedIn's Feed that reimagines ranking by treating your feed interaction history as a sequence... GR processes more than a thousand of your historical interactions."
- Signals: "your actions (long dwells, likes, comments, shares) are embedded and interleaved with post representations"; prediction head: "passive tasks (click, skip, long-dwell) and active tasks (like, comment, share) get specialized gating".
- Signals from the profile and history: "information you've chosen to share on your own profile such as industry, experience, skills and geography ... how you engage with content over time, including what you've read, liked, commented on, returned back to, or simply scrolled past."
- Freshness: "When a post is published or gains engagement, we update its item prompt... The entire process happens within minutes."
- Number features: percentile-bucketed popularity, engagement rates, recency signals and affinity scores are fed to the model as tokens.
- The post contains no mention of "360Brew" (grep count 0), of hashtags, external links, editing, or AI-generated content.

### 2b. arXiv papers (read abstract pages; 2602.12354 also HTML full text)
- 2602.12354 "An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking" (Hertel et al., submitted 12 Feb 2026): "We present Feed Sequential Recommender (Feed SR), a transformer-based sequential ranking model for LinkedIn Feed that replaces a DCNv2-based ranker... Feed SR has been serving the majority of LinkedIn's Feed traffic for over three months and shows significant improvements in member engagement (+2.10% time spent, +3.52% like, comments, or reshares) in online A/B tests". Full text lists "popularity, dwell-time buckets, post age, and explicit affinity between viewer and action/root-actor" as numeric features and "click, skip, and long-dwell" as passive tasks. Confirms dwell is a modeled signal.
- 2510.14223 "Large Scale Retrieval for the LinkedIn Feed using Causal Language Models" (submitted 16 Oct 2025): fine-tunes "Meta's LLaMA 3 as a dual encoder" for suggested (out-of-network) content: "2000 candidates are retrieved from a pool of hundreds of millions". Scope: retrieval of suggested content only.
- 2502.03417 "From Features to Transformers: Redefining Ranking for Scalable Impact" (LiGR): transformer ranking, deprecates most hand-built features.

### 2c. news.linkedin.com, "How LinkedIn Is Improving the Feed to Show More Relevant, Authentic Professional Content" (Published Mar 12, 2026, LinkedIn Corporate Communications Team)
URL: https://news.linkedin.com/2026/ImprovingTheFeed
- "Smarter content ranking using Generative Recommenders and LLMs: LinkedIn is rolling out more advanced models that better understand what posts are about and how members' interests change over time."
- "Action against automated comments and inauthentic engagement: We're working to make engagement pods ineffective and curb comment automation or third party tools that create fake conversations, so real people and real perspectives stand out."
- "Less generic content and engagement bait: We're reducing recycled and click-driven posts to make the Feed feel more useful. We want the Feed to be relevant to your interests, not a popularity contest."
- "That's why we take action to stop behaviors that promote inauthentic engagement, including comment automation, engagement pods, and unauthorized third-party tools."
- "This isn't about limiting reach or discouraging participation."
- "We're improving our systems to reduce repetitive, low-substance posts and engagement bait, such as 'comment to agree' prompts or videos that don't match the text."
- "You'll see more posts that offer genuine insight, actionable ideas, and thoughtful perspectives and fewer that are designed purely to game distribution."
- Also: Interest Picker being tested at sign-up. "These changes are already rolling out."
- NOT in the post: any mention of "AI", "AI-generated" or "slop"; any "Seems like AI slop" report option. The target is "generic", "recycled", "repetitive, low-substance" and "engagement bait", not AI authorship as such. The post links to the Tim Jurka and Oscar Rodriguez LinkedIn Pulse articles, which were 403-blocked and not read. (Third-party roundups attribute the statement about pods to Tim Jurka; that could not be checked.)

### 2d. Other LinkedIn primary pages
- Help Center, "LinkedIn relevance - Optimizing the member experience" (https://www.linkedin.com/help/linkedin/answer/a1339724, "Last updated: 7 months ago"):
  - "These algorithms also filter out or taper distribution of low-quality and unsafe content to enhance the value of what you see on your Feed."
  - Content signals listed: "How often a post is viewed or engaged with. What the post is about and whether it provides knowledge or advice. How recent the content is. Whether the content comes from someone you follow or are connected to. The language of the post. How constructive or professional the conversation is. Tagged people, companies, or topics."
  - Activity signals: "Content you spend the most time viewing." and "Engagement others have with your posts and how recent it is."
  - "Feed distribution isn't influenced by payments from third parties to LinkedIn, except for promoted (paid) content".
  - No mention of external links, hashtags, editing, posting frequency, or AI content.
- Engineering, "Understanding dwell time to improve LinkedIn feed ranking" (Siddharth Dangi, May 12, 2020): dwell on the feed "starts measuring when at least half of a feed update is visible"; a "P(skip)" model predicts dwell below a threshold T_skip and "reducing the score of all updates by an amount proportional to the predicted P(skip)". The post says a single skip threshold works across text, image and video, but it does not publish a number of seconds. Also: "we don't want to blindly increase members' time spent on the feed".
- Help Center spam policy (https://www.linkedin.com/help/linkedin/answer/a1338787, last updated 2 years ago): "We may remove or limit the distribution of content designed to artificially increase engagement through misuse or misrepresentation of LinkedIn's features." Examples: "Emoji / reaction polls that artificially boost engagement", "Widely circulated 'chain letter'-type content, requesting likes, reactions, and shares", "Excessive, irrelevant, or repetitive comments or messages".
- Help Center false or misleading content (https://www.linkedin.com/help/linkedin/answer/a1340752): synthetic or manipulated media must be disclosed when it misrepresents real events; "Content that is false or substantially misleading but not likely to cause harm is not eligible for distribution beyond the author's network." This is about deceptive synthetic media, not about AI-assisted writing.
- Professional Community Policies page: nothing on AI-written text. Searched for "AI", "slop", "generat" with no relevant hit.

### 2e. Not found anywhere readable
- Any "Seems like AI slop" (or similar) report option on a LinkedIn page. NOT FOUND. Cannot be confirmed or denied; it may exist in the product UI or in the blocked Pulse articles.
- Any LinkedIn statement on external-link penalties, hashtag effects (count or reach), editing a post, golden hour, comment-to-like weighting, posting frequency, or 360Brew. NOT FOUND on all readable primary pages.

## 3. Claim-by-claim verification

| # | Claim (from algorithm_claims.md) | Old level | Primary page result | Status | New level |
|---|---|---|---|---|---|
| 1 | Feed uses LLM retrieval plus transformer sequential ranker (rebuild dated 12 Mar 2026) | A (via secondary) | Engineering post dated March 12, 2026 and newsroom post of same date both say so. Quote in 2a/2c | CONFIRMED | A (read on primary) |
| 2 | Replaces multiple heterogeneous retrieval sources and independent impression-based ranking | A (via secondary) | Post: heterogeneous retrieval sources replaced by LLM-based retrieval; "Traditional ranking models evaluate each impression independently" vs GR sequence model | CONFIRMED | A |
| 3 | arXiv 2602.12354 = Feed SR replacing DCNv2 ranker | A (titles only) | Abstract read: transformer Feed SR "replaces a DCNv2-based ranker"; +2.10% time spent, +3.52% like/comment/reshare in A/B | CONFIRMED (corrected detail: paper is the ranker; the Mar 2026 blog calls its model "Generative Recommender (GR)", and the paper's model is named Feed SR, so treat the two names as describing the same family, not proven identical) | A (paper) |
| 4 | arXiv 2510.14223 = LLM/causal-LM retrieval for Feed | A (titles only) | Abstract read: LLaMA 3 dual encoder; applies to suggested (out-of-network) content, 2000 candidates | CONFIRMED (scope narrowed to suggested content) | A (paper) |
| 5 | arXiv 2502.03417 "From Features to Transformers" | A (title only) | Abstract read: LiGR transformer ranking framework | CONFIRMED | A (paper) |
| 6 | Newsroom post: pods ineffective, comment automation and third-party fake-conversation tools curbed | A (via secondary) | Quotes in 2c | CONFIRMED | A |
| 7 | Newsroom attributes to Tim Jurka that pod comments, automation, extensions are not allowed | weak secondary | Newsroom post has no named author ("LinkedIn Corporate Communications Team") and does not quote Jurka; it says "comment automation, engagement pods, and unauthorized third-party tools". Jurka Pulse article 403-blocked | NOT FOUND (name attribution); wording partly CORRECTED: "not allowed" is not in the post, it says LinkedIn "take[s] action to stop" these | [Unverified] for Jurka quote; A for the unattributed corporate statement |
| 8 | Pods work (popular claim) | Contradicted by A | LinkedIn says it is working to make pods ineffective and that the change is "already rolling out". Not a measurement of effectiveness | CONFIRMED as contradicted by LinkedIn's stated intent | A (intent only; no effectiveness data) |
| 9 | Newsroom post targets generic/low-quality AI content | (implicit in notes and a 47% stat) | Post targets "generic", "recycled", "repetitive, low-substance" posts and engagement bait. It never says "AI". | CORRECTED: policy is about quality and engagement bait, not AI authorship | A for "less generic content and engagement bait"; "penalizes AI-written content" = [Unverified] |
| 10 | Engagement bait is reduced | not in table | "comment to agree" prompts and "videos that don't match the text" named as examples | CONFIRMED (new item) | A |
| 11 | "Seems like AI slop" report option | not in notes | Not found on any readable page | NOT FOUND | [Unverified] |
| 12 | Dwell time is a ranking signal (2020 engineering post) | A (2020, secondary) | 2020 post read: P(skip) model with T_skip; Mar 2026 post and arXiv 2602.12354 list "long dwells"/"long-dwell" as modeled passive action; Help Center lists "Content you spend the most time viewing" | CONFIRMED, and now also current (2026) | A |
| 13 | No official dwell threshold | stated in notes | 2020 post publishes no seconds value; says one T_skip works across formats | CONFIRMED | A |
| 14 | Specific dwell thresholds 8s/15s/31-60s | C | Nothing on any primary page | NOT FOUND | C |
| 15 | 360Brew runs the feed | C / [Unverified] | Mar 2026 engineering post does not contain "360Brew" (grep count 0); newsroom post does not either | CONFIRMED as unsupported (LinkedIn does not name it) | [Unverified] / C |
| 16 | Hashtags route content but do not increase reach (LinkedIn confirmed) | A? weak | Help Center lists "Tagged people, companies, or topics" as a content signal, but says nothing about hashtag count or reach | CORRECTED: only a generic "tagged ... topics" signal confirmed; the "do not increase reach" statement not found | [Unverified] (route/reach statement); A only for "tags are a content signal" |
| 17 | Exactly 3 hashtags is optimal | C | No LinkedIn source | NOT FOUND | C |
| 18 | Tagging people boosts/penalizes reach | [Unverified] | Help Center lists "Tagged people, companies, or topics" among content signals used for relevance. Direction and size not stated | CORRECTED: tags are a used signal; boost/penalty claim still unsupported | A for "signal exists"; [Unverified] for any boost or penalty |
| 19 | Editing a post resets or kills reach | [Unverified] | Nothing on any readable page. (Engineering post: when a post "gains engagement, we update its item prompt", but this does not mention edits) | NOT FOUND | [Unverified] |
| 20 | External links lower reach (direction) | B | No LinkedIn statement on links on any readable primary page | NOT FOUND (primary); dataset evidence unchanged | B (unchanged; not re-checked, Buffer/MagicPost not in allowlist) |
| 21 | Link penalty is ~60% / ~18.8% / first-comment link effects | C / C-B / mixed | No LinkedIn source | NOT FOUND | C / C-B / mixed (unchanged) |
| 22 | Comments count "2x" likes; weighted multipliers | C | 2020 post: score is "a weighted linear combination" of predicted click and viral-action quantities, with weights "tuned" for balance, but no weights published. 2026 post: like/comment/share are separate task heads | CORRECTED: LinkedIn confirms multi-action weighted scoring exists, but not any 2x number | C for "2x"; A for "weighted combination, weights unpublished" (2020) |
| 23 | Golden hour (first 60 min decides reach) | C / contradicted | Post says embeddings refresh "within minutes" of publication or new engagement, and Help Center lists "How recent the content is" and "Engagement others have with your posts and how recent it is". No "golden hour" statement | CORRECTED: recency and near-real-time freshness are official; a 60-minute decision window is not | C for the window; A for "recency counts, signals refresh within minutes" |
| 24 | Post 2-5x/week | B | No LinkedIn statement on frequency found | NOT FOUND (primary) | B (unchanged) |
| 25 | Carousels/documents strongest; native video +69%; organic reach -50% YoY; AI-generic 47% less reach | B / C | Nothing on primary pages. The 2026 post says feed will favor "genuine insight, actionable ideas" regardless of format | NOT FOUND | unchanged (B/B/C/C); "47%" stays C |
| 26 | LinkedIn says low-quality content is tapered | not in notes | Help Center: algorithms "filter out or taper distribution of low-quality and unsafe content" | CONFIRMED (new item) | A |
| 27 | Feed ranking uses profile signals and your engagement history | not in notes | Engineering and Help Center quotes in 2a/2d | CONFIRMED (new item) | A |
| 28 | Topic authority / semantic relevance drives visibility (360Brew framing) | [Unverified] as policy | LinkedIn says system "better understands what a post is actually about"; LLM retrieval matches semantically related topics (SMR vs electrical engineering example) | CORRECTED: semantic topic understanding of posts is official; "topic authority" and any 360Brew label are not | A for semantic understanding; [Unverified] for authority/360Brew |
| 29 | Early-engagement strength (Creator Mode guidance) | [Unverified] | Nothing found | NOT FOUND | [Unverified] |
| 30 | Pre-2025 pods/first-comment-link/hashtag tricks are stale | inference | LinkedIn statement "designed purely to game distribution" fewer | Consistent but still an inference | inference |
| 31 | Newsroom says reducing "reach" is not the aim | not in notes | "This isn't about limiting reach or discouraging participation." | CONFIRMED (new item) | A |

## 4. Trade press (Search Engine Land, Social Media Today, PPC Land, ContentGrip)
Could not be read. Search Engine Land and PPC Land returned HTTP 403 with a Cloudflare "Just a moment..." challenge; socialmediatoday.com and contentgrip.com were refused at the agent proxy tunnel (403) even though they were listed as allowed. The Search Engine Land article cited in algorithm_claims.md (searchengineland.com/linkedin-updates-feed-algorithm-llm-ranking-retrieval-471708) remains a secondary pointer only. Nothing in trade press was needed to confirm the core claims because the LinkedIn primary pages were readable. Any claim that only trade press or blogs support (AI-slop report option, Jurka quotes, link penalties) stays at its old level.

## 5. Suggested replacement text for the evidence column
- Rows 1, 2, 6, 10, 12, 13, 26, 27, 31: A (primary read, with URL above).
- Rows 3-5: A (arXiv abstracts read).
- Rows 9, 16, 18, 22, 23, 28: keep the official part at A, mark the numeric or causal part C or [Unverified].
- Rows 7, 11, 14, 15, 17, 19, 20, 21, 24, 25, 29: no primary support found; keep prior level.

## 6. Summary
Confirmed on primary pages (A): LLM-based retrieval plus Generative Recommender sequential ranking (12 Mar 2026, both engineering and newsroom posts); the arXiv Feed SR, causal-LM retrieval and LiGR papers; action against engagement pods, comment automation and unauthorized third-party tools; reduction of generic, recycled, low-substance posts and engagement bait ("comment to agree", mismatched videos); dwell/long-dwell as a modeled signal (2020 and 2026); recency, tags, time viewing and tapered distribution of low-quality content as listed signals; weighted combination of action predictions (2020).

Corrected: the newsroom post does not mention AI at all, so "LinkedIn penalizes AI-generated content" is unsupported (the target is generic or engagement-bait content); the post is not authored by Tim Jurka and does not say pods are "not allowed" (it says LinkedIn takes action); hashtags are not addressed, only "tagged people, companies, or topics" as a signal; "golden hour" is replaced by "freshness within minutes plus recency signals", with no 60-minute rule; "comments count 2x" is unsupported, only the weighted-multi-action design is confirmed; arXiv 2510.14223 covers suggested-content retrieval only.

Still unverified: "Seems like AI slop" report option; 360Brew as the feed model; any link penalty (any size) and first-comment workaround; hashtag count or reach effects; edit and tag reach effects; posting frequency, early-engagement window, dwell thresholds in seconds; Tim Jurka statements. Datasets (Buffer, MagicPost, Van der Blom) were not re-checked.

Hosts that blocked: www.linkedin.com/pulse (403 Cloudflare challenge); searchengineland.com (403 challenge); ppc.land (403 challenge); socialmediatoday.com and www.socialmediatoday.com (proxy CONNECT 403); contentgrip.com and www.contentgrip.com (proxy CONNECT 403). Readable: news.linkedin.com, www.linkedin.com blog/engineering and help pages, arxiv.org.
