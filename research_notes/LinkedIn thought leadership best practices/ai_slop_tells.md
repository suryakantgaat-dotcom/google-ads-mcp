# AI-slop tells in LinkedIn posts and how to avoid them

Research limits: in this session WebFetch was blocked for every host (wikipedia, linkedin, originality.ai, arxiv, fastcompany and others failed DNS), so primary pages could not be opened. All findings below come from WebSearch result summaries, which cite the URLs given. Where a claim is only in a secondary or vendor source, it is labelled. Primary pages worth verifying by hand: the Wikipedia guide, the LinkedIn announcement, the Originality.ai study, the Kobak et al. paper.

## 1. What lexical and structural tells are documented?

### Takeaway
Documented tells fall into three layers. First, a small set of words that spiked after ChatGPT (Kobak et al.; Wikipedia's guide). Second, structures: negative parallelism, rule of three, inflated significance, vague attribution, heavy em dashes. Third, formatting: emoji in headings or bullets, title-case headings, curly quotes. Wikipedia and the academic literature both stress that these are signals, not proof, and that the tells shift with each model generation.

### Cited Findings
- Wikipedia's "Signs of AI writing" is an advice page from WikiProject AI Cleanup, not policy. It is descriptive, says no single sign proves AI authorship, and warns that fixing surface signs makes detection harder. — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (via search summaries; page not opened), [ScriptGrain](https://scriptgrain.com/blog/wikipedia-signs-of-ai-writing)
- Wikipedia's "AI vocabulary" heading lists: "tapestry" (abstract noun), "testament", "underscore" (verb), "pivotal", plus crucial, delve, enhance, "landscape" (abstract noun). Search summary says the list is dated by model era: delve, pivotal and underscore are tied to 2023 to mid-2024 (GPT-4), with later lists for GPT-4o and GPT-5; a mirror says Grok overused "underscore" as of 2026. — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [UV mirror](https://unvis.it/en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Puffery: LLM text inflates a subject's importance by claiming minor details represent a broader topic, even for mundane subjects like etymology or population data. Phrase example from secondary coverage: "stands as a testament to". — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Beutler Ink](https://www.beutlerink.com/blog/how-to-spot-ai-writing)
- Negative parallelism, the "not X, but Y" contrast-reframe, is flagged as constant in AI output and rare in natural speech. — [Beutler Ink](https://www.beutlerink.com/blog/how-to-spot-ai-writing), [Blake Stockton](https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/)
- Rule of three is flagged when overused: "the rule of three is fine; the rule of three in every sentence is not". — [Blake Stockton](https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/)
- Em dashes: the guide does not ban them; it says LLM output uses them more than nonprofessional human text of the same genre, and in places where humans would use commas, parentheses, colons or hyphens. Secondary sources conflict on whether the guide now treats em dashes as a leading sign or a dated one. — [Beutler Ink](https://www.beutlerink.com/blog/how-to-spot-ai-writing), [Rewritica](https://www.rewritica.com/blog/signs-of-ai-writing)
- Vague attribution to unnamed authority, example "some critics argue". — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (via search summary)
- "It's important to note" style phrases insert interpretation (secondary-source reading). — [Wikipedia discussion summary, Medium](https://medium.com/@sakaerka/wikipedia-discussion-signs-of-ai-writing-11a98ff61669)
- Formatting: title-case section headings, curly quotes and apostrophes, and emoji on headings or list items are listed as signs. — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Humaniser](https://humaniser.com/blog/signs-of-ai-writing)
- Academic word-frequency study (Kobak et al., Science Advances 2025): analysed 14M PubMed abstracts from 2010 to 2024, comparing 2024 word frequency against a counterfactual projected from 2021-2022. Excess-use words in 2024 include "potential", "findings", "crucial", and "delve". Estimates of LLM-processed 2024 abstracts: at least 13.5% in an earlier version, at least 10% in the later version. — [arXiv 2406.07016](https://arxiv.org/abs/2406.07016v5), [Language Log](https://languagelog.ldc.upenn.edu/nll/?p=64877)
- Caveat on word lists: "delve" had 5,526 uses in 2024 versus 108,616 for "explore", so a relative spike is not an absolute marker, and word fashions exist independent of LLMs. — [Language Log](https://languagelog.ldc.upenn.edu/nll/?p=64877)
- LinkedIn-specific patterns (vendor and blog sources, not research): engagement-bait closers such as "Agree?" and "Comment YES if this resonates", comment-a-keyword hooks, "it's not X, it's Y" constructions, emoji bullets, and cliche openers. — [Taplio](https://taplio.com/blog/linkedin-ai-slop), [Soloop](https://www.soloop.io/blog/linkedin-ai-slop-rules), [Peerlist](https://peerlist.io/danielsinewe/articles/ai-slop-on-linkedin-and-x-evidence-drivers-harms-detection-a)
- Generic-advice tell: AI output gives information and advice that offends no one, and avoids sounding honestly uncertain, amused, irritated or committed. — [Fast Company](https://www.fastcompany.com/91603675/how-to-sound-human-ai) (via search summary)
- Evenly sized sentences and openers like "this essay will explore", "in conclusion", "the role of" are cited as tells. — [PR Daily](https://www.prdaily.com/4-reasons-your-writing-accidentally-sounds-ai-generated-and-how-to-fix-it/) (via search summary)

### Inferences
- A Wikipedia-derived vocabulary list is a poor LinkedIn filter on its own. The page documents encyclopedic text, and the LinkedIn-specific patterns come from vendor blogs. Structure (contrast-reframe, triads, inflated stakes, generic closers) is better supported than single words.
- Because the lists are model-era specific, any fixed banned-word list will date quickly.

### Gaps
- "Here's the thing", one-sentence broken-line paragraphs, fake vulnerability ("I was fired / I cried in my car" narratives) and "hook, line break, moral" templates: I found no research or primary source documenting these as AI tells. They remain [Unverified] as AI-specific markers, although widely mentioned anecdotally.
- I could not open the Wikipedia page, so the full list of sections and exact wording is unconfirmed.
- No peer-reviewed study of LinkedIn-specific lexical markers was found.

## 2. How do AI-generated LinkedIn posts perform, and how do audiences perceive them?

### Takeaway
Prevalence is high (Originality.ai: about 54% of long posts likely AI; Pangram: 41% fully AI). Engagement evidence is thin and conflicting: a widely repeated "45% less engagement" figure comes from detector labels and vendor blogs, while the same coverage reports that human-edited AI posts did as well or better. Academic work shows disclosed AI use lowers trust, a penalty that is strongest where authenticity matters.

### Cited Findings
- Originality.ai analysed 8,795 LinkedIn posts of at least 100 words and found about 54% of long-form posts from October 2024 were likely AI-generated; AI involvement was negligible in the years before ChatGPT. Word count of AI-assisted long posts rose about 107% after ChatGPT; early-2023 spike reported as 189% (eWeek) or 186% (Website Planet). — [Originality.ai](https://originality.ai/pt/blog/ai-content-published-linkedin), [Fast Company](https://www.fastcompany.com/91237998/how-linkedin-opened-the-door-to-ai-slop), [eWeek](https://www.eweek.com/fr/news/ai-generated-posts-flood-linkedin/), [Website Planet](https://www.websiteplanet.com/news/linkedin-long-posts-ai)
- Caveat: the 54% counts fully AI, AI with human edits, and human text heavily AI-edited, so it does not equal fully machine-written; detectors are imperfect. — [Website Planet](https://www.websiteplanet.com/news/linkedin-long-posts-ai)
- Pangram Labs reported 41% of LinkedIn long-form posts (over 250 words) are fully AI-generated. — [PPC Land](https://ppc.land/over-half-of-linkedin-posts-are-now-likely-ai-but-authenticity-still-wins/)
- Engagement: likely-AI posts averaged 45% less engagement than likely-human posts per Originality.ai, reported by secondary sources. Sources disagree on the sample (3,368 posts from 99 influential profiles vs the 8,795-post study), and I could not confirm the figure in the original write-up. — [PPC Land](https://ppc.land/over-half-of-linkedin-posts-are-now-likely-ai-but-authenticity-still-wins/), [Flight Deck Advertising](https://flightdeckadvertising.com/blog/linkedin-ai-generated-posts-engagement-study)
- Counter-evidence in the same coverage: AI-assisted posts (AI draft, human-edited) averaged 6.85% engagement vs 6.22% for purely human; AI leadership/inspiration posts beat human by 75%; human posts won in healthcare (208 vs 116 interactions). These come from a vendor follow-up summary. — [PPC Land](https://ppc.land/over-half-of-linkedin-posts-are-now-likely-ai-but-authenticity-still-wins/), [SocialNexis](https://socialnexis.com/guides/ai-post-performance-by-format)
- Perception: in a 261-participant study (Nakano et al., IUI '26), disclosing AI authorship lowered perceived trust, caring, competence and likability, more so with higher disclosed AI share and in interpersonal contexts; higher AI literacy correlated with more tolerance. Design used deception about AI share and GPT-4o texts only. — [arXiv 2510.24011](https://arxiv.org/html/2510.24011)
- A pre-registered survey of 1,970 people found human and LLM raters both penalised disclosed AI use. — [CHIWORK 2025 workshop paper](https://arxiv.org/html/2507.01418v1)
- Secondary report of 16 experiments with 27,491 participants: readers discounted writing equally whether told it was human-AI collaboration or purely AI; mediator was perceived authenticity. Only found via a mirror site. [Unverified against original]. — [Novamag mirror](https://zk8xobzkidue2qet2.mags.novamag.de/de/2026/research-shows-why-readers-consistently-devalue-ai-generated-creative-)
- Counterpoint: other studies rate AI text as equal or better when efficiency and accuracy are valued. — [CHIWORK 2025](https://arxiv.org/html/2507.01418v1) (via search summary)

### Inferences
- The strongest finding for a thought-leadership strategy is the authenticity penalty. The risk is being perceived as AI, not just being AI.
- Detector-based engagement gaps conflate "AI-like" style with AI use; they cannot separate causes.

### Gaps
- No rigorous, independent measurement of LinkedIn reach for AI vs human posts; the "30% less reach" claim is from unnamed analysts [Unverified].
- Original Originality.ai engagement methodology not confirmed (fetch blocked).

## 3. LinkedIn's stated policy and ranking stance

### Takeaway
LinkedIn does not ban AI-assisted writing. In 2026 it announced classifiers to detect and down-rank generic or low-quality AI content and engagement bait, and added a "Seems like AI slop" report option. Several numeric claims are second-hand.

### Cited Findings
- LinkedIn's feed update says it is reducing recycled and click-driven posts ("Less generic content and engagement bait") and is rolling out upgraded classifiers to detect and down-rank both AI-generated and generally low-quality posts, with LLM-augmented ranking. — [LinkedIn News](https://news.linkedin.com/2026/ImprovingTheFeed) (via search summary)
- Laura Lorenzetti (LinkedIn VP and Executive Editor) wrote that overused, automated AI "dilutes the valuable insights that real human conversations can spark"; AI-assisted content remains welcome if it has original ideas or encourages meaningful conversation; flagged posts are not deleted. — [Fast Company](https://www.fastcompany.com/91545007/linkedin-declares-war-on-ai-slop), [Engadget](https://www.engadget.com/2174163/linkedin-doesnt-want-your-ai-slop-anymore/), [Entrepreneur](https://www.entrepreneur.com/business-news/linkedin-is-fighting-back-against-ai-slop-and-ai-comments) (via search summaries)
- Targets named include generic AI-generated posts and comments, attention-bait video, and automation tools generating AI content. — [Channel News](https://www.channelnews.com.au/linkedin-moves-to-reduce-ai-generated-spam-across-user-feeds/), [The Next Web](https://thenextweb.com/news/linkedin-ai-slop-crackdown-generic-content)
- A "Seems like AI slop" report option appeared around 30 July 2026; reports reportedly tune classifiers and ranking. — [AlternativeTo](https://alternativeto.net/news/2026/7/linkedin-adds-a-seems-like-ai-slop-button-to-report-low-quality-ai-generated-content/), [Futurism](https://futurism.com/artificial-intelligence/linkedin-adds-button-report-seems-like-ai-slop)
- Second-hand numbers: 94% accuracy flagging generic content in early tests (Channel News); about 40% fewer views for flagged content (CPO, reported secondhand). Reach limits are described differently across outlets (limited to immediate network vs visible to direct connections). — [Channel News](https://www.channelnews.com.au/linkedin-moves-to-reduce-ai-generated-spam-across-user-feeds/), [Taplio](https://taplio.com/blog/linkedin-ai-slop)

### Inferences
- LinkedIn's stated test is value, not provenance: original idea or genuine conversation vs generic, recycled, bait.

### Gaps
- Primary LinkedIn text not read; the 94% and 40% figures are unverified. One snippet mentioning a March 2026 "Authenticity Update" came from a single FAQ page [Unverified].
- Tomer Cohen was not tied to any slop statement.

## 4. Practical techniques from credible writers and editors

### Takeaway
Sources converge on: supply specifics and first-hand experience yourself, give the model samples of your own prose, edit for clusters of tells rather than banning words, and keep human control on reputation-bearing thought leadership. Sources are mostly newsletters and vendor blogs, so these are expert opinion, not tested results.

### Cited Findings
- Specificity is the main fix: concrete detail, a case study, or a point of view from real experience in place of filler. — [Fast Company](https://www.fastcompany.com/91603675/how-to-sound-human-ai), [skills.sh style skill](https://skills.sh/conorbronsdon) (via search summaries)
- Voice samples: give the model a short sample of your own clean prose to imitate (sentence length, specificity, willingness to make judgments). — [Bea Krause Sorio, Substack](https://beakrausesorio.substack.com/p/how-to-write-well-with-ai-without)
- Do not let the model fill gaps: if you do not supply the number, it may invent one confidently. — [Your AI Copyeditor, Substack](https://youraicopyeditor.substack.com/p/stop-your-writing-from-sounding-like)
- Edit patterns, not single words: one em dash does not make text AI-sounding; "write naturally" is unhelpful advice. — [PR Daily](https://www.prdaily.com/4-reasons-your-writing-accidentally-sounds-ai-generated-and-how-to-fix-it/)
- Thought leadership and reputation-bearing content need closer human control than routine email. — [CPA Australia InTheBlack](https://intheblack.cpaaustralia.com.au/technical-skills/why-human-editing-still-matters-ai-generated-content)
- LinkedIn's own stated acceptance criterion (original idea or meaningful conversation) is consistent with the above. — [Fast Company](https://www.fastcompany.com/91545007/linkedin-declares-war-on-ai-slop)

### Inferences
- A practical workflow consistent with the sources: start from your own notes, data and anecdotes; use AI for structure or edit; remove contrast-reframes, triads, inflated stakes and bait closers; add named specifics; read aloud for voice.

### Gaps
- No controlled evidence that any technique raises LinkedIn performance or lowers detection or reader suspicion.
- Wikipedia's guide itself warns that surface fixes do not make text good, so technique should aim at content quality, not evasion.
