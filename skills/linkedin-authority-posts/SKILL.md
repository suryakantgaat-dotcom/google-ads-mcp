---
name: linkedin-authority-posts
description: Drafts LinkedIn posts that build authority for a performance marketer (Google Ads, Meta Ads, paid media) from the user's real data, with an anti-slop self-check and evidence-labelled defaults. Use this skill whenever the user wants a LinkedIn post, hook, carousel outline, case study, teardown, experiment write-up, contrarian take, or personal-brand content about paid media, even if they only say "write me something for LinkedIn", "turn this campaign result into a post", "help me post this week", or ask how often or when to post. Also use it to review a draft for AI-sounding patterns or to log post results.
---

# LinkedIn authority posts

Write posts that a hiring manager, client or peer would treat as evidence of expertise. Authority comes from first-hand results and committed judgment, so the work starts with the user's material, not with prose.

Why intake comes first: the research behind this skill found that the best-supported rule is "publish specific, substantive content". LinkedIn's March 2026 feed post says it is reducing generic, recycled, low-substance posts and engagement bait. A language model fills gaps with plausible-sounding numbers, and an invented number or client result is worse than no post. Never supply a figure, client name, result or quote the user did not give you.

## Workflow

1. **Intake.** Collect the inputs below. If any required one is missing, ask for it; do not guess or fill it in. Ask in one short batch, not one at a time.
2. **Permission gate.** If the post uses client or employer results, run `references/client-results-checklist.md` before drafting. If permission is unconfirmed, draft with anonymised or indexed numbers, or switch to the user's own or test accounts.
3. **Pick a post type** with the user, from `references/post-types.md` (case study, teardown, experiment write-up, contrarian take, framework). Use that file's skeleton and required inputs.
4. **Draft.** Apply the defaults in `references/rules-and-defaults.md` and the voice notes in `references/voice-samples.md`. If the voice file is empty, draft in plain neutral prose, say the voice is not calibrated, and ask for 3 to 10 samples of the user's own writing or posts they admire.
5. **Companion passes.** Run the `content-writing` skill's copywriting, copy-edit and humanise passes on the draft, in that order, as set out in `references/companion-skills.md`. They improve hook, flow and voice. They must not add facts: any detail, anecdote or number comes from the user's intake or is asked for.
6. **Final gate.** Run `references/anti-slop-checklist.md` on the result. It works on clusters of tells, not single words. Fix by adding the missing specific, not by swapping words. Then re-trace every number, date, name and quote to the intake, since the companion passes edit text.
7. **Deliver** in this shape:
   - the post (plus one alternate hook)
   - **Claims to verify**: every number, date, causal claim and named entity, each marked with where in the user's input it came from
   - **Defaults being tested**: which of length, format, hook, CTA, time or cadence this post uses, and a pre-filled row for `references/measurement-log.md`
   - one line on which companion passes ran and whether any changed a fact

## Required inputs

| Input | Why it is needed |
|---|---|
| What happened: account type, spend band or scale, dates, what was changed | The post has nothing to say without it |
| Baseline and result, with the metric and the time window | Authority comes from a before and after, not an adjective |
| Caveats: sample size, seasonality, other changes, what did not work | Honest limits are what separate evidence from a pitch. Search Engine Land experiment write-ups model this (not read; evidence level I) |
| The point of view: what the user believes that most peers do not, and when they would change their mind | A narrow, defensible position is what practitioner sources recommend (level C) |
| Client permission status | Legal and contractual risk; see the checklist |
| Audience emphasis for this post: hiring managers, clients or peers | Changes the stakes, the vocabulary and the close |

Optional: target accounts to comment on, a link or asset to attach, a posting date.

## How to present evidence

The defaults in the reference files carry labels: **A** stated by LinkedIn or in a paper and read on the primary page; **B** large vendor dataset; **C** practitioner opinion or a small test; **I** inference; **[Unverified]** no traceable source. Present B, C and I items to the user as defaults to test on their own audience, not as how LinkedIn works. Do not state any [Unverified] item as a rule. That includes golden hour, a fixed hashtag count, comments counting double, 360Brew, edits resetting reach, a numeric link penalty, and "LinkedIn penalizes AI-written content". If the user asks about one, say it is unverified and give what the sources do show.

## Boundaries

- No engagement pods, comment automation or third-party comment tools. LinkedIn has said it is targeting them (level A).
- No "comment to agree" prompts, requests for likes, reactions or shares, or reaction polls (level A).
- Do not draft comments for the user to post as if typed by them in bulk; help them write a specific comment on a specific post when asked.
- This skill does not give legal advice. The checklist is a prompt for the user to confirm consent, not a legal opinion.
- Known gaps in the research (hiring-manager preferences, named creators, structure-level data, Edelman figures not read) are listed at the end of `references/rules-and-defaults.md`. Mention a gap when it bears on the user's question.
