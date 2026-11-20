# Anti-slop check

Run this on every draft before delivering it.

## What the evidence supports

- Wikipedia's "Signs of AI writing" is a descriptive advice page for detecting undisclosed AI text. It says no single sign proves AI authorship and warns: "do not merely treat these signs as the problems to be fixed; that could just make detection harder." So a list of tells is a diagnostic. Scrubbing tells from a post with nothing specific in it does not make it good.
- LinkedIn's stated target is generic, recycled, repetitive, low-substance posts and engagement bait (level A). It has not stated that AI authorship itself is penalized.
- Structure is better supported than single words. Word lists date fast: "delve" peaked in 2023 to early 2024 and fell off in 2025 per Wikipedia.
- Research on disclosed AI authorship finds lower perceived trust and competence (arXiv 2510.24011, 261 participants; arXiv 2507.01418). These are analogies, not LinkedIn data.

## Procedure

1. Read the draft once for substance. Does every paragraph carry a number, a mechanism, a decision or a stated judgment from the user's input? Mark paragraphs that carry none. Fix these first, by asking the user for the missing specific or cutting the paragraph.
2. Scan for tell families below. Count distinct families per paragraph.
3. Rewrite any paragraph with two or more distinct families, and any item in the "Ban" list regardless of count. A single isolated tell from the "Limit" list can stay when it is the plainest way to say the thing.
4. Check for invented specifics: every number, date, name and quote must trace to the user's input. Move any that do not trace into "Claims to verify", or delete them.
5. Read the post aloud as the user would say it. Replace anything the user would not say.

## Tell families

| Family | Examples | Treatment | Source / level |
|---|---|---|---|
| Contrast reframe | "Not X, but Y"; "it's not X, it's Y"; "Y rather than X" | Ban unless a real contrast exists. Common in human writing too, only stereotypically an AI sign. | Wikipedia (C, read); Beutler Ink, Taplio (C, Taplio not read) |
| Triads | Three parallel items where two or one would do | Limit. Stronger tell where the flourish adds nothing. | Wikipedia (C, read) |
| Inflated significance | "stands as", "serves as", "is a testament", "pivotal", "evolving landscape", "marks a shift"; trailing "-ing" analysis ("highlighting the importance of") | Ban | Wikipedia (C, read) |
| Vocabulary clusters | delve, tapestry, underscore, crucial, landscape, robust, meticulous, showcase, valuable insights; later-era: leverage, multifaceted, prioritize | Flag as a cluster (three or more in a post), not as single words. Replace with the concrete thing. | Wikipedia (C, read); Kobak et al., Science Advances 2025 (A, read; biomedical abstracts only) |
| Vague attribution | "some critics argue", "experts argue", "industry reports", "studies show" with no study | Ban. Name the source or cut. | Wikipedia (C, read) |
| Formatting | Emoji at the start of headings or bullets; title-case headings; curly quotes; heavy bold; inline-header vertical lists | Ban emoji bullets. Sentence case. Straight quotes. Limit bold. | Wikipedia (C, read) |
| Closers and summaries | "In conclusion", "Overall", "Despite these challenges...", "It's important to note" | Ban. Wikipedia dates "important to note" to about 2023. | Wikipedia (C, read) |
| Chat leakage | "Certainly!", "I hope this helps", "let me know if" | Ban | Wikipedia (C, read) |
| Engagement bait | "Comment to agree", "Agree?", "Comment YES", "comment [keyword] and I'll send", requests for likes, reactions, shares, reaction polls | Ban. LinkedIn names "comment to agree" and the spam policy covers reaction requests. Keyword-comment funnels are blog-flagged only. | LinkedIn News, Help Center (A, read); Soloop (C) |
| Mismatched media | A video or image that does not match the text | Avoid | LinkedIn News (A, read) |
| Invented specifics | Any number, client, quote or result not in the user's input | Ban | C |
| Generic advice | A claim that offends no one; no committed judgment | Ban. Require a position the user holds and a condition under which they would drop it. | LinkedIn News (A, read) |
| Uniform rhythm | Sentences of near-equal length throughout | Vary deliberately. Short sentences are fine. | C (PR Daily) |

## Not tells by themselves

- Em dashes. Wikipedia now lists them as a historical sign (2022 to September 2026), useful only in combination with others. Use commas, colons or parentheses where they read better.
- Perfect grammar, and "bland" or "robotic" tone. Wikipedia lists these as ineffective indicators.

## Style risks with no source [Unverified as AI tells]

"Here's the thing", ladders of one-line paragraphs, fake-vulnerability openers, the hook-break-moral template. No source documents these as AI tells. They are common on LinkedIn and can read as formulaic, so flag them as style risk only and let the user decide. Do not tell the user these make a post "look like AI".

## Do not promise detection results

No technique has controlled evidence of raising LinkedIn performance or lowering reader suspicion of AI authorship. Do not tell the user a post "will pass" or "will not be flagged". Say what was checked and what remains uncertain.
