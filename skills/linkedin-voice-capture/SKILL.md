---
name: linkedin-voice-capture
description: "Builds the user's writing-voice profile for LinkedIn from their own words: it reads how they write to the AI and anything they paste, sets short raw-writing exercises on specific topics, runs a brief interview, and offers ways to put their own voice into each draft. Use this skill whenever the user says \"capture my voice\", \"make posts sound like me\", \"learn my writing style\", \"I have no past posts\", or when the linkedin-authority-posts skill finds an empty or thin references/voice-samples.md. Also use it to refresh the profile after the user has published a few posts."
---

# LinkedIn voice capture

Collect evidence of how the user actually writes, then record it where the drafting skill reads it: the `references/voice-samples.md` file of the `linkedin-authority-posts` skill (in the source repo: `skills/linkedin-authority-posts/references/voice-samples.md`). This skill never writes samples for the user and never invents a quote.

Why raw samples: credible-writer sources recommend building a voice guide from the author's own writing (5 to 10 pieces) with explicit banned phrases (level C, from search summaries, not re-read). No source tested whether this lowers reader suspicion of AI authorship, so describe the profile as a drafting aid, not a guarantee.

## Workflow

1. **Gather what exists.** Ask what the user wants counted: their messages in this conversation, anything they paste, files they point to. Count only text the user wrote. Exclude pasted material by others and any text an AI wrote or edited, because that contaminates the profile. Say what you will read before you read it.
2. **First-pass observations** from that material, using `references/observation-guide.md`. Each observation carries the exact words it rests on and a tag: **[Observed]** (visible in the quoted text) or **[Inference]** (your reading of it). State the sample size and a confidence level. Writing to an AI is terse and directive and is not LinkedIn prose, so use it for word choice, directness and humour, and do not use it to set post rhythm or length.
3. **Writing exercises.** Give 3 to 5 prompts from `references/writing-prompts.md`, chosen to fit the posts the user plans (case study, teardown, experiment write-up, contrarian take, framework). Rules for the user: write fast, no AI help, no polishing, rough is fine, 80 to 200 words each. Dictating and pasting the transcript is allowed. Offer more rounds if the profile is still thin.
4. **Interview.** Ask the 8 questions in `references/writing-prompts.md` in small batches. Answers in the user's own phrasing go into the profile verbatim.
5. **Ways to add voice.** Offer the options below and ask which the user will use per post. Record the choice.
6. **Draft the profile** (format below). Show it to the user and change anything they dispute before saving. The user's correction outranks your observation.
7. **Save** to the `linkedin-authority-posts` skill's `references/voice-samples.md`: notes in the user's words where possible, samples verbatim, date, sample count, confidence. If that file cannot be written (an installed skill folder may be read-only), output the finished profile in a code block and tell the user to keep it in a file or project note and paste it into the chat when drafting.
8. **Refresh.** After the user has published 3 or more posts, ask for them (as posted, plus the drafts if available). Compare drafts with what the user changed and update the profile with the differences.

## Ways to add voice to a draft

Offer these as choices. None has controlled evidence of improving reach or reader trust; they are practical ways to keep the user's own words in the post.

| Method | What the user does |
|---|---|
| Write the first line and last line | The user writes the hook and the closing line by hand. The draft fills the middle from the user's facts. |
| Voice note first | The user talks through the result for 2 minutes, transcribes it, and the draft is built from the transcript, keeping their phrasing. |
| Disagree pass | The user reads the draft and marks every sentence they would not say, then rewrites those. |
| Phrase bank | The user keeps a running list of their own phrases, metaphors and pet peeves, and the draft uses them where they fit. |
| Opinion injection | The user adds one sentence starting "What I actually think is..." and it stays unedited. |
| Reaction capture | When something in an account surprises or annoys them, they send a one-line note at the time. The note becomes raw material. |
| Banned list | The user names words and structures they would never use. Add them to the profile. |

## Profile format

Write the profile in this form, filling only what the evidence supports. Leave a field as "not enough evidence" when it is.

- **Sample basis**: number of samples, total words, source of each (chat messages, exercise, past post), date.
- **Confidence**: low (under 5 samples or under 500 words), medium, higher. Say what would raise it.
- **Observed patterns** with quotes: sentence length range, paragraph length, openings, how they state a result, hedging, jargon, punctuation, first person or "we", humour, how they disagree.
- **Words and phrases they use** (verbatim) and **never use** (as stated by the user).
- **Topics and stances** they gave in the interview, in their words.
- **Chosen voice-adding methods** from the table.
- **Open questions** to settle with more samples.

## Boundaries

- Do not write the user's samples, rewrite their exercises "to improve them", or fill the profile with plausible traits. A trait needs a quote or an explicit statement from the user.
- Do not diagnose personality or character from writing. Describe the writing.
- Do not flatter the samples. Report what is there and what is missing.
- Do not store anything outside the repo. The profile lives only in the voice-samples file.
- Keep the user's private details (names, client data) out of the profile unless the user chooses to include them.
