# Annual water observation dictionary

The versioned source table is [annual-water.csv](../data/seed/annual-water.csv). Derived results belong in [annual-audit.csv](../reports/annual-audit.csv).

| Fields | Meaning |
|---|---|
| reporting_year | Reported year, not publication/upload year |
| report_coverage_start / end / kind | Report's water-quality testing coverage; distinct from accounting coverage |
| production_start / end / period_status | Explicit production dates if printed; 2023 gives a year only and keeps exact dates empty |
| billing_coverage_start / end / status | Metered-usage/billed-volume coverage dates; all currently unconfirmed |
| billing_denominator_days / status | Explicit analytical denominator; currently 365/366 with `assumed_calendar_days`, not confirmed report practice |
| measurement_boundary_status | Whether matching customers, system and meter/account inclusion have been confirmed; currently unconfirmed |
| pws_id_reported | Identifier printed on cover; early reports omit the NY prefix; this is not a boundary history |
| produced_gal | Printed annual production, US gallons |
| reported_daily_produced_gal | Printed daily production, gallons/day |
| reported_daily_billed_gal / daily_billed_basis_status | Printed billed figure with daily-context qualification; 2023 is contextual |
| reported_unaccounted_pct / percentage_decimal_places | Printed percent in 0–100 units and number of displayed decimals |
| source_id + source_sha256 | Exact join to retrieval receipt; never join on source ID alone |
| physical_pdf_page | Accounting paragraph page, 1-based physical PDF page |
| verification_status | `ai_text_and_visual_checked` means AI checked extracted text and a rendered original page; independent human check remains pending |
| notes | Interpretation qualifications and provenance |

Empty is missing, never zero. Printed quantities remain distinct from derived annual billing and inferred residual. Conditional rounding assumes nearest integer gallons and the displayed percentage unit; departmental rounding practices remain unknown.
