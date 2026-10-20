# Independent human source-review handoff

All seven annual rows remain `ai_text_and_visual_checked`. Every human-review checklist row is pending. This guide and the local page index are preparation artifacts, not a completed independent review.

## Review materials

- [Seven-year checklist](source-review-checklist.csv): the printed quantities, pinned SHA256, original physical page and priority questions. New `review_type` and `reviewer_relationship_to_project` columns make independence explicit.
- [Pinned source table](../data/seed/annual-water.csv) and [retrieval receipts](../data/manifests/retrievals.csv): connect each observation to its original bytes and retrieval date.
- [Annual audit](../reports/annual-audit.md) and [bridge](../reports/reconciliation-bridge.md): reported observations versus conditional calculations.
- [Public evidence table](public-source-evidence.csv): billing-notice, minute, example-bill and draft-scope qualifications to check before any quantitative request exhibit is shared.

The local-only viewer is `data/interim/source-review/index.html` under this checkout. It shows the seven accounting pages with source/hash/page labels, original-PDF links and the pending checklist. It is intentionally ignored by Git and is not a public GitHub link. The reviewer should open the original PDF as well as the displayed accounting page; surrounding wording and report coverage matter. The viewer does not record a signature or change verification status.

## Required review record

1. Record the reviewer identifier, local review date, relationship to the project and review type. Use `independent_human` only when a person independent of the AI extraction actually performs the checks. A same-author human check should be described accurately rather than called independent. Keep identifying notes locally unless their publication is approved.
2. Confirm the file's SHA256 and inspect the exact physical PDF page (1-based). Do not replace the pinned file with a fresh download or rely on extracted text alone. Note a changed or unavailable source rather than silently substituting it.
3. Check annual production, reported daily production, billed figure, unaccounted percentage and displayed precision. Check units and daily wording. Separate water-quality coverage, explicit production dates and unknown billing coverage.
4. Prioritize 2020's printed percentage and denominator alternatives; 2021's small annual/daily production difference and unconfirmed precision; 2022's percentage and repeated billed value; 2023's contextual daily interpretation and absent exact production dates; and 2024/2025's unconfirmed billing and measurement coverage. See the checklist's year-specific prompts.
5. Enter corrections or an exact review-memo reference. A signed/dated local memo should identify the inspected hashes/pages, findings and any unresolved qualifications. File hashes establish identity; they do not establish that the content was reviewed.
6. Mark a row `human_verified` only after a documented person's review. Record whether that review was independent separately. Any transcription correction must update the source/claim records and regenerate downstream reports without overwriting the original PDF. Do not remove accounting-coverage qualifications merely because the printed numbers match.

Before an external exhibit is attached, integrate documented corrections and review the regenerated table/chart and adjacent request text. Departmental period/boundary confirmation is a separate gate from human transcription verification. No review completion, signature or request dispatch is implied by this handoff.
