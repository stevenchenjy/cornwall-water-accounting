# Setup preflight — water accounting

Generated at 2026-10-20T01:15:13.920928+00:00.

This is a bootstrap diagnostic, not the completed study or a leakage estimate.

Sources: [source register](../research/source-register.csv), [retrieval timestamps and SHA256 receipts](../data/manifests/retrievals.csv), and [source observations with physical PDF pages](../data/seed/annual-water.csv).

| Reporting year | Snapshot | Observation status | Days | Derived annual billed (gal) | Derived unaccounted (%) | Difference from report (pp) |
|---|---|---|---:|---:|---:|---:|
| 2019 | downloaded | pending extraction | 365 | — | — | — |
| 2020 | downloaded | pending extraction | 366 | — | — | — |
| 2021 | downloaded | pending extraction | 365 | — | — | — |
| 2022 | downloaded | pending extraction | 365 | — | — | — |
| 2023 | downloaded | pending extraction | 365 | — | — | — |
| 2024 | downloaded | source_text_checked | 366 | 228,808,194 | 19.2600 | +0.0000 |
| 2025 | downloaded | source_text_checked | 365 | 193,898,585 | 33.2501 | +0.0001 |

Annual billed values above are daily billed values × calendar days. They are derived estimates, not annual billing ledger totals.
The 2024 denominator is 366 days. An integer daily billed figure implies annual rounding half-width ±183 gal (2024) or ±182.5 gal (2025), assuming rounding to nearest gallon.
The percentage check is a calculation-consistency diagnostic; a pass does not establish matching production and billing periods.

## Remaining work

- Extract and independently verify 2019–2023 observations; blank values are intentional.
- Independently verify the 2024/2025 seed rows against the original PDF, physical page 2.
- Confirm service boundary, monthly ledger periods and components of unaccounted water.
- Evaluate the billing-change lead and other alternatives after a consistent series exists.
- No causal explanation, leakage total or department endorsement is established.
