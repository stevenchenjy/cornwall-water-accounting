# Annual water accounts: revised public-source audit

Generated 2026-10-20T15:06:15.466817+00:00.

**Result:** all seven accounting pages were checked against extracted text and rendered original PDFs by AI. No independent human verification or departmental confirmation is claimed. Production and billing comparability remains unestablished in every year.

Source observations are [pinned to exact PDF hashes](../data/seed/annual-water.csv), with [retrieval receipts](../data/manifests/retrievals.csv). Pages below are physical PDF pages, starting at 1.

| Year / PDF page | Reported production (gal) | Reported daily billed (gal/day) | Reported residual (%) | Calendar-day implied residual (%) | Difference (pp) | Percentage rounding compatible (1-gal annual scenario)? |
|---|---:|---:|---:|---:|---:|---|
| [2019, p. 5](https://gemgrp.com/eReports/CNNY000310Y20/docs/NY000310.pdf) | 276,677,000 | 552,595 | 27.1 | 27.1001 | +0.0001 | yes |
| [2020, p. 2](https://gemgrp.com/eReports/CNNY000310Y21/docs/NY000310.pdf) | 287,637,000 | 502,972 | 36.6 | 36.0000 | -0.6000 | NO |
| [2021, p. 7](https://cornwall-on-hudson.gov/Portals/1/2021_Annual_Water_Quality_Report.pdf) | 280,356,000 | 635,063 | 17.32 | 17.3201 | +0.0001 | yes |
| [2022, p. 2](https://cornwall-on-hudson.gov/Portals/1/2022_Annual_Water_Quality_Report.pdf) | 265,762,000 | 635,063 | 13.15 | 12.7799 | -0.3701 | NO |
| [2023, p. 7](https://cornwall-on-hudson.gov/Portals/1/2023%20Annual%20Water%20Quality%20Report.pdf) | 242,076,000 | 519,037 | 21.74 | 21.7401 | +0.0001 | yes |
| [2024, p. 2](https://cornwall-on-hudson.gov/Portals/1/2024%20Annual%20Water%20Quality%20Report.pdf) | 283,389,000 | 625,159 | 19.26 | 19.2600 | +0.0000 | yes |
| [2025, p. 2](https://cornwall-on-hudson.gov/Portals/1/Water/2025%20Annual%20Water%20Quality%20Report.pdf?ver=-Zx6vWbx8zC8TzWdNWYYoQ%3D%3D) | 290,485,000 | 531,229 | 33.25 | 33.2501 | +0.0001 | yes |

## What the table establishes

- The 2020 report gives 36.6%, while the calendar-day calculation gives approximately 36.00%. The 2022 report gives 13.15%, while the same calculation gives approximately 12.78%. These differences exceed conditional rounding intervals and the separately retained 0.05 pp diagnostic heuristic. They require clarification; they do not identify which input or definition is responsible.
- The 2021 and 2022 reports print the same daily billed volume, 635,063 gallons/day. Repetition alone does not establish a copying error.
- The other five years have compatible unaccounted percentages under all three tested annual-total precision scenarios. This percentage result does not mean every daily-production check passes or that billing periods and boundaries align.
- The 2023 billed figure has a contextual daily interpretation. Its production paragraph identifies the year without explicit start/end dates. The exact production dates remain empty in the source table.

## Periods and precision

Water-quality testing coverage, production coverage, billing-volume coverage and the daily-billing denominator have separate fields. Billing coverage and customer/measurement boundaries are unconfirmed for all seven rows. The 365/366 billing denominators are explicit analytical assumptions. 2021: reported annual production / explicit period days = 768,098.6301 gallons/day, versus 768,098 printed (difference +0.6301). This exceeds the 0.5-gallon/day heuristic; nearest 1 gal: incompatible; nearest 100 gal: compatible; nearest 1,000 gal: compatible. 5 explicitly dated years are compatible under all tested production-precision scenarios. Daily-production checks withheld for lack of explicit production dates: 2023. These are conditional precision qualifications, not established reporting errors.

Inferred annual billing = printed daily billed volume × assumed calendar days. It is not an observed annual ledger total. Conditional rounding uses ±0.5 gallon/day and half the displayed percentage unit (0.05 pp in 2019–2020; 0.005 pp in 2021–2025). Annual-production half-widths of ±0.5, ±50 and ±500 gallons are tested separately. Trailing zeros do not establish a rounding rule; all scenarios remain unconfirmed. The 2020 and 2022 percentage discrepancies survive all three scenarios.

The 0.05 pp difference threshold remains a labeled diagnostic heuristic and does not replace the precision-aware overlap check. Neither check estimates physical leakage. Unaccounted water includes authorized unbilled uses and possible losses.

## Next decision

Review this table and the [2024–2025 bridge](reconciliation-bridge.md) before any final brief. Ask first for the 2024/2025 calculation worksheets, billing periods/denominators, adjustments, system boundary and existing Water Master Plan analysis. Keep 2020/2022 as targeted historical clarification items. See the [draft request](../research/questions-for-water-department.md) and [hypothesis matrix](../research/hypothesis-evidence.csv).

If those records are unavailable, the defensible endpoint is a public-report comparability audit with an unresolved change. A causal explanation remains outside the available evidence.

## Source-precision sensitivity

| Year | Nearest 1 gal: percentage / daily production | Nearest 100 gal | Nearest 1000 gal |
|---|---|---|---|
| 2019 | compatible / compatible | compatible / compatible | compatible / compatible |
| 2020 | incompatible / compatible | incompatible / compatible | incompatible / compatible |
| 2021 | compatible / incompatible | compatible / compatible | compatible / compatible |
| 2022 | incompatible / compatible | incompatible / compatible | incompatible / compatible |
| 2023 | compatible / withheld | compatible / withheld | compatible / withheld |
| 2024 | compatible / compatible | compatible / compatible | compatible / compatible |
| 2025 | compatible / compatible | compatible / compatible | compatible / compatible |

For 2020, using 365 rather than 366 billed days yields 36.1748%, still incompatible with 36.6% even under ±500-gallon annual-production precision. An ordinary one-day annualization change alone is insufficient.

Confirmation statuses require traceable departmental documents. The code also requires billing-coverage, denominator and boundary reference fields before returning comparability established; references still require substantive human validation. No such confirmations have been supplied. The 2023 daily billed interpretation remains contextual and is not a verified comparable trend observation.

Next-stage handoff: [independent source-review checklist](../research/source-review-checklist.csv), [departmental request draft](../research/department-request.md), and [data-intake plan](../research/data-intake-plan.md).
