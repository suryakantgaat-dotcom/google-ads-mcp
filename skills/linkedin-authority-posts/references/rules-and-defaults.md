# Rules and defaults, with evidence levels

Source: the research report "LinkedIn thought leadership best practices" (revised 2026-11-20) and its `verify_*.md` notes, kept in the source repo under `reports/` and `research_notes/` (not bundled in an installed copy).

Levels: **A** stated by LinkedIn or in a paper, primary page read. **B** large third-party dataset, usually vendor-run. **C** practitioner opinion, small test, or loose support. **I** inference. **[Unverified]** no traceable source.

Every B, C and I item is a default to test, not a fact about how LinkedIn works. Vendor datasets disagree with each other, and several vendors sell scheduling or analytics tools.

## Contents

- Content rules (R1 to R5)
- Format and length defaults (R6, R7)
- Hooks, CTAs, links (R8, R9, R12)
- Cadence, timing, commenting (R10, R10a, R11)
- Measurement (R13)
- Claims to keep out of posts and advice
- Open gaps

## Content rules

| # | Rule | Level | Source |
|---|---|---|---|
| R1 | Base every post on a real account, test or judgment the user supplies. Never supply numbers. Ask for missing baseline, spend band, duration, result. Fixing style tells does not fix a post that lacks substance. | A (LinkedIn targets low-substance, generic posts) + C (no invented numbers) + A (Wikipedia warning that fixing signs alone can make detection harder) | [LinkedIn News](https://news.linkedin.com/2026/ImprovingTheFeed); [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) |
| R2 | Experiment post: hypothesis, setup, metric and baseline, result with significance caveat, what you would change. Publish null results. | I, from C sources not read | [SEL](https://searchengineland.com/ppc-experimentation-vs-ppc-testing-448771) |
| R3 | Frame around a specific buyer problem (for example lead quality versus volume), not generic tips. | B (Edelman survey, not read) + A (LinkedIn reduces generic posts) | [Edelman 2025](https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report) |
| R4 | One narrow position. Contrarian only with evidence. State when you would change your mind. | C | [Animalz](https://www.animalz.co/blog/thought-leadership-content/) |
| R5 | Client data needs written permission. Otherwise anonymise, index metrics (percent change), or use own accounts, test accounts or public assets. Do not imply atypical results are typical. | C + legal sources outside the verification pass | [Peshev](https://mariopeshev.com/answers/case-studies-digital-agencies/); [Morgan Lewis](https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials) |

## Format and length defaults

| # | Default | Level | Notes |
|---|---|---|---|
| R6 | Text posts about 1,200 to 1,500 characters, not under 400. Put the point of the hook inside the first ~140 characters. The post limit is 3,000. | B + I | AuthoredUp (372,126 personal-profile posts): 1,301 to 2,500 characters had a 27% higher median engagement than under 400. Compared with each author's own usual reach, differences shrink to "a few percent". The fold (~210 desktop, ~140 mobile) is observed by AuthoredUp, not specified by LinkedIn. [AuthoredUp](https://authoredup.com/blog/linkedin-character-limit) |
| R7 | Put frameworks, checklists and teardowns in a document (PDF carousel). Do not make polls the core. Treat video as a test. | B | Documents lead on Socialinsider (company pages, 7.00% in 2025), AuthoredUp (personal profiles, 1.39x reach / 1.30x engagement) and Buffer. Polls: AuthoredUp 1.78x reach but 0.37x engagement. Video: mixed, reach down about 36% year on year on two datasets. Socialinsider is company-page data and may not transfer to a personal profile (I). |

## Hooks, CTAs, links

| # | Default | Level | Notes |
|---|---|---|---|
| R8 | Hook with a specific number or stake, a story, or an evidence-backed contrarian claim. No CTA in line one. No question-only hook. | B/C, conflicting, not re-read | Hook rankings differ across sources (story, contrarian and curiosity-gap lead; questions rank low). Treat as hypotheses. |
| R9 | CTA: one specific question tied to the post's claim, or none. No "comment to agree", reaction-asking or chain-letter requests. Route leads through the profile or DM. | A + I | LinkedIn names "comment to agree" prompts as reduced content. The spam policy covers reaction polls and like/reaction/share requests. [Help Center](https://www.linkedin.com/help/linkedin/answer/a1338787) |
| R12 | Links: link posts show the lowest median engagement in Buffer and Socialinsider data. LinkedIn states no link penalty and no first-comment rule. Test one thing at a time (body link versus profile or DM routing). Do not cite a penalty size. | B (direction, correlational) / C (size) | The 60% and 18.8% penalty figures have no LinkedIn source. First-comment evidence is mixed. |

## Cadence, timing, commenting

| # | Default | Level | Notes |
|---|---|---|---|
| R10 | About 3 posts a week, test 4 to 5. Do not recommend 11+ as a default. | B, conflicting, observational + I | Buffer (2M+ posts) shows gains rising with frequency relative to 1 post a week, with diminishing returns. AuthoredUp (personal profiles) peaks at 4 to 5 a week and falls above 7. Metricool sees about 3 a week for personal profiles. |
| R10a | Posting time has no consensus. Test two or three slots against the user's own analytics. | B, sources disagree | Buffer 3 to 8 pm; Sprout midday; Metricool about 10 to 11 am; Hootsuite early morning (internally inconsistent). |
| R11 | Reply to substantive comments promptly. Comment on target accounts' posts yourself, with a specific addition. No pods, automation or third-party comment tools. | A (pods, automation, third-party tools targeted) + C (reply timing) | The "67% more engagement for first-hour replies" figure is from an unreviewed 50,000-post analysis on DEV. Other first-hour figures are [Unverified]. |

## Measurement

| # | Default | Level |
|---|---|---|
| R13 | Track profile views per impression, follower growth among target titles, inbound DMs and meetings, saves, and the quality of comments from target accounts. Use `measurement-log.md`. | I |

## Claims to keep out of posts and advice

Do not state these as fact: "golden hour", exactly 3 hashtags, comments count 2x, 360Brew runs the feed, editing resets reach, a 60% link penalty, "LinkedIn penalizes AI-written content", "45% less engagement for AI posts", "54% of posts are AI", "73% of executives trust thought leadership more". All are C or [Unverified]. The Edelman figures (79%, 56% versus 14%, 84%, 59%) were not read on a primary page, so quote them only with "reportedly" and the source.

## Open gaps

- No source studied hiring managers, so advice for that audience rests on inference (I).
- No verified named performance-marketing creators or post data.
- No structure-level data comparing case study, teardown, contrarian and framework posts.
- Edelman statistics, Fast Company, Search Engine Land, Van der Blom and Taplio were blocked or not obtained.
- No official Google Ads or Meta policy on publishing case studies was found.
- No controlled tests of CTA style, comment timing or first-comment links.
- "Here's the thing", one-line paragraph ladders and fake-vulnerability stories are not documented as AI tells anywhere.
