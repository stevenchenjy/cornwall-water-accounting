# Early methods self-review — October 19, 2026

Reviewer: the same AI session that prepared the table and code. This is an inline self-review, not independent human or independent-agent verification. The source checks inspected rendered original accounting pages and extracted text for all seven PDFs; cover identifiers were also checked in extracted text. Exact source hashes/pages are in the seed table, with retrieval timestamps in the receipts.

| Check | Result | Remaining limit |
|---|---|---|
| Seven reported production/daily production/daily billed/percentage values | Matched transcribed values to accounting-page text and images | A person has not independently rechecked them |
| Exact snapshot binding | Observation joins require source ID + inspected SHA256; byte hash checked if original available | Fresh downloads never silently replace inspected observations |
| Period comparability | Report, production, billing coverage and denominator separated; unknown dates remain empty | No year's billing coverage/boundary is confirmed |
| Rounding and calendars | Explicit 365/366 scenarios; one versus two percentage decimals; 2020/2022 flagged | Nearest-unit rounding is conditional, not confirmed practice |
| 2024–2025 bridge | Production + inferred billing changes sum to inferred residual change | No documented explanatory adjustment is available |
| Alternative explanations | Seven-row hypothesis matrix and narrowed request prepared | July issuance notice does not establish a billing mechanism |
| Existing work | Official environment narrative and preliminary Master Plan meeting checked | Full plan/accounting scope and departmental use unresolved |

Regression tests cover missing versus zero, omitted denominator, mismatched periods, leap years, conditional rounding, excess billing and pinned provenance. The annual chart was rendered and visually inspected. These checks support the first public-source artifact; they do not replace independent review or authorize causal claims.

Next review should independently inspect original pages, resolve the contextual 2023 billed basis and examine the requested departmental worksheets. If unavailable, retain the public-audit endpoint and unresolved bridge.

## Second-review correction - October 20, 2026

The external ChatGPT review reproduced a +0.6301 gallon/day 2021 warning overlooked by the first narrative. This session reproduced it and replaced the static claim with data-driven reporting, tested annual-total precision scenarios (1/100/1000 gallons), retained the unresolved 2020/2022 results, added the 2020 365-day sensitivity, and decomposed inferred billing change. Confirmation references are required in addition to status fields. This remains AI methods review; the human checklist is pending.

## Public-source follow-up - October 20, 2026

The later [evidence table](../research/public-source-evidence.csv) corrects an incomplete description of the billing notice: it announces a shortened transition consumption period as well as issuance changes. July 2024 minute pages 7-8 provide a recorded schedule-overlap/late-fee resolution. The official 2023 presentation also includes historical water-loss discussion. These additions strengthen the documentary questions without supplying actual read dates, annual volume adjustments or confirmed boundaries. Example bills remain illustrative; public IMA versions remain unsigned. See the [follow-up and capture limits](../research/public-source-audit.md).

This extension is inline AI source verification and self-review. It does not complete the independent person/source-and-method review or alter the conditional bridge. The first dated review table above records the earlier review state; current evidence and unresolved gates are in the linked follow-up.

## Evidence-stage readiness and independent AI review - October 20, 2026

This is the enduring A1-A3 handoff. The lead revised existing artifacts rather than repeating the public search or adding runtime infrastructure. A1 now has a prioritized seven-page [human-review route](../research/source-review-guide.md). A2 has short [unsent correspondence](../research/department-request.md), a separate [technical attachment](../research/questions-for-water-department.md) and existing-format alternatives in [R01-R07](../research/accounting-evidence-requests.csv). A3 is the C1-C6 acceptance, H1-H7 record-test, adjustment and stopping [protocol](../research/data-intake-plan.md).

The lead checked all seven original receipt/hash/page/checklist/render bindings and visually inspected all seven accounting-page images. No transcription inconsistency was established. All human checklist rows remain pending. Raw PDFs and the optional local index are ignored; readiness in this checkout does not mean a remote reader has received the original packet. Browser rendering of the optional HTML index remains unverified; the original-PDF route is available.

One read-only `methods_reviewer` child agent independently reviewed the working packet against base commit `883fcae317f3ebba3eb04d6482a9e77f5d268da1`. Initial task `A1-A3-independent-methods-review-20261020T175924Z` was inspected at 17:59:24 UTC; bounded recheck `A1-A3-methods-recheck-20261020T180150Z` completed at `2026-10-20T18:01:50.769434+00:00`. The lead integrated this record; the reviewer edited no files. This is independent **AI artifact/methods review**, not independent human source verification, a signature or departmental acceptance. The reviewer visually sampled 2023, not all seven pages.

| Finding | Disposition and remaining limit |
|---|---|
| Moderate: `comparability_established` can be true despite an incompatible percentage or billed volume above production | Protocol now states that the flag checks only period/denominator/scope status/reference presence and cannot certify C5 arithmetic, C6 human review or documentary truth. Diagnostic code semantics are unchanged; no actual year is confirmed. Independent recheck: addressed. |
| Minor: the ignored viewer labeled the 2023 billed figure as a reported daily unit | Both the 2023 summary row and section now say the daily basis is contextual; the common column header is qualified. Original-page/source/seed values are unchanged. Independent recheck: addressed; browser rendering remains unverified. |

The reviewer reproduced 18 passing unit tests, all 39 receipt size/hash matches, seven source/checklist/page/render joins, 17 existing local HTML file references, and six synthetic sign/conservation countercases. The lead separately reproduced the conditional baseline and four synthetic sign/countercases. These synthetic amounts never entered the evidence or bridge. An added billed volume lowers a residual; a linked transfer across years conserves volume but can change the annual difference by twice that transfer. The reviewer accepted aggregate/detail exclusion, separate authorized-use composition, direct-ledger handling, hypothesis limits, request proportionality and the unresolved-result stopping rule. The recheck found no residual consequential issue within the two fixes.

### Reviewed snapshot receipts

The independent reviewer pinned these inputs; the intake and HTML hashes are the accepted recheck versions. These hashes identify the reviewed content, not a person's review or a departmental finding.

| Artifact | SHA256 |
|---|---|
| `research/source-review-guide.md` | `647b51076520cc60a351d68fcb7ab112e08d52d3ae304c84e3d7a569ab1947ae` |
| `research/source-review-checklist.csv` | `513b37f2d4941de245e2dc8aded3b0857bcced6d299f5d926f28d1236f733a8a` |
| `data/seed/annual-water.csv` | `da213ea96f4a4fadf7c11e052845a02567d6d9c2981cf9d222e5cf748d16576f` |
| `research/department-request.md` | `76f970dbbb6c756d2314699cab7fb4eed9eb07a76916248db64e9bdafcabd868` |
| `research/questions-for-water-department.md` | `1570030db734c8faea866a8fe3831f1becc1aaf331c800db261f64688d5a3731` |
| `research/accounting-evidence-requests.csv` | `52e92d716eecddcdbe9c02ee7c2046c9534b34bfa6021d070ece80e142a1c8e1` |
| `research/data-intake-plan.md` | `a5edc30be94cbc60a556403e4f2e6f2bd1453d4f8f88077856291d0028f7c022` |
| ignored `data/interim/source-review/index.html` | `a984355485a9ee6a88fd5bc905a108df1a96f2895228a029da6631127df6239d` |

### Findings and readiness

Verified at the AI/material level: exact source bindings, usable page images, correct protocol algebra, and the two addressed review findings. No new authoritative accounting record was available that closes a remaining definition/scope gate; the bounded public search was not repeated. Calendar-day arithmetic remains conditional: **42,005,609 inferred gallons of unexplained residual change**, with 2020/2022 discrepancies, 2021 precision and 2023 wording/date qualifications retained. Billing-transition, formula, correction, scope, authorized-use, measurement and physical-loss explanations remain hypotheses until their specified records support them.

| Stage | Verdict | Exact outstanding input |
|---|---|---|
| Independent human source review | Prepared and usable through the local original PDFs | A person's dated seven-row review identifying exact hashes/pages, relationship, findings and corrections; provide the ignored packet separately to an authorized reviewer. |
| Departmental intake | Request and acceptance protocol prepared; no intake/contact has occurred | User-approved sender/recipient/attachments and explicit transmission authorization; then R01-R03 worksheets/coverage/scope, accessible R04 plan/version and focused R05 clarification. |
| Explanatory analysis | Not ready; only descriptive conditional accounting is supported | C1-C6 documentary/human checks and any needed R06/R07 evidence, with supported adjustment amounts and uncertainty. |
| External recommendations | Operational, leakage and causal recommendations not ready | Validated comparable accounts, evidence appropriate to the specific claim and a documented departmental decision need. The present recommendation is to validate records. |

### Next three actions

| Order | Owner / dependency | Acceptance criteria |
|---|---|---|
| 1 | Independent person; user/lead provides the exact local source packet | Review all seven rows in guide order; record identity/relationship/date/hash/page and matched/corrected/unresolved fields. Lead integrates corrections and reruns relevant checks. No automatic `human_verified`. |
| 2 | User approves correspondence; authorized sender transmits only after that approval | Finalize sender, recipient and attachment scope. Use the separate technical request within the coordinated package; omit the numerical exhibit until human review is complete. Request existing records, accept partial replies and retain privacy/use restrictions. |
| 3 | Lead/accounting analyst with methods review; depends on an actual response | Pin records and decide each C gate; reproduce each year's account, book each supported volume once and classify comparable/reconstructed/unresolved. Seek only necessary conditional follow-up. If useful records remain unavailable after focused clarification, close with the unresolved public audit instead of extrapolating or claiming leakage. |

### Local verification and delivery boundaries

For this evidence-stage revision, `make check` passed all 18 tests, setup/TOML checks and the English check; `make chart` completed the preflight and plot generation. The fresh PNG was inspected; PNG bytes, normalized SVG geometry/text, seed observations and generated report content/numeric diagnostics matched the baseline. Earlier report/chart bytes were retained to avoid timestamp/ID-only changes. Local Markdown/CSV and ignored index bindings are checked separately from browser rendering. GitHub CI for base `883fcae` was observed successful in [Research checks run 39461648825](https://github.com/stevenchenjy/cornwall-water-accounting/actions/runs/39461648825); this is not a claim about a later commit. Final commit, remote HEAD and any later CI observation are recorded by the publication handoff. No department/resident contact, restricted-file publication or external record delivery occurred.
