# Evidence intake and next-analysis decision protocol

The question is whether the 2024 and 2025 reported accounts are comparable and how much change can be reconciled from records. This protocol governs the next analysis; it does not declare any evidence gate passed. The public-source audit, [evidence table](public-source-evidence.csv) and [bounded search](public-source-search-log.csv) leave actual billing coverage, calculation rules, annual scope and the complete written plan unresolved. The current bridge remains **42,005,609 inferred gallons of unexplained change under calendar-day annualization**, with no causal attribution or leakage estimate.

## Intake and minimum response

The [unsent correspondence](department-request.md), [technical attachment](questions-for-water-department.md) and [request register](accounting-evidence-requests.csv) make R01-R03 the first accounting bottleneck, R04 the existing-work check and R05 a focused historical clarification. Monthly/native-cycle records (R06) and use/measurement records (R07) are conditional follow-ups. No request has been sent or accounting response received.

1. Complete the person's [source-review record](source-review-guide.md) before releasing quantitative exhibits. Keep all seven checklist rows pending until that review occurs; AI review is a separate record.
2. After authorized contact, preserve each received original unchanged in ignored local storage. Record request ID, sender/source, received timestamp, SHA256/byte count, version, publication restrictions, exact page/table/cell, applicable dates, units and account/meter scope. Label reported, derived, assumed and reviewer-confirmed fields separately. Private correspondence and row-level records are not public by default.
3. Record a response to every requested definition as supported, contradicted or unresolved, with the exact evidence reference and the reviewer/date. An unavailable worksheet, absent adjustment log or silence is missing evidence, not a zero or confirmation. A partial response resolves only its supported claims.
4. Reproduce both annual worksheets before explaining their difference. Preserve the seven printed observations. Put corrected inputs or direct ledger observations in a separately identified revision; record every change from the public-report baseline. Check the existing plan for an earlier explanation and its actual data period rather than assuming it covers 2024/2025.

## Comparability acceptance

All conditions below require substantive review of exact records. A reference string, PWS match, executed agreement, compatible percentage or passing test alone is insufficient.

| Gate | Required evidence and acceptance test | If absent or inconsistent |
|---|---|---|
| C1 - identity and units | Dated/source-identified worksheets belong to the intended NY3503526 accounting system; production, billed and percentage units and all conversions are explicit. | Retain unresolved identity/unit status; do not combine totals. |
| C2 - production period | Actual production start/end, meter/source aggregation and corrections reproduce the annual production figure, or document a revision. | Keep report testing coverage separate; do not infer production dates from a cover year. |
| C3 - billed volume and denominator | Actual billed usage coverage, reading/issuance dates, year assignment, source total or averaging formula, and the actual denominator are documented for each year. Reproduce the billed figure and its precision from those inputs. | Keep calendar-day annualization as a scenario. Do not substitute a notice, sample bill, reading date alone or assumed 60-day cycle. |
| C4 - common scope | Year-specific included account/customer/wholesale groups and production-meter chain align. Transfers, exports/imports or scope changes are either absent by documented check or bridged with volumes on a declared common boundary. | No comparability claim based only on municipal names or an unsigned/current agreement. |
| C5 - arithmetic and adjustment closure | Formulas, rounding, estimates/corrections and any year-boundary allocations reproduce printed figures within **documented** precision, or trace an explicit correction. The adjustment register sums to independently checked revised totals with no duplicate volumes. | Report the exact discrepancy and uncertainty; the 0.05 pp heuristic is not an acceptance tolerance. |
| C6 - review and cross-year consistency | A documented person validates source transcription; the analyst and methods reviewer check C1-C5, the same accounting definition across years, and production/billing period alignment within each year. Calendar years have 366 days in 2024 and 365 in 2025. | State which documentary/human gate remains open; no blanket confirmed label. |

Classify the result as **source accounts comparable**, **comparable only after documented reconstruction**, or **unresolved**. Reconstruction must name the common period/scope, every transformation and remaining uncertainty; it does not retroactively make the printed inputs comparable. A worksheet method change can be documented even when the old daily-average interpretation cannot be reproduced.

Use a direct observed annual billed total when provided and supported. If only a daily statistic exists, multiply only under its documented construction and denominator, retaining its rounding interval. Do not invent a ledger total. The current `reconcile()` function's `comparability_established` flag checks only a particular daily-average method's period/denominator, scope-status and reference-presence conditions. It can be true while a percentage is incompatible or billed volume exceeds production; it does not certify C5 arithmetic, C6 human review or documentary truth. It is not a general ledger importer. A valid alternative formula or direct ledger response needs a separately reviewed calculation path. Do not force it into this function or change a status merely to obtain `comparability_established=True`.

## Tests of the proposed explanations

These are record tests, not a causal model or ranked explanations. They apply the [hypothesis register](hypothesis-evidence.csv); evidence of a schedule or asset event without an attributable volume establishes context only.

| Hypothesis | Record-supported signature | Evidence that weakens it / remaining qualification |
|---|---|---|
| H1 - billing coverage/cutoff | Actual transition/adjacent cycles and year-assignment rules yield a reproducible transfer into or out of 2024/2025. | Identical coverage and assignment after adjustment, with no material transfer in complete records; announced timing alone cannot quantify it. |
| H2 - denominator/formula | Worksheets show a changed denominator or formula and its recalculation accounts for a specific difference. | Same supported method/precision and aligned inputs in both years. Formula reconciliation is accounting evidence, not a physical water-use change. |
| H3 - corrections/estimates/omissions | Existing adjustment totals and estimate-to-actual history change the billed/production totals by supported amounts. | Complete relevant records show no material corrections. A missing log cannot weaken it; late-fee waivers are dollars, not gallons. |
| H4 - boundary/inclusion | Actual scope/inclusion and meter records identify changes and volumes needed to reconstruct the same boundary. | Documented stable inclusion and meter chain. An executed agreement without the included groups/meters is insufficient. |
| H5 - authorized unbilled use | Existing logs or defensible documented estimates support year-specific uses on the aligned period/scope. | Complete comparable logs show stable or insufficient use; unavailable uses stay unknown. |
| H6 - measurement | Calibration/replacement evidence and the affected meter totals support a signed correction with uncertainty. | Stable checked measurement or an effect too small to account for the change; a replacement date alone is insufficient. |
| H7 - physical losses | A remaining aligned balance plus independent loss/repair/measurement evidence supports a particular physical-loss claim after recorded uses and accounting differences are considered. | An accounting reconciliation explains the apparent change; otherwise an unresolved remainder alone still does not identify leakage. |

## Adjustment bookkeeping and bridge

Keep one local adjustment register with: unique event ID, request/hypothesis reference, evidence hash and page/cell, affected year, usage/reading/issuance period, scope, P or B side, signed gallons, conversion/calculation, precision/uncertainty, parent/transfer ID, reviewer and status. Only supported, reviewed amounts enter the numeric bridge. Proposed or unquantified entries stay unknown and cannot be summed as zero.

Let `P0_y` be printed production and `B0_y` the current conditional daily-rate × calendar-days baseline. For each supported basis/scope/correction event record additions to production as `cP_y` and additions to billed volume as `cB_y`; negative values remove volume. Then:

```text
P*_y = P0_y + sum(cP_y)
B*_y = B0_y + sum(cB_y)
R*_y = P*_y - B*_y
D* = R*_2025 - R*_2024
   = 42,005,609 + sum(cP_2025 - cP_2024) - sum(cB_2025 - cB_2024)
E_i = (cB_i,2025 - cB_i,2024) - (cP_i,2025 - cP_i,2024)
D* = 42,005,609 - sum(E_i)
```

`E_i` is a signed accounting contribution to the starting conditional difference; a negative contribution increases it. The 42,005,609 starting value remains conditional. No actual `cP`, `cB` or `E` amount has been established. Supported zero adjustments require a complete scope-specific check; missing adjustments remain unknown even when the arithmetic display carries only supported entries. An added billed volume lowers that year's residual; added production raises it. A reallocation across years has linked opposite entries and conserves event volume, although its effect on the year-to-year difference can be twice the transferred volume.

Use either an aggregate basis-replacement entry (for example, observed annual B minus conditional B0) **or** disjoint detailed entries that sum to it. Mark the alternative parent/details as reconciliation-only and do not book both. A transition correction already included in a corrected worksheet cannot be booked again. Group the same atomic volume under one event even if H1/H2/H3 all describe it. Reconcile transfers on both sides/years, keep wholesale transfers internal or external consistently, and check conservation, units, signs and totals against the source. Do not net unrelated or unknown corrections to make the remainder vanish. Carry documented precision and correlated uncertainty; do not assume independent errors to narrow an interval.

Authorized unbilled use is a **composition of the aligned residual**, not a billed-volume correction. If supported, show `R*_y = U_y + remaining_y` separately, with `U` on the same period/scope and counted once. Do not book it as `cB` or subtract it twice. `remaining_y` still includes possible measurement/apparent errors and physical losses; it is not a leakage estimate. The rate/calendar decomposition in the public bridge is arithmetic and must not also be booked as an explanatory adjustment.

## Advance, limit or close

For intake triage, a material gap is one that exceeds documented input precision or could change the comparability classification or stated reporting decision. Record the chosen criterion and its evidence before attributing adjustments. No arbitrary gallon threshold or the existing 0.05 pp diagnostic heuristic establishes materiality.

| Records available | Defensible next output | Stop/limit |
|---|---|---|
| C1-C6 supported; worksheets suffice | Reproduced or corrected accounts, a signed accounting bridge, uncertainty and the department's stated reporting use if supplied. | No physical-loss attribution without separate H7 evidence. No monthly export needed when existing records answer the question. |
| Definitions or partial totals only | Revise only supported assumptions; report bounded calculations if the bounds themselves have evidence. Identify exactly which period/scope or adjustment remains missing. | No extrapolated annual ledger, assumed zero use or causal interpretation. Seek only the R06/R07 item needed for that gap, after authorization. |
| Complete useful response unavailable, declined, or still insufficient after a focused clarification | Close this stage as a public-report comparability audit, with dated search/intake coverage, open C gates, conditional bridge and retained historical qualifications. | Do not manufacture reconciliation or keep expanding searches/engineering. Reopen only when a specific new record or authorized response could change a gate. |

Do not initiate contact to satisfy the stopping rule. Until a user-authorized request is sent, describe the current endpoint as **bounded public-source work complete; external evidence pending**. Missing coverage, denominator, scope, adjustments or authorized-use/measurement evidence prevents causal interpretation. Even a complete accounting explanation is not a causal estimate of leakage, policy effectiveness or infrastructure performance. Seven annual observations support descriptive accounting only; external operational recommendations remain gated on validated evidence and a documented departmental decision need.
