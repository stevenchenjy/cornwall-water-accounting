# Annual water accounts: first public-source audit

Generated 2026-10-20T02:10:43.581428+00:00.

**Result:** all seven accounting pages were checked against extracted text and rendered original PDFs by AI. No independent human verification or departmental confirmation is claimed. Production and billing comparability remains unestablished in every year.

Source observations are [pinned to exact PDF hashes](../data/seed/annual-water.csv), with [retrieval receipts](../data/manifests/retrievals.csv). Pages below are physical PDF pages, starting at 1.

| Year / PDF page | Reported production (gal) | Reported daily billed (gal/day) | Reported residual (%) | Calendar-day implied residual (%) | Difference (pp) | Conditional rounding compatible? |
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
- The other five years are compatible with the conditional rounding check. Arithmetic compatibility does not establish aligned billing dates, measurement boundaries or an explanation.
- The 2023 billed figure has a contextual daily interpretation. Its production paragraph identifies the year without explicit start/end dates. The exact production dates remain empty in the source table.

## Periods and precision

Water-quality testing coverage, production coverage, billing-volume coverage and the daily-billing denominator have separate fields. Billing coverage and customer/measurement boundaries are unconfirmed for all seven rows. The 365/366 billing denominators are explicit analytical assumptions. Printed daily production agrees within half a gallon with annual production divided by the explicit production-period days for the six reports giving dates; the 2023 check is withheld for lack of explicit dates.

Inferred annual billing = printed daily billed volume × assumed calendar days. It is not an observed annual ledger total. Conditional rounding uses ±0.5 gallon/day, ±0.5 gallon for the printed annual total and half the displayed percentage unit (0.05 pp in 2019–2020; 0.005 pp in 2021–2025). These are hypothetical nearest-unit rules, not confirmed reporting practices.

The 0.05 pp difference threshold remains a labeled diagnostic heuristic and does not replace the precision-aware overlap check. Neither check estimates physical leakage. Unaccounted water includes authorized unbilled uses and possible losses.

## Next decision

Review this table and the [2024–2025 bridge](reconciliation-bridge.md) before any final brief. Ask first for the 2024/2025 calculation worksheets, billing periods/denominators, adjustments, system boundary and existing Water Master Plan analysis. Keep 2020/2022 as targeted historical clarification items. See the [draft request](../research/questions-for-water-department.md) and [hypothesis matrix](../research/hypothesis-evidence.csv).

If those records are unavailable, the defensible endpoint is a public-report comparability audit with an unresolved change. A causal explanation remains outside the available evidence.
