# Annual water table

| Field | Meaning / unit |
|---|---|
| reporting_year | Stated data/reporting year, not upload or publication year |
| period_start / period_end | Dates explicitly supported by the source; leave blank until checked |
| pws_id | Reported system identifier; do not infer it from a locality name |
| produced_gal | Reported annual water production, US gallons |
| reported_daily_produced_gal | Reported daily production, gallons/day |
| reported_daily_billed_gal | Reported daily billed consumption, gallons/day |
| reported_unaccounted_pct | Reported percentage in 0–100 units, not a decimal fraction |
| source_id / physical_pdf_page | Stable source-register identifier / physical PDF page, starting at 1 |
| verification_status | pending_extraction / source_text_checked / human_verified |
| derived_annual_billed_gal | Daily billed consumption × 365/366; an inferred value, not an observed annual total |

Empty numeric cells mean missing data and must not be replaced with zero. Join source hashes and retrieval times through `source_id` to `data/manifests/retrievals.csv`.
