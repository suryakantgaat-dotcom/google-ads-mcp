# Verification of LinkedIn vendor statistics against primary pages

Checked 2026-11-20 by fetching primary pages with curl through the agent proxy (HTML stripped to text, read directly). Earlier notes (post_formats.md, cadence_hooks_comments.md) were not edited. Status key: MATCH / DIFFERS / ABSENT (not on the primary page) / [Unverified] (could not be checked).

Reach of fetches:
- OK (HTTP 200): buffer.com, sproutsocial.com, www.socialinsider.io (HTML pages), authoredup.com, blog.hootsuite.com, metricool.com.
- Blocked / not found: none returned 403 or a bot block. Socialinsider PDFs: linkedin_benchmarks_2025.pdf returned HTTP 404; linkedin_benchmarks_2026.pdf returned no response (curl code 000, connection failure). The HTML benchmark page was used instead. metricool.com/linkedin-study/ returned 404; the real study landing page is metricool.com/linkedin-trends-study/ (200), but the full study is behind a download form, so only the public sneak-peek and the stats/best-time pages were read.

---

## 1. Buffer: posting frequency (2M+ posts)

Page: https://buffer.com/resources/how-often-to-post-on-linkedin/ ("How Often Should You Post on LinkedIn in 2026? Data From 2 Million+ Posts"), author Tamilore Oladipo with data scientist Julian Winternheimer. Page date shows "Published Aug 28, 2025" (title says 2026; no later update date shown; earlier notes called it a "2026 edition", which the page date does not support).

Sample: "more than 2 million LinkedIn posts from 94,000+ accounts". Account type: not stated as pages or profiles; page says "accounts", "creators", "brands" and refers to personal-account experience of the authors. Covers all four formats combined (text, image, video, carousel/PDF), not split by format. Method: z-scores per account and fixed-effects regression; compares each account's weeks against its own baseline.

| Claim | Exact page figure | Earlier notes | Status |
|---|---|---|---|
| 2-5 posts/week | "+1,182 more impressions per post and a 0.23 percentage point lift in engagement rate compared to posting just once a week" | +1,182 impressions, +0.23 pp | MATCH figures; DIFFERS on baseline: page baseline is 1 post/week, notes said "vs fewer posts" |
| 6-10 posts/week | "+5,001 more impressions per post", "0.76 percentage point increase in engagement rate" | same | MATCH (baseline 1 post/week) |
| 11+ posts/week | "+16,946 impressions per post, +1.40 percentage points, 3x more engagements" (intro says "nearly triple the engagements per post compared to once-a-week posters") | same | MATCH (baseline 1 post/week) |
| Recommendations | 2-5/week sustainable growth; 6-10 accelerate; 11+ maximise "if you can maintain quality" | same | MATCH |
| Plateau | Page says "Posting more always helps, but the marginal payoff decreases as you climb higher"; gain from 6-10 to 11+ is smaller than the jump from 1 to 2-5. "Can you post too much? The short answer: no." | Notes said "no sign of a plateau up to 11+" | DIFFERS slightly: Buffer reports diminishing marginal gains, though no decline |
| Causal caveat | Page does not say "observational/correlation" in the text read; it says the controls (z-score, fixed effects) isolate the effect within accounts | Notes said observational/correlational caveat came from search summary | ABSENT as an explicit caveat on the page; the design is within-account observational, so the caveat is still a fair inference, not a Buffer statement |
| Account size | "Small accounts with a few hundred followers saw the same relative lift... as large accounts"; bigger accounts gain more in absolute numbers | not in notes | New detail |
| Format findings on same page | Median engagement vs text: images ~72% more, video 84% more, carousels "278% more engagement than videos, 303% more than images, and nearly 600% more than text posts"; link posts lowest | not in notes | New detail |

The notes' "LinkedIn's own marketing account recommends at least 2-3 posts per week (per Buffer)" was not found on this page: ABSENT. [Unverified]

## 2. Buffer: best time to post

Page: https://buffer.com/resources/best-time-to-post-on-linkedin/ ("The Best Time to Post on LinkedIn in 2026: 4.8 Million Posts Analyzed"), Kirsti Lang, Published Sep 9, 2026. Sample: "over 4.8 million posts sent through Buffer"; page says it applies whether growing "a LinkedIn Page for a brand or your own personal brand" (mixed or unspecified; not split). Times normalised to local time zone.

Exact figures: best window 3 p.m.-8 p.m. on weekdays; top slots Wednesday 4 p.m., Friday 3 p.m., Friday 4 p.m.; best day Wednesday, then Thursday, then Friday; Monday and Tuesday lowest; mornings (6-11 a.m.) now weaker; "In 2025, peak engagement was almost entirely confined to working hours". Per-day top-3: Mon 10pm/5pm/9pm; Tue 4pm/5pm/10pm; Wed 4pm/3pm/5pm; Thu 5pm/7pm/9pm; Fri 3pm/4pm/5pm.

Earlier notes: no Buffer time-of-day data (listed as a gap). Status: ABSENT from notes; this is a new and materially different finding (late afternoon/evening, not late morning). It contradicts Sprout's midday windows (below) and the notes' "sources agree on Tuesday-Thursday late morning to early afternoon" takeaway: DIFFERS. The page states the engagement metric and warns audiences differ; no engagement-rate figures per slot given in text (heatmap image).

Related earlier Buffer 2025 study referenced on the frequency page: "The Best Time to Post on LinkedIn: 1 Million Posts Analyzed" (not fetched).

Same page, format: "carousel (document) posts generate up to 596% more engagement than text-only posts" (consistent with the frequency page's "nearly 600%").

## 3. Buffer: 58-post experiment

Page: https://buffer.com/resources/linkedin-experiment/, author Jena Dunay (guest, business owner), Published May 20, 2024. Figures: 60 days, 58 posts, 568,000 impressions; text posts 5,000-10,000 impressions typically, top 20,000+; polls ~15,000 impressions, one poll with 300 participants got 21 comments and 10 messages; carousels "consistent at getting me 5,000+ impressions". n=1 personal account. MATCH with notes (notes only gave 58/60/568k). Note the notes cited a hook finding to this page; the page does list three hook types (numbers/data, strong opinion, direct call-out) but no hook statistics.

## 4. Sprout Social: best times

Page: https://sproutsocial.com/insights/best-times-to-post-on-linkedin/, "[Updated March 2026]", Published on March 31, 2026, author Mary Keutelian.

Sample: "nearly 2 billion engagements across 307,000 social profiles across Facebook, Instagram, LinkedIn, Pinterest, TikTok and X (Twitter) between November 27, 2025 and February 27, 2026". This is the cross-network sample, not LinkedIn-only; no LinkedIn-specific count and no page-vs-profile split is given (Sprout's customers are largely brands, an inference).

Exact figures: Monday 1-2 p.m.; Tuesday 11 a.m.-5 p.m.; Wednesday 11 a.m.-4 p.m.; Thursday 11 a.m. and 1-5 p.m.; Friday 11 a.m. and 1-2 p.m.; Saturday and Sunday "avoid posting". Page text: "The best time to post on LinkedIn is Tuesdays from 11 a.m.-5 p.m." Technology & Software industry: Tuesdays and Wednesdays 10 a.m.-4 p.m. (on this page; the notes cited a separate "linkedin-tech" page that was not fetched).

Earlier notes: Tuesday 11am-5pm, Wednesday 11am-4pm, Thursday 1-5pm, weekends worst, updated March 2026. MATCH, with additions (Thursday also 11 a.m.; Monday and Friday windows exist). The notes' "Tuesday strongest" is consistent with the page headline. Notes' Oct 2025 edition and Shopify's "34,000+ profiles" claim: [Unverified] (not fetched).

## 5. Socialinsider: LinkedIn benchmarks

Page: https://www.socialinsider.io/social-media-benchmarks/linkedin ("LinkedIn Organic Benchmarks 2026"), author Elena Cucu, dated Mar 16, 2026, with later quarterly updates inside (Q2 and Q3 2026 figures appear, so the date line understates when it was last edited). PDFs not retrievable (see top).

Sample and account type: company pages only. Methodology section: "2,450,610 LinkedIn posts coming from brands between 1K-1M followers... January 2025-December 2026 [sic]", organic posts only, five size buckets summing to roughly 26,100 pages. Several figures on the page state "2.45 million posts from 26,000 LinkedIn company pages". DIFFERS from the notes, which gave "1.3M posts, 16,645 pages, Jan 2024-Dec 2025 per a third-party summary". The page's own intro still says "Based on the analysis of 1.3M LinkedIn business posts" (internal inconsistency on the primary page). A note on the page says "2025 values, presented as 2026".

Engagement rate by impressions (reactions + comments + shares divided by impressions), 2024 vs 2025 table:
Native document 6.10% -> 7.00%; multi-image 6.60% -> 6.45%; video 5.60% -> 6.00%; image 4.85% -> 5.30%; text 4.00% -> 4.50%; poll 4.40% -> 4.20%; link 3.30% -> 3.25%. Overall 2025 average 5.20%.
Quarterly update on the same page: Q3 2026 native documents and multi-image both 6.40%; video 5.25%; image 4.70%; text 3.50%; poll 3.60% (from 4.50% in Q2 2026); link 2.50% (from 3.40% in Q2). Multi-image Q2 2026 6.60%.

Status vs notes: documents 7.00% (up from 6.10%), multi-image 6.45% (down from 6.60%), text 4.50%, overall 5.20% = MATCH. Notes' 2025-report figures (multi-image 6.60%, document 6.10%, video 5.60% for 2024 data) = MATCH (the 2024 column). Notes' "document 5.85% in the 2025 report" = [Unverified] (PDF 404). New: Q3 2026 figures show documents and multi-image tied at 6.40% and text down to 3.50%, which the notes lack.

Posting frequency (company pages, average posts per page per month, 2024 -> 2025): native document 1 -> 2; multi-image 1 -> 1; video 2 -> 4; image 5 -> 7; text 1 -> 1; poll 1 -> 1; link 4 -> 4. Notes said "video and native document posting roughly doubled, image 5 to 7, text/poll/link flat": MATCH on image/video/document/text/poll, but link is 4 per month (flat), consistent. The notes' "Apaya claims a peak near 2 posts/week" stays [Unverified]; the Socialinsider page gives per-format monthly counts only, no posts-per-week figure.

Other: video views down 36% YoY (155-1,380 views per video by page size); polls top impressions only above 50K followers (up to 9,797 per post); multi-image tops impressions for 5K-50K pages (up to 1,850 per post). Follower growth 6.4% (100K-1M) to 31.0% (5K-10K) in 2025.

## 6. AuthoredUp: format study

Page: https://authoredup.com/blog/best-performing-content-on-linkedin ("Best Performing Content on LinkedIn in 2026 (Big data analysis)"), Ivana Todorovic, Published Jul 28, 2025, Updated Nov 5, 2026. Personal profiles only.

Exact: "over 3 million LinkedIn posts from March 2025 through February 2026"; multipliers are relative to each profile's own median. Reach / engagement multipliers: document 1.39x / 1.30x (4.88% of posts); image 1.20x / 1.33x (57.16%); poll 1.78x / 0.37x (1.16%, "reach trap"); text-only 1.07x / 0.78x (11.59%); video 0.86x / 0.93x (10.61%); article 0.69x / 0.44x (6.00%); reshare 0.29x / 0.22x. Video reach down 36% YoY (all profiles), 34% top performers. Video duration sub-study: 36,946 video posts, Oct 2025-Mar 2026; 3 minutes+ is 1.21x reach, 0-30 s 0.96x. Documents are 12.92% of saved posts (about 2.6x share of content). Text 20+ sentences 1.14x reach; under 5 sentences 0.64x.

Posting frequency (same page, personal profiles): 1 post/week 79.80% of profiles, median engagement 2.40%, 679 impressions; 2-3/week 2.58%, 741; 4-5/week 2.60%, 870 (28% more impressions than weekly; "sweet spot"); 6-7/week 1.61% of profiles, 2.54%, 959 impressions; 8+/week 0.97% of profiles, 1.79%, 586. Page says above 7/week both metrics drop sharply. This is directly at odds with Buffer's "11+ is best" and is not in the earlier notes.

Status vs notes: the notes' "AuthoredUp 2025 analysis of 621,833 posts; poll 1.64x; video 1.14x to 1.10x" = DIFFERS / not found on the current page (page now says 3M+ posts, poll 1.78x, video 0.86x); the earlier numbers may come from an older edition of the page. [Unverified] for the 621,833 figure. Notes' "later AuthoredUp piece: poll reach down 28%" = not found; [Unverified] (the only "28%" on the page is a caption-length and a frequency statistic). Notes' unattributed "3M-post study: document/carousel 39% more reach and 30% more engagement" (via Contentin) = CONFIRMED as AuthoredUp (1.39x / 1.30x, personal profiles). Notes' "document/carousel best content type" = MATCH. Notes' "Polls ... LigoSocial -50%" and Metricool poll claims remain different datasets.

## 7. AuthoredUp: post length (372,126 posts)

Page: https://authoredup.com/blog/linkedin-character-limit, Published Apr 2, 2026, Updated Nov 5, 2026. Personal profiles, Sep 2025-Feb 2026, posts with at least 1 impression, 372,126 posts.

Exact: "Posts between 1,301 and 2,500 characters generate 27% higher engagement than posts under 400 characters". Table of median engagement rate: 1-400 chars 2.10% (17.3% of posts, median 575 impressions); 401-700 2.24%; 701-1,000 2.31%; 1,001-1,300 2.44%; 1,301-2,000 2.61% (23.1%); 2,001-2,500 2.67% (6.8%); 2,501-3,000 2.62%. Caveat on the page: these are medians across everyone and long posts lean toward bigger accounts; comparing each post with its own author's usual reach (709,195 personal-profile posts, Jul 2025-Jun 2026), differences between lengths shrink to "a few percent"; text-only posts under 400 characters stay last (about 14% below the author's usual reach); text posts do best around 1,200-1,500 characters.

Fold: "~210 characters on desktop (or ~140 on mobile)"; limit 3,000; headline 220; comment 1,250 (starred in the table); poll options 30. Status: figures MATCH the notes (27%, 1,301-2,500, 372,126, personal profiles, Sep 2025-Feb 2026, fold, limits). CORRECTION to add: the 27% lift is a raw median comparison that shrinks to a few percent after controlling for the author; the notes did not carry that caveat. The fold remains AuthoredUp's own observed number, not a LinkedIn spec.

## 8. Hootsuite

Page: https://blog.hootsuite.com/best-time-to-post-on-linkedin/ ("The best time to post on LinkedIn [2025 data]"), dated November 19, 2025. Sample: "over 1 million social posts" with Critical Truth, times localised across 118 countries; account type not stated; the "1 million" appears to be across social platforms rather than LinkedIn only (wording: "1 million social posts").

Exact figures, and an internal inconsistency on the page: key takeaway says "8-9 AM on Tuesdays and Wednesdays"; the section text says "early morning (4 AM-6 AM) on Tuesdays and Wednesdays". By day: Mon 11 AM; Tue 6-8 AM; Wed 9 AM; Thu 2 PM; Fri 8 PM; Sat 4-5 AM; Sun 6 AM. Industries: tech, education, healthcare mornings; finance, construction, hospitality afternoons/evenings. Notes: Hootsuite time data was not retrieved, and the notes cited only a Hootsuite comment-length article (not fetched; the first-30-minutes "4x" LinkHub and 14 vs 6 replies claims remain [Unverified]). New: Hootsuite's early-morning result conflicts with both Sprout (midday) and Buffer (3-8 p.m.).

## 9. Metricool

Pages read: https://metricool.com/linkedin-statistics/ (2026 stats), https://metricool.com/linkedin-trends-study/ (study landing page, dated 14 April 2026, author Blanca Ruiz), https://metricool.com/best-time-to-post-on-linkedin/ (dated 15 May 2026). Full study is gated behind a form.

Sample: "673,658 posts from 63,108 LinkedIn accounts", company pages and personal profiles analysed separately (the best-time page also mentions 40,000 accounts / 490,000 posts per month for its premium feature). Public figures: carousels get "17x more interactions than images, yet images are still posted 6x more"; posts with a question get "77% more comments"; "nearly 40% of all interactions in a post happen on day one"; 6.89% of company pages grew; personal profile engagement 2.60% vs company pages 1.74%, "personal profiles received 63% higher engagement than company pages" (the best-time page; note the page's own numbers 2.60 vs 1.74 imply about 49%, another small internal inconsistency); personal profiles post 3.05 times/week vs company pages 2.74 (overall 2.34, down from 2.60); engagement for company pages rose in 2025 with lower posting frequency; Metricool concludes "less is more" for small brands. Best times (its own accounts): Mon 10am-12pm, Tue 11am, Wed ~11am, Thu 9am-12pm, Fri 10am, Sat/Sun 10am.

Earlier notes cited a 2025 Metricool study (carousel engagement ~46% above other formats; poll reach +206%; via a Social Media Today press release, Apr 2025). Neither figure appears on the 2026 pages: ABSENT / [Unverified] (the 2025 study may be superseded). The 2026 study's "17x" carousel figure is a different statistic and contradicts the "46%" framing. Metricool's company-page frequency of ~2.7/week and personal ~3/week is a useful descriptive benchmark and conflicts in spirit with Buffer's "more is better".

---

## Summary of earlier claims

Confirmed (match primary page):
- Buffer frequency tier figures (+1,182 / +5,001 / +16,946 impressions per post; +0.23 / +0.76 / +1.40 pp; 3x engagements; 2M+ posts, 94,000+ accounts; 2-5, 6-10, 11+ recommendations).
- Sprout Social March 2026 windows (Tue 11am-5pm, Wed 11am-4pm, Thu 1-5pm, weekends worst).
- Socialinsider format engagement rates (documents 7.00%, multi-image 6.45%, text 4.50%, overall 5.20%; 2024 figures 6.10/6.60/5.60) and monthly posting frequency by format.
- AuthoredUp length study (372,126 personal-profile posts, 1,301-2,500 characters, +27% vs under 400; fold ~210 desktop, ~140 mobile; 3,000 limit).
- AuthoredUp's "39% more reach, 30% more engagement" for documents (the previously unattributed "3M-post study" is AuthoredUp).
- Buffer 58-post experiment details.

Corrected or qualified:
- Buffer frequency lifts are relative to 1 post/week, not "fewer posts"; the page is dated Aug 28, 2025 (not a 2026 edition); gains show diminishing marginal returns rather than "no plateau"; no explicit observational caveat on the page.
- Socialinsider sample is 2,450,610 posts from about 26,000 company pages (methodology), not 1.3M / 16,645 pages (the 1.3M appears only in the page intro); page now includes Q3 2026 figures (documents and multi-image 6.40%, text 3.50%).
- AuthoredUp format study is now 3M+ posts (Mar 2025-Feb 2026); poll multiplier is 1.78x reach but 0.37x engagement; video is 0.86x reach and down 36% YoY. The notes' 621,833 posts / 1.64x / 1.14x to 1.10x do not appear.
- AuthoredUp 27% length lift shrinks to a few percent when compared within-author (page's own caveat).
- Notes' conclusion that sources agree on late-morning to early-afternoon timing is wrong: Buffer (4.8M posts, Sep 2026) says 3-8 p.m., Wednesday best, Monday/Tuesday worst; Hootsuite (Nov 2025) says early morning; Metricool says ~10-11 am; Sprout says midday.
- New frequency counterpoint: AuthoredUp personal-profile data peaks at 4-5 posts/week and declines above 7; Metricool reports about 3/week for personal profiles and "less is more".

Still [Unverified] (not found on pages reached, or not fetched):
- Socialinsider "5.85%" document figure in the 2025 PDF (PDF 404); 2026 PDF unreachable.
- Metricool 2025 study figures (+46% carousel, +206% poll reach).
- AuthoredUp "poll reach down 28%" and the 621,833-post analysis.
- Buffer attribution of "LinkedIn recommends 2-3 posts/week".
- Sprout October 2025 edition, Sprout tech sub-page, Shopify "34,000+ profiles".
- Hootsuite long-vs-short comments article, LinkHub 4x claim, AuthoredUp hook-type medians (story 2.60%, contrarian 2.31%, question 2.16%), AuthoredUp "~1M posts reply 2.4x" (pages not fetched).
- Van der Blom, Taplio, Magnettu, LigoSocial, Ordinal, LinkedIn-published items (hosts not on the allowlist, not attempted).

Hosts that blocked: none returned 403 or a bot-protection page. Only failures were Socialinsider PDF paths (404 for 2025, no response for 2026) and one wrong Metricool URL (404, corrected to /linkedin-trends-study/). Metricool's full study is gated behind a form, so not read.
