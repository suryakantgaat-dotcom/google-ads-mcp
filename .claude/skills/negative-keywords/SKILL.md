---
name: negative-keywords
description: Decide which Google Ads search terms become negative keywords, at what level (shared list by type, campaign, or ad group), with which match type, and why — using the account owner's own rules. Use this whenever the user wants to review search terms, find wasted spend in search terms, build or clean negative keyword lists, stop irrelevant/competitor/brand queries leaking into a campaign, fix search terms split across ad groups, or prepare negatives before pausing/migrating a campaign — for any account (TrackoBit/TrackoField, Qura, Housr, or new ones), whether data comes live from the google-ads-mcp server or from a pasted search-terms export. Trigger on "negative keywords", "negatives", "search term report", "search terms audit", "block these queries", "wasted spend on search terms", "exclude", "neg list", even if the user doesn't say "negative keyword".
---

# Negative Keywords

> Status: draft. Rules come from the owner's interview; the skill has not yet been test-run on live data.

Turns a search-terms report into negative keywords using a fixed decision order the account owner taught. The reasoning is the same for every account and product; what changes is the **product profile** (what's relevant, which brands are competitors, which are unrelated). Profiles live in `references/profiles/`.

The owner's rules are numbered R1–R17 so every suggestion can cite the rule behind it. Do not invent rules. If a term doesn't fit any rule, put it in the "Needs your call" section rather than guessing.

---

## Step 0 — Load the product profile

1. Identify the product line of each campaign (profile lists the campaign-name → product mapping).
2. Read `references/profiles/<product>.md`. It defines: what's relevant, own-brand terms, competitor brands, known unrelated brands, known irrelevant modifiers, and known vague terms.
3. **No profile for this product?** Don't guess relevance. Interview the user with `references/profile-template.md`, write the new profile, then continue.

Relevance is the foundation of everything below, and it's product-specific — a word irrelevant to one product line can be core to another (R15).

## Step 1 — Get the data

**Live (google-ads-mcp `search` tool, pass `account_name` + `customer_id`):**

Search terms (costs in micros ÷ 1,000,000; widen the date range to what the user asked; search_term_view accepts ranges beyond 30 days, change_event does not):
```
resource: search_term_view
fields: ["search_term_view.search_term", "search_term_view.status",
         "campaign.name", "ad_group.name",
         "segments.keyword.info.text", "segments.keyword.info.match_type",
         "metrics.impressions", "metrics.clicks", "metrics.cost_micros", "metrics.conversions"]
conditions: ["campaign.id = <id>", "segments.date BETWEEN '<start>' AND '<end>'", "metrics.impressions > 0"]
orderings: ["metrics.cost_micros DESC"]
```
Page with cost bands (e.g. `metrics.cost_micros > 250000000`, then a band below) if results are large.

Active keywords of every campaign the negatives will apply to (needed for the conflict check):
```
resource: keyword_view   (or ad_group_criterion)
fields: ["campaign.name", "ad_group.name", "ad_group_criterion.keyword.text",
         "ad_group_criterion.keyword.match_type", "ad_group_criterion.status"]
conditions: ["ad_group_criterion.status = 'ENABLED'", "campaign.status = 'ENABLED'", "segments.date DURING LAST_30_DAYS"]
```
Competitor campaign keywords (define the competitor list, R14): same query filtered to the competitor campaign(s) named in the profile.

**Pasted export:** needs search term, campaign, ad group, impressions, clicks, cost, conversions. Keyword list for the conflict check if available; if not, say the conflict check was skipped.

State the coverage gap: the search terms report omits low-volume terms. Report visible conversions vs campaign total conversions.

## Step 2 — Classify each search term (in this order; first match wins)

Skip terms whose status is already EXCLUDED unless the existing negative is at the wrong level/list.

| Order | Test | Action | Match type | Level | Rule |
|---|---|---|---|---|---|
| 1 | Contains **own brand** (any spelling/variant in profile) and campaign is not the brand campaign | Negative | One-word brand → **broad** (`trackofield`); multi-word/spaced variant → **phrase** (`"track o field"`) | Shared **Own-brand** list, applied to all non-brand campaigns | R5 |
| 2 | Contains a **competitor brand** (brand present in competitor-campaign keywords, or named competitor in profile) and campaign is not a competitor campaign | Negative | **Broad**, brand word only (`unolo`) | Shared **Competitor** list (per product line), applied to non-competitor campaigns | R4, R14 |
| 3 | Contains **any other third-party brand** (not own, not competitor) | Negative | **Broad**, brand word only (`odoo`, `petpooja`) | Shared **Other-brands** list (per product line), applied to all campaigns of that product line | R3, R14 |
| 4 | **Irrelevant because of a modifier word** (the word that shows non-product intent, e.g. `excel`, `sheet`, `register`, `payslip`, `biometric`) | Negative the **modifier word only** | **Broad**, one word | Shared **Irrelevant-generic** list (per product line) | R1, R7 |
| 5 | **Vague / head term** with no product intent on its own (`field agent`, `team`, `software`, `dashboard`) | Negative the full query | **Exact** (`[field agent]`) so longer relevant queries still serve | Shared **Irrelevant-generic** list (per product line) | R8 |
| 6 | **Relevant** and served by **more than one ad group** | Don't block the term. Pick the owner ad group; add **exact** negatives in the other ad groups | **Exact** | **Ad group** (non-owner ad groups only) | R6, R10, R16 |
| 7 | **Relevant**, single ad group | **Never block**, even with spend and 0 conversions. List it under "Relevant, not converting" with the likely fix area (bid, ad, landing page) | — | — | R6 (relevant stays) |

Cross-cutting rules:
- **R1 Relevance first.** "Relevant" = matches the profile's product definition. A query containing one of our keyword words is still irrelevant if its intent is outside the product (e.g. payroll attendance for a field-force product).
- **R2 Conversions don't rescue irrelevant terms.** Irrelevant + converted → still negative; flag the conversions as likely junk leads in the reason column.
- **R12 Evidence: first sight.** An irrelevant term is negated on its first impression, regardless of clicks or spend. Spend thresholds do not apply to irrelevant terms.
- **R9 Variants reactively.** New misspellings and singular/plural forms are added when they appear in the report; don't pre-generate variant lists. Negatives don't expand to variants (see match-type notes), so each new form needs its own entry.
- **R10/R16 Owner ad group** for a split relevant term: the ad group with the most conversions for that term; if none converted, the ad group whose keyword/theme is closest to the query. If still unclear, put it in "Needs your call".
- Brand + irrelevant modifier in one query (e.g. `petpooja attendance`): the brand rule wins (order 3) — `petpooja` broad covers it. Don't also add the modifier unless it's independently irrelevant.

## Step 3 — Conflict check (before suggesting any broad or phrase negative)

A broad or phrase negative can block our own keywords. For every proposed broad/phrase negative, check it against the active keywords of every campaign the list/level applies to:
- **Broad negative** conflicts if every word of the negative appears in a keyword (any order).
- **Phrase negative** conflicts if the negative's words appear in the keyword in the same order.

If it conflicts: don't suggest it. Move the term to "Needs your call" and show the keyword it would block (e.g. broad `attendance` would block `field staff attendance app`). Offer the narrower alternative (a different modifier word, or the full query as exact).

Also never put own-brand negatives on the brand campaign, or competitor negatives on the competitor campaign.

## Step 4 — Output

**First, the review table** (don't produce the upload file until the user approves):

```
[Account] · [Campaign(s)] · [date range] · currency
Coverage: visible conversions X of campaign total Y

### Negatives to add
| # | Search term | ₹ Spend | Clicks | Conv. | Negative | Match | List / Level | Rule | Reason |

### Ad-group sculpting (relevant terms split across ad groups)
| Search term | Owner ad group (why) | Exact negative added in | Rule |

### Relevant, not converting (not blocked)
| Search term | ₹ Spend | Clicks | Ad group | Likely fix area |

### Needs your call
| Search term | ₹ | Why it's unresolved (conflict / no rule / unclear owner / unclassified brand) |
```

Totals per list (₹ of spend covered). Keep reasons short and tied to the rule.

**After approval, the upload files** (only approved rows):
1. **Shared lists** — one block per list name, paste-ready with match syntax (`word` broad, `"phrase"`, `[exact]`), for Tools → Shared library → Negative keyword lists. List names: `NEG – <Product> – Own Brand`, `NEG – <Product> – Competitors`, `NEG – <Product> – Other Brands`, `NEG – <Product> – Irrelevant Generic`. Also state which campaigns each list must be applied to.
2. **Ad-group negatives** — CSV for Google Ads Editor with columns `Campaign,Ad Group,Keyword,Criterion Type` and Criterion Type values `Negative exact` / `Negative phrase` / `Negative broad`. [Unverified column format — confirm on first Editor import and update this line.]

Save files where the user can open them and name the path.

## Match-type behaviour for negatives

Source: Google Ads Help, "About negative keywords" (support.google.com/google-ads/answer/12437241), read from the owner's saved copy.

Google's example, negative keyword "running shoes":

| Search | Broad `running shoes` | Phrase `"running shoes"` | Exact `[running shoes]` |
|---|---|---|---|
| running shoes | blocked | blocked | blocked |
| blue running shoes | blocked | blocked | shows |
| shoes running | blocked | shows | shows |
| running shoe | shows | shows | shows |
| blue tennis shoes | shows | shows | shows |

- **Broad** (default): blocks when the search contains all the negative's words, in any order; shows if only some words are present. Multi-word broad is risky (`track o field` broad would block any query containing `track`, `o`, `field` anywhere) — hence one-word broad only (R3, R4, R7) and phrase for multi-word brand spellings (R5).
- **Phrase**: blocks when the words appear in the same order; extra words around them are allowed. Extra characters on a word let the ad show.
- **Exact**: blocks only the exact words in the same order with no extra words; `field agent tracking app` still serves under `[field agent]` (R8).
- **No close variants**: negatives don't expand to plurals/singulars or other variants (`running shoes` doesn't block `running shoe`). They do account for casing and for misspellings where Google corrects the search results. `odoo` didn't block `www odu com` because that spelling isn't treated as a correction [inference]. New spellings and singular/plural forms are added as they appear (R9).
- **Symbols**: periods are ignored (`www.odoo.com` = `www odoo com`). `&` ≠ `and`, accented ≠ unaccented. Invalid: `, ! @ % ^ ( ) = { } ; ~ \` < > ? \ |` — strip these from search terms before proposing them. `site:`, `OR` and leading `-` are ignored or change meaning; don't use them.
- **16-word limit**: a negative word after the 16th word of the search isn't matched.
- Too many negatives can reduce reach — another reason relevant terms are sculpted, not blocked (R6).
- Account-level negatives exist (they also cover Performance Max and Shopping) but the owner does not use them; all lists stay per product line on Search campaigns (R15).

## Worked examples (owner's decisions, TrackoField)

| Search term | Decision | Why |
|---|---|---|
| www odoo com website (₹2,469, 12 clicks, 0 conv) | `odoo` broad → Other-brands list | Unrelated brand, not a competitor; blocked everywhere (R3) |
| petpooja attendance (₹570, 0 conv) | `petpooja` broad → Other-brands list | Unrelated brand wins over the attendance modifier (R3) |
| asanify payslip (₹704, 2 conv) | Block anyway (payroll intent) | Conversions from irrelevant queries are junk (R2) |
| track o field / trackofield pricing (₹1,464 in generic) | `"track o field"` phrase, `trackofield` broad → Own-brand list on non-brand campaigns | Brand traffic belongs to the brand campaign (R5) |
| attendance sheet in excel / attendance register staff / biometric attendance login | `excel`, `sheet`, `register`, `biometric` broad → Irrelevant-generic | Block the word that makes it off-topic (R7); `attendance` itself not blocked (conflict with `field staff attendance app`) |
| field agent (₹1,252, 11 clicks, 0 conv) | `[field agent]` exact → Irrelevant-generic | Vague head term; keep `field agent tracking app` (R8) |
| employee tracking app (₹3,374, 4 ad groups, 0 conv) | Not blocked. Owner = closest theme (none converted); exact negatives in the other 3 ad groups | Relevant terms are sculpted, not blocked (R6, R16) |
| unolo app | `unolo` broad → Competitor list on non-competitor campaigns | Competitor has its own campaign (R4) |

## Rules index

R1 relevance first · R2 conversions don't rescue irrelevant · R3 unrelated brands broad everywhere · R4 competitors blocked in non-competitor campaigns · R5 own brand out of non-brand campaigns · R6 relevant terms never blocked, split terms sculpted · R7 off-topic → modifier word broad · R8 vague → exact · R9 variants as they appear · R10 owner = best performer · R11 lists by type · R12 block on first sight · R13 table then upload file · R14 competitor = in competitor campaign or named · R15 lists per product line · R16 tie-break = closest theme · R17 same reasoning across accounts, profiles differ
