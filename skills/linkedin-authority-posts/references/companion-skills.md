# Working with the content-writing skill

The installed `anthropic-skills:content-writing` skill (`/content-writing`) bundles the copywriting, copy-editing, humanize-writing and social-content modules. No separate copywriting skill is installed, so "copywriting" here means its `write` module. This skill supplies the facts, evidence labels and claim discipline. content-writing supplies sentence-level craft. Each does what the other cannot.

## Order of operations

1. **Draft** (this skill, workflow step 4): facts from the user's intake, post-type skeleton, defaults, voice notes.
2. **Copywriting pass**: call `/content-writing write` (references `copywriting.md`, `copywriting-masters.md`, `copywriting-natural-transitions.md`). Scope it to the hook (first ~140 characters), the structure and flow, clarity, and the close. Use `social-content-post-templates.md` for hook variants.
3. **Copy-edit pass**: `/content-writing edit` (`copy-editing.md`). Tighten and cut. Do not let it add content.
4. **Humanise pass**: `/content-writing humanize`, mode "Rewrite AI", task type `social`. It uses `humanize-writing.md` and `humanize-writing-wikipedia-ai-signs.md`.
5. **Final gate** (this skill): run `anti-slop-checklist.md` again, then re-trace every number, date, name and quote to the user's intake. Companion passes edit text, so they can introduce errors. The final gate always runs last.

If a pass cannot be invoked (for example in a context without the Skill tool), read the named reference files directly and apply them, or skip the pass and say so in the delivery note.

Pass the companion skill these things so it works within the constraints: the post type, the audience, the voice notes from `voice-samples.md`, the facts list from intake, and the instruction "do not add facts".

## Precedence

When the two skills disagree, this skill wins on facts and on evidence-labelled advice. content-writing wins on sentence-level style, unless the change would alter a fact.

| Companion advice | What to do |
|---|---|
| humanize: "add one specific, concrete detail", "insert a real example", "add a personal anecdote" | Use only details the user gave in intake. If the post lacks one, ask the user for it. Never invent a detail, anecdote, number or client. |
| humanize: fix "generic examples" | Same rule. Replace with a real example from the user's work, or ask. |
| copywriting: add social proof, stats, testimonials | Only the user's own, with consent status confirmed (`client-results-checklist.md`). The copywriting reference itself says fabricated statistics erode trust. |
| copywriting: strengthen the CTA | Keep to R9: one specific question tied to the claim, or none. No "comment to agree", reaction requests, or keyword-comment funnels. |
| social-content: posting frequency (3 to 5 a week), calendar days, "link in comments", "comments are higher value than likes", daily 5 to 10 comment routine | Treat as untested defaults. Apply the evidence levels in `rules-and-defaults.md` (R10, R10a, R11, R12). Do not state link-in-comments or comment weighting as a LinkedIn rule: both are C or [Unverified]. Commenting yourself on target accounts' posts is fine. |
| social-content: hook formulas (curiosity, story, value, contrarian) | Use as options. R8 applies: hook rankings conflict across sources, so test. A hook must be true to the user's material. |
| humanize: em dashes banned entirely | Follow it. It costs nothing, though Wikipedia lists em dashes only as a historical sign that matters in combination with other signs. Do not tell the user em dashes alone mark text as AI. |
| humanize: add contractions, vary sentence length | Follow, unless the voice notes say otherwise. |
| humanize: any claim that a rewrite "passes" detection | Do not repeat it to the user. No technique has controlled evidence of lowering reader suspicion (`anti-slop-checklist.md`). |
| copy-editing: "Seven Sweeps" and similar | Use for clarity and cuts. Skip any sweep that adds claims. |

## Delivery note

After the passes, add one line to the delivery: which companion passes ran, and any change they made that touched a fact or a number (there should be none). If the voice file is empty, say so.
