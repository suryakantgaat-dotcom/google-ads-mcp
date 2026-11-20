# Verification of AI-slop and thought-leadership claims against primary pages

Date checked: 2026-11-20. Method: curl through the agent proxy (`-A "Mozilla/5.0"`), HTML stripped with python3 -I. Checks ai_slop_tells.md and original_value.md. Those files were not edited.

Status labels: CONFIRMED, CORRECTED, CONTRADICTED, [Unverified] (no primary page reachable).

## Host access log

| Host | Result |
|---|---|
| en.wikipedia.org | API `action=parse` returned HTTP 429 (rate limit). `index.php?title=Wikipedia:Signs_of_AI_writing&action=raw` returned 200 (183 KB wikitext, revision showing edits to Nov 2026). Used that. |
| arxiv.org | 200 on abs/ and html/ pages for 2406.07016 (v4, v5), 2510.24011, 2507.01418. |
| originality.ai | 200. The LinkedIn study page has since been rewritten (see section 3). |
| www.edelman.com | 403 "Access Denied" (Akamai) on home page, the 2025 report URL and the 2026 report URL. Not bypassed. |
| ppc.land | 403 Cloudflare "Just a moment..." challenge on every URL tried. Not bypassed. |
| searchengineland.com | 403 Cloudflare challenge. Not bypassed. |
| www.fastcompany.com | 403 DataDome captcha page. Not bypassed. |
| www.contentgrip.com / contentgrip.com | Proxy refused the CONNECT tunnel (curl 56, "CONNECT tunnel failed, response 403", HTTP 000). Host appears not to be allowed by the proxy despite the stated allowlist. |

Because Edelman and every trade-press host named for Edelman coverage (ContentGrip, PPC Land) were blocked, section 5 has no primary or trade-press confirmation. No other fetched page quoted the Edelman figures.

## 1. Wikipedia "Signs of AI writing"

URL: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (read as raw wikitext, revision current on 2026-11-20; the page cites edits through November 2026).

### Page status and caveats (CONFIRMED, with refinement)
- Page type: WikiProject advice page (`{{WikiProject advice|wikiproject=WikiProject AI Cleanup}}`). Earlier note said "advice page from WikiProject AI Cleanup, not policy": CONFIRMED.
- Quote: "this list is descriptive, not prescriptive; it consists of observations, not rules."
- Quote: "Not all text featuring these indicators is AI-generated, as the large language models that power AI chatbots are trained on human writing, including Wikipedia. Many elements of AI writing can be found in editorials, blogs, or fan fiction."
- Quote: "Please do not merely treat these signs as the problems to be fixed; that could just make detection harder." Earlier note's "fixing surface signs makes detection harder": CONFIRMED.
- Scope limit: "it is a field guide to help detect undisclosed AI-generated content on Wikipedia: while some of the signs may be broadly applicable, some may not apply in a non-Wikipedia context." Footnote: guide "is less useful for texts which are not informational writing." This supports the earlier inference that it is a weak LinkedIn filter.
- Detectors and humans: "Do not solely rely on AI content detection tools (such as GPTZero and Pangram)... these tools have non-trivial error rates." Also: "Humans are notoriously bad at distinguishing human and LLM-generated text" (cites a 2025 study finding human ability no better than random chance; a 2025 preprint where 'expert' annotators correctly identified 90% of AI text).
- Strongest-tell statement on vocabulary: "an edit (post-2022) introducing lots of them, lots of times, is one of the strongest tells for AI use." Single words are weak.

### "High density of AI vocabulary words" box (exact list)
"Words to watch: Additionally (especially beginning a sentence), align with, boasts (meaning "has"), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as a verb), interplay, intricate/intricacies, landscape (as an abstract noun), meticulous/meticulously, pivotal, robust, showcase, tapestry (as an abstract noun), testament, underscore (as a verb), valuable, vibrant"

Earlier note listed "tapestry, testament, underscore, pivotal, plus crucial, delve, enhance, landscape": CONFIRMED but incomplete.

Era breakdown (quoted):
- "2023 to mid-2024 (GPT-4): Additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant"
- "Mid-2024 to mid-2025 (GPT-4o): align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant"
- "Mid-2025 to mid-2026 (GPT-5): emphasizing, enhance, highlighting, showcasing (plus words associated with 'Canned emphasis on notability, attribution, and media coverage')"
- "Mid-2026 and on (GPT-6): challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally (with much more period and comma usage and shorter sentences around a strict 8-20 word limit)"
- On delve: "the word delve was famously overused by ChatGPT in 2023 and early 2024, but became less frequent later in 2024, then dropped off sharply in 2025."
- Grok: "overuses superficially 'scientific' words like causal, empirical, correlate, and continues to overuse underscore as of 2026."
- Context caution: "a word being overused by AI does not imply that its synonyms are also overused."

Earlier note says delve, pivotal and underscore tie to 2023 to mid-2024 (GPT-4): CONFIRMED (but pivotal and underscore also appear in the GPT-4o list). "Grok overused underscore as of 2026": CONFIRMED on the Wikipedia page itself (the note had cited a mirror).

New finding: the page itself now notes a 2026 era (GPT-6) with different words (leverage, multifaceted, prioritize, etc.). The earlier note mentioned later lists only vaguely. Any fixed banned-word list dates fast: CONFIRMED by the page.

### Structures (exact "Words to watch" and descriptions)
- Undue emphasis on significance, legacy, broader trends: "stands/serves as, is a testament/reminder, a crucial/pivotal/vital/significant/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, distinction [matters/is important] because". Text: "LLM writing often puffs up the importance of the subject matter by adding statements about how arbitrary aspects of the topic represent or contribute to a broader topic." Also: "LLMs may include these statements for even the most mundane of subjects like etymology or population data." Earlier note: CONFIRMED. The phrase "stands as a testament to" is not verbatim; the page lists "stands/serves as" and "is a testament/reminder".
- Claims a topic has influenced discussions: "has/have shaped conversations/discussions/debate about".
- Undue emphasis on notability, attribution and media coverage: "independent coverage, local/regional/national/[country] media outlets, music/business/tech outlets, trade publications, cited/featured/profiled in".
- Undue emphasis on online presence: "maintains an active / a strong digital presence, social media presence". Quote: "particularly idiosyncratic to AI text and relatively uncommon on Wikipedia before ~2024." This is the closest LinkedIn-adjacent item.
- Superficial analyses: "highlighting/underscoring/emphasizing ..., ensuring ..., reflecting/symbolizing ..., contributing to ..., cultivating/fostering ..., encompassing ..., enhancing ..., valuable insights, align/resonate with". Mechanism: "attaching a present participle ('-ing') phrase at the end of sentences".
- Vague expression of connection: "in connection with/to, connected with/to, in association with, associated with".
- Vague attributions: "Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when only few sources are cited), such as (before exhaustive word lists)". Text: "AI chatbots tend to attribute opinions or claims to some vague authority—a practice called weasel wording." Earlier note ("some critics argue"): CONFIRMED.
- Outline-like conclusions: "Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook".
- Avoidance of basic copulatives: "serves as/stands as/marks/functions as/operates as/represents [a], boasts/features/maintains/offers [a], refers to". Text cites an over-10% decline in "is/are" in one study.
- Negative parallelisms. Page text: "While it is common among human writers (especially in 'common misconceptions' or 'myths busted' listicles), it is stereotypically an 'AI sign'." Three subforms:
  - "Not only ... but ..." / "It is not just ..., it's ..."
  - "It's not ..., it's ..." / "no ..., no ..., just ..."
  - "Y rather than X": "a construction particularly common in recent LLM output."
  Earlier note's "not X, but Y": CONFIRMED. The earlier note said it is "rare in natural speech"; the page instead says it is common among human writers in some genres, so that wording is CORRECTED (flagged as a stereotype sign, not rare in human text).
- Rule of three: "LLMs overuse the rule of three... from 'adjective, adjective, adjective' to 'short phrase, short phrase, and short phrase'. LLMs often use this structure to make superficial analyses appear more comprehensive." And "This sign is stronger when it appears in contexts where most people would not bother to include such stylistic flourishes". The earlier quote "the rule of three is fine; the rule of three in every sentence is not" is from a blog (Blake Stockton), not the page: it does not appear on the Wikipedia page. [Unverified as a Wikipedia statement.]
- Section summaries (historical): "In summary, In conclusion, Overall". "older LLMs often added sections titled 'Conclusion'... this sign is still observed after 2024, just much less."
- Didactic disclaimers, 2023-2024 era: "Older LLMs (~2023) often added didactic disclaimers about topics being 'important to note'." So "It's important to note" is listed as an older-era tell (the earlier note's secondary reading: CONFIRMED but dated; it is not a current top tell).
- Hedging disclaimers (mid-2026): "While specific details are limited/scarce..., not widely available/documented/disclosed, ...in the provided/available sources / search results..., based on available information, ...does not by itself establish...".
- Promotional language (historical, 2023-2025): "boasts a, vibrant, rich, profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array".
- Chat leakage: "Of course!, Certainly!, You're absolutely right!, I hope this helps, Would you like..., let me know, here is a...".

### Style section (exact)
"Using title case instead of sentence case in section titles. Overuse of boldface in prose, sometimes misusing asterisks in an attempt to do so. Frequently presenting information in inline-header vertical lists. Using the incorrect heading levels... Affixing emoji at the beginning of section titles or list entries. Using curly quotation marks and apostrophes instead of straight ones."
Earlier note (title-case headings, curly quotes, emoji on headings or list items): CONFIRMED. Added: overuse of boldface and inline-header vertical lists.

### Em dashes: CORRECTED in emphasis
Section "Overuse of em dashes (2022-September 2026)" now sits under "Historical indicators". Quotes:
- "LLM output is much more disposed to use them than nonprofessional human-written text of the same genre, and uses them in places where humans are more likely to use commas, parentheses, colons, or (misused) hyphens."
- "This sign is most useful when taken in combination with other indicators, not by itself."
- "A July 2026 study found that of contemporary models only Claude used em dashes more than professional writers, and ChatGPT used them less."
- "those same latest AI models of late (September 2026 and onward) have more and more often been found to be hard coded to not use em dashes at all... commas and periods are more likely now than even human text" (this clause carries a {{cn}} citation-needed tag).
So the earlier note's "secondary sources conflict" is resolved: Wikipedia now treats em dashes as a dated sign (2022 to Sept 2026), still usable in combination with others. Recommendation: do not treat an em dash as a strong tell in late 2026.

### Ineffective indicators (new, relevant to LinkedIn editing advice)
Page lists as ineffective: "Perfect grammar", mixed casual/formal register, "bland" or "robotic" prose, "fancy" or "formal" prose, transition words in isolation, unsourced content. Matches the earlier "edit patterns, not single words" advice.

### LinkedIn-style patterns on the page?
- Not mentioned: the page contains no mention of LinkedIn as a source of tells, and no coverage of engagement-bait closers ("Agree?", "Comment YES"), comment-a-keyword hooks, one-line paragraph breaks, "Here's the thing", or fake-vulnerability narratives. These stay [Unverified] as AI tells from primary sources (earlier note correct).
- Partial overlaps that exist on the page: "It's not X, it's Y" (negative parallelism), rule of three, emoji at the start of headings or list entries, bold overuse, inline-header vertical lists, "social media presence", puffery ("pivotal", "landscape", "testament"), "valuable insights", "Overall" and "In conclusion" summaries, vague "Experts argue". The page also says "Many elements of AI writing can be found in editorials, blogs, or fan fiction", and mentions "punched up" sales-like writing in the em dash section.
- Footnote worth noting: "the many tells specific to fiction (whispering woods, Elara Voss, etc.) ... are not listed here", so the page is deliberately encyclopedic.

## 2. Kobak et al., Science Advances 2025

Primary pages: https://arxiv.org/abs/2406.07016 (v5, last revised 3 Jul 2025, "v5: Reverting to v3"), https://arxiv.org/abs/2406.07016v4, https://arxiv.org/html/2406.07016v5. Journal reference on the arXiv page: "Science Advances, 2 Jul 2025, Vol. 11, No. 27", DOI 10.1126/sciadv.adt3813. Title: "Delving into LLM-assisted writing in biomedical publications through excess vocabulary".

- Corpus size: CORRECTED. Earlier note said 14M PubMed abstracts. v5 abstract (the published version) says "over 15 million biomedical abstracts from 2010--2024 indexed by PubMed"; full text: "all 15.1 M English-language abstracts from 2010 onwards". The "14 million" figure is from v4 only.
- Lower bound: CORRECTED. Earlier note said "at least 13.5% in an earlier version, at least 10% in the later version". The reverse is true. v4 abstract: "at least 10% of 2024 abstracts were processed with LLMs... reaching 30% for some sub-corpora" (14 million abstracts). v5 (equal to v3, the journal version): "at least 13.5% of 2024 abstracts were processed with LLMs... reaching 40% for some subcorpora." Use 13.5% and 40%.
- Excess words: CONFIRMED with detail. Full text: "Less common words with strong excess usage included delves (r = 28.0), underscores (r = 13.8), and showcasing (r = 10.7)... More common words with strong excess usage included potential (δ = 0.052), findings (δ = 0.041), and crucial (δ = 0.037)". Earlier note's "potential, findings, crucial, delve": CONFIRMED (the word is "delves", r = 28.0).
- Other figures: 379 style words with elevated frequency in 2024; number of excess words rose to 454 in 2024 (190 in 2021 during Covid); of 379 excess style words in 2024, 66% were verbs and 14% adjectives; 900 unique excess words annotated for 2013-2024 (51.3% content, 45.2% style). Abstract also says the effect surpasses Covid.
- Caveat on "delve" counts (5,526 uses in 2024 vs 108,616 for "explore") comes from Language Log, a secondary source. Not checked (host not on the allowlist). [Unverified].
- Note: the paper's domain is biomedical abstracts, so it does not show LinkedIn behaviour.

## 3. Originality.ai LinkedIn AI-content study

Primary page: https://originality.ai/blog/ai-content-published-linkedin (also served at /pt/blog/...). Page metadata: datePublished 2024-11-25, dateModified 2026-07-30. Title now: "LinkedIn AI Content Study: 81% of Long-Form Posts Are Likely AI - 'Seems Like AI Slop' Feature Rolling Out". Author Jonathan Gillham, dated July 30, 2026.

What the current primary page says:
- "In July 2026, we analyzed 5,000 public LinkedIn posts across nine topics. More than four in five (81.2%) were classified as Likely AI." "4,061 of 5,000 posts were Likely AI: 81.2%."
- Method: "nine topics, posts of at least 100 words, and Originality.ai's 15% AI Allowance"; 10 pages of results from 90 topic-and-date searches, de-duplicated; "This covers public LinkedIn posts found through our searches, not every LinkedIn post or anyone's personal feed."
- "The earlier study ended with over half of long-form posts classified as Likely AI"; "from roughly half of sampled long-form posts in late 2024 to well over three-quarters today."
- LinkedIn Chief Product Officer Hari Srinivasan is quoted as saying AI slop is "a top priority"; the "Seems like AI slop" option is in the three-dot menu; 404 Media independently reproduced it. The page says LinkedIn "has not said whether the option is available globally." This matches the earlier note's 30 July 2026 date for the report option: CONFIRMED.

Claims from the earlier note:
- "8,795 posts, ~54% likely AI (October 2024)": the current page no longer contains "8,795", "54%" or any 2024 sample figures (grep found none). The earlier study is only described as "over half". Status: [Unverified] against the primary write-up as it exists now (the original 2024 text was overwritten). Do not cite 8,795 or 54% as read from Originality.ai. Note that the page itself says the July 2026 sample is different (5,000 posts), so the 54% and 81.2% come from different sample designs.
- "Share of AI posts": current primary figure is 81.2% (July 2026, 5,000 posts, 100-word minimum). The earlier note's 54% is superseded for 2026 purposes and its source is now secondary only.
- "45% less engagement": NOT in the primary page. The words "engagement", "45%", "3,368", "107%" and "189%" do not occur on the page. Status: CONTRADICTED as a primary-page claim (primary page has no engagement finding at all); the figure remains secondary/vendor-reported [Unverified].
- Page lists no other LinkedIn engagement study on originality.ai: the originality.ai sitemap contains only one LinkedIn study URL (`ai-content-published-linkedin`); other LinkedIn URLs are templates or tool reviews (`linkedin-statistics`, `mention-ai-linkedin-post-review`, etc.). Not opened.
- Counter-evidence figures (6.85% vs 6.22%, 75% etc.) attributed to PPC Land: [Unverified] (PPC Land blocked).
- Pangram 41% fully AI: [Unverified] (PPC Land blocked; Pangram not on allowlist).
- Caveat that Originality counts AI-edited text as likely AI: current page uses "Likely AI" with a "15% AI Allowance", which supports the caveat that the label is a detector threshold, not proof of fully machine-written text.

## 4. arXiv 2510.24011 (AI disclosure and trust)

URLs: https://arxiv.org/abs/2510.24011 (v2, 22 Jan 2026) and https://arxiv.org/html/2510.24011. Title: "Understanding Reader Perception Shifts upon Disclosure of AI Authorship". Authors: Hiroki Nakano, Jo Takezawa, Fabrice Matulic, Chi-Lan Yang, Koji Yatani. HTML page: "Accepted at 31st International Conference on Intelligent User Interfaces (IUI '26)."

- Sample and result: CONFIRMED. Abstract: "We conducted a study with 261 participants... six distinct communicative acts. Our analysis of 990 responses shows that disclosure generally erodes perceptions of trustworthiness, caring, competence, and likability, with the sharpest declines in social and interpersonal writing."
- AI literacy: CONFIRMED. "higher AI literacy mitigates these negative perceptions, leading to greater tolerance or even appreciation for AI use."
- Share of AI: the full text varies the disclosed AI proportion "from 0% to 100% in 10% increments"; the body text says effects are stronger with higher disclosed AI share ("perceptions are shaped not only by the degree of AI authorship but also by perceived human effort, emotional context, and readers' AI literacy"). Earlier note CONFIRMED.
- Design caveat: CONFIRMED. "we used a deception-based design: while all texts were entirely AI-generated (with minor human proofreading), participants were told that only specific portions were created or altered by AI." Stimuli generated with GPT-4o (English, then translated to Japanese). New: texts were translated into Japanese, so participants are presumably Japanese-language readers (inferred from the translation step; participant demographics not checked in full).
- Thematic analysis links negative shifts to "a perceived loss of human sincerity, diminished author effort, and the contextual inappropriateness of AI."
- Also: the effect concerns a fictitious author and short sentences, not LinkedIn posts, so applicability is by analogy.

Related paper cited in the earlier note: https://arxiv.org/abs/2507.01418 (Cheong et al., "Penalizing Transparency?"): CONFIRMED. Abstract: "both human raters (n = 1,970) and LLM raters (n = 2,520) evaluated a single human-written news article... both human and LLM raters consistently penalize disclosed AI use." Earlier note called it a "pre-registered survey of 1,970 people": the abstract says "large-scale controlled experiment", and "pre-registered" was not seen on the abstract page. Also the same paper has 2,520 LLM raters; it is a single news article. CORRECTED on wording ("controlled experiment", not "survey"; pre-registration [Unverified]). The "CHIWORK 2025 workshop paper" label was not checked.

## 5. Edelman-LinkedIn B2B Thought Leadership Impact Reports (2025, 2026)

Edelman pages: https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report and .../2026-b2b-thought-leadership-report returned HTTP 403 Access Denied (Akamai). Trade press: PPC Land (403 Cloudflare challenge), ContentGrip (proxy refused tunnel), Search Engine Land (403 Cloudflare challenge). No page quoting the report was fetched. Every statistic below is therefore [Unverified] against primary or trade-press pages in this pass.

| Claim in original_value.md | Status |
|---|---|
| 79% more likely to champion a vendor in an RFP if it consistently publishes quality thought leadership (2025) | [Unverified] |
| 56% vs 14% (demonstrating understanding of challenges vs product strength, for trust) (2025) | [Unverified] |
| More than 40% of B2B deals stalled by internal misalignment (2025) | [Unverified] |
| 84% used AI to summarize thought leadership in vendor evaluation (2026) | [Unverified] |
| 82% say thought leadership is becoming more valuable as AI spreads (2026) | [Unverified] |
| 59% of final decision-makers say poor or absent thought leadership contributed to a vendor being removed (cited to the 2026 page) | [Unverified] |
| 1,934 executives, 17 March to 3 April 2025 (2025 sample) | [Unverified] |
| 1,135 professionals in seven markets (2026) | [Unverified] |

Cautions to carry forward:
- The 59% figure is cited in original_value.md to the 2026 page but in its takeaway was used alongside 2025 findings; confirm which edition and which base (final decision-makers only) before publication.
- The earlier note itself flags "72-79%" and "71% vs 75%" as conflicting; those remain unresolved.
- Do not cite these numbers as "verified"; they need a manual check by someone able to open edelman.com (or the PDF through a browser).

## 6. Fast Company coverage of AI slop on LinkedIn

Fast Company pages are blocked (DataDome captcha, HTTP 403 on https://www.fastcompany.com/ and each of the three article URLs). Not bypassed.

Existence claims from the earlier note, all [Unverified] here because the pages could not be opened:
- https://www.fastcompany.com/91237998/how-linkedin-opened-the-door-to-ai-slop
- https://www.fastcompany.com/91545007/linkedin-declares-war-on-ai-slop
- https://www.fastcompany.com/91603675/how-to-sound-human-ai

Indirect evidence: Originality.ai's primary page (section 3) and the earlier note's other cited outlets agree that LinkedIn announced an anti-slop push and a "Seems like AI slop" option in July 2026. That supports the underlying story (CONFIRMED via originality.ai, which links to "LinkedIn's feed policy" and 404 Media), but it does not verify the Laura Lorenzetti quotes or the Fast Company articles. The Lorenzetti quote and "94% accuracy" and "40% fewer views" figures remain [Unverified].

## Summary

Confirmed (primary page read):
- Wikipedia: advice page, descriptive not prescriptive, "do not merely treat these signs as the problems to be fixed"; AI-vocabulary list including delve, pivotal, tapestry, testament, underscore, crucial, enhance, landscape; era dating (delve falling off in 2025; Grok overusing "underscore" in 2026); negative parallelism, rule of three, vague attribution ("Some critics argue", "Experts argue"), puffery, title case, curly quotes, emoji in headings and lists.
- Kobak et al.: excess words delves/underscores/showcasing and potential/findings/crucial; Science Advances 2025.
- Nakano et al. (2510.24011): 261 participants, 990 responses, disclosure lowers trust/caring/competence/likability, AI literacy mitigates, deception design, GPT-4o texts, accepted at IUI '26.
- Cheong et al. (2507.01418): 1,970 human raters penalise disclosed AI use.
- Originality.ai: LinkedIn study exists; 30 July 2026 date and the "Seems like AI slop" option are confirmed on the primary page.

Corrected:
- Kobak: 15 million abstracts (15.1 M English abstracts), not 14M; the published 13.5% lower bound (up to 40% for some subcorpora) is the later version, v4's 10% (30%) the intermediate one. The earlier note had the version order reversed.
- Wikipedia em dashes: now a "historical indicator" (2022-Sept 2026), best used in combination; models are increasingly suppressing them.
- Wikipedia negative parallelism: the page says it is common in human writing and only "stereotypically" an AI sign, not "rare in natural speech".
- Wikipedia on "It's important to note": listed as a 2023-2024 era didactic disclaimer, not a current lead tell.
- Rule-of-three "fine ... in every sentence is not" is a blog quote, not on the Wikipedia page.
- Originality.ai's headline figure is now 81.2% of 5,000 July 2026 posts (4,061 posts), replacing "about 54% of 8,795 posts" as the primary-page number.
- Cheong et al. is a controlled experiment (single news article), not described as a survey on the abstract page.
- Wikipedia vocabulary list has more words than the earlier note listed (e.g., robust, meticulous, interplay, garner, align with, boasts, deep dive, valuable, vibrant, fostering, showcase).

Contradicted:
- "45% less engagement" is not in the primary Originality.ai page; the page contains no engagement analysis. Treat as secondary only.

Still unverified ([Unverified]):
- All Edelman figures (79%, 56% vs 14%, 40% of deals, 84%, 82%, 59%, sample sizes), because edelman.com, PPC Land, ContentGrip and Search Engine Land were all unreachable.
- Original 2024 Originality.ai figures (8,795 posts, 54%, 107% word count, 3,368 posts/99 profiles) and any engagement figure; Pangram 41%.
- All three Fast Company articles and the Lorenzetti quotes; LinkedIn 94% and 40% figures.
- "Here's the thing", broken-line paragraphs, fake vulnerability and engagement-bait closers as documented AI tells (absent from Wikipedia).

Hosts that blocked or limited access: www.edelman.com (403 Akamai), ppc.land (403 Cloudflare challenge), searchengineland.com (403 Cloudflare challenge), www.fastcompany.com (403 DataDome captcha), contentgrip.com and www.contentgrip.com (proxy refused CONNECT tunnel, 403). en.wikipedia.org API rate-limited (429) but action=raw worked. arxiv.org, originality.ai and en.wikipedia.org (raw) were reachable.
