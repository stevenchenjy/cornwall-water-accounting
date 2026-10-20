# Independent human source-review handoff

All seven annual rows remain `ai_text_and_visual_checked`. Every human-review checklist row is pending. This guide and the local page index are preparation artifacts, not a completed independent review.

## Review materials

- [Seven-year checklist](source-review-checklist.csv): the printed quantities, pinned SHA256, original physical page and priority questions. New `review_type` and `reviewer_relationship_to_project` columns make independence explicit.
- [Pinned source table](../data/seed/annual-water.csv) and [retrieval receipts](../data/manifests/retrievals.csv): connect each observation to its original bytes and retrieval date.
- [Annual audit](../reports/annual-audit.md) and [bridge](../reports/reconciliation-bridge.md): reported observations versus conditional calculations.
- [Public evidence table](public-source-evidence.csv): billing-notice, minute, example-bill and draft-scope qualifications to check before any quantitative request exhibit is shared.

The local-only viewer is `data/interim/source-review/index.html` under this checkout. It shows the seven accounting pages with source/hash/page labels, original-PDF links and the pending checklist. It is intentionally ignored by Git and is not a public GitHub link. The reviewer should open the original PDF as well as the displayed accounting page; surrounding wording and report coverage matter. The viewer does not record a signature or change verification status.

## Prioritized seven-page review

The October 20 evidence-stage readiness check matched all seven originals to receipt byte counts/SHA256, checklist values and page-render hashes, checked physical page bounds, and inspected each rendered accounting page. This was an AI check of the review materials. Browser rendering of the optional local HTML index remains unverified. A person can review the original PDFs in a PDF reader without that index; the originals and images exist in this checkout, but are not delivered through GitHub.

Use this order. The hash prefixes below are navigation aids; compare the **complete 64-character hash** in the checklist and receipt before recording a review. Every row uses source ID `awqr-YYYY`; find the exact ignored original path and retrieval timestamp by that ID plus full hash in [retrievals.csv](../data/manifests/retrievals.csv). Do not choose a newer snapshot by date alone.

| Order | Report / physical page | SHA256 prefix | What the person must inspect |
|---|---|---|---|
| 1 | 2024 / 2 | `eef6fb90ef4f` | 283,389,000 annual gal; 774,287 daily production; 625,159 billed figure; 19.26%; explicit January 1-December 31 production dates. Daily context is not actual billed coverage. |
| 2 | 2025 / 2 | `f0124f4abce4` | 290,485,000 annual gal; 795,849 daily production; 531,229 billed figure; 33.25%; explicit production dates. Check residual-use wording and preserve unknown billing/scope fields. |
| 3 | 2020 / 2 | `095ed3712958` | Printed 36.6% and all three volume figures. Reproduce the conditional 366-day result near 36.00% and 365-day sensitivity near 36.1748%; neither establishes the actual denominator or an error's cause. |
| 4 | 2022 / 2 | `cd1f77ae766f` | Printed 13.15% versus conditional 12.7799%; 635,063 daily billed context repeats 2021. Do not correct it based on repetition alone. |
| 5 | 2021 / 7 | `c30779d5cbfb` | 280,356,000 annual gal and 768,098 daily production. The +0.6301 gal/day arithmetic difference fails nearest-1-gallon annual precision but fits nearest-100/1000 scenarios; the actual rounding rule is unknown. |
| 6 | 2023 / 7 | `aa7a685257af` | The 519,037 billed figure follows the daily-average sentence without an explicit per-day unit; the production paragraph gives the year without exact dates. Retain `contextual_daily_basis` and empty exact production dates unless new evidence resolves them. |
| 7 | 2019 / 5 | `8b13d5660356` | Four printed quantities, explicit production dates and one-decimal percentage precision. Use the original page layout because text extraction interleaves columns. |

For every row check US gallons versus gallons/day, percentage points versus percent, and all printed digits. The nearest-1/100/1000-gallon annual scenarios and nearest-gallon daily scenario are analytical sensitivity assumptions, not source-certified precision. The 2020 and 2022 discrepancies survive annual uncertainty of ±500 gal. Read the residual-use sentence: authorized unbilled uses and possible losses are included; the whole residual is not leakage. Check the report cover/PWS identifier as context without treating it as proof of unchanged yearly scope.

## Required review record

1. Record the reviewer identifier, local review date, relationship to the project and review type. Use `independent_human` only when a person independent of the AI extraction actually performs the checks. A same-author human check should be described accurately rather than called independent. Keep identifying notes locally unless their publication is approved.
2. Confirm the file's SHA256 and inspect the exact physical PDF page (1-based). Do not replace the pinned file with a fresh download or rely on extracted text alone. Note a changed or unavailable source rather than silently substituting it.
3. Check annual production, reported daily production, billed figure, unaccounted percentage and displayed precision. Check units and daily wording. Separate water-quality coverage, explicit production dates and unknown billing coverage.
4. Prioritize 2020's printed percentage and denominator alternatives; 2021's small annual/daily production difference and unconfirmed precision; 2022's percentage and repeated billed value; 2023's contextual daily interpretation and absent exact production dates; and 2024/2025's unconfirmed billing and measurement coverage. See the checklist's year-specific prompts.
5. Enter corrections or an exact review-memo reference. A signed/dated local memo should identify the inspected hashes/pages, findings and any unresolved qualifications. File hashes establish identity; they do not establish that the content was reviewed.
6. Mark a row `human_verified` only after a documented person's review. Record whether that review was independent separately. Any transcription correction must update the source/claim records and regenerate downstream reports without overwriting the original PDF. Do not remove accounting-coverage qualifications merely because the printed numbers match.

Before an external exhibit is attached, integrate documented corrections and review the regenerated table/chart and adjacent request text. Departmental period/boundary confirmation is a separate gate from human transcription verification. No review completion, signature or request dispatch is implied by this handoff.

Return one dated review memo covering all seven rows, or separate row memos, with a finding of matched, corrected or unresolved for each requested field. A row may be transcription-verified while its billing coverage remains unresolved; name that limit. The lead integrates corrections and updates provenance/claims before rerunning `make check` and preflight. Stop quantitative exhibit release if a source is missing, a hash differs, a material digit/unit remains disputed or the review is undocumented. The user still decides whether to authorize any correspondence.
