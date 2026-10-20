# Analysis plan — draft, before substantive research

1. Retrieve seven reports and preserve originals, URLs, SHA256 hashes and retrieval times. Record each cover's reporting year, data-period dates and PWS ID.
2. Transcribe and cross-check annual production, reported daily production, reported daily billed consumption and reported unaccounted-water percentage. Automatic text extraction is only an aid; physical PDF pages start at 1. The 2024/2025 seed rows have been checked against source text but still require independent human verification.
3. Let `d` be 365 or 366 for the calendar year. Calculate `P/d`, `B_daily*d`, `P-B_daily*d` and `100*(P-B_daily*d)/P`. Annual billed volume inferred from a rounded daily average is not an observed annual billing-ledger total.
4. Also retain calculations using the reported daily-production denominator. If daily billed consumption was rounded to an integer, the inferred annual rounding interval is ±d/2 gallons. Reported percentages have 0.01 percentage-point precision. The code uses an explicit 0.05 pp diagnostic threshold; a pass does not establish matching accounting periods.
5. Unaccounted water includes firefighting, street/sewer cleaning, unmetered municipal use and possible losses. Do not equate the entire residual with leakage or automatically equate it with a standard audit definition of non-revenue water.
6. Record event dates, sources and testable mechanisms. A change in bill-issuance dates does not prove the same change in meter-reading dates or annual reporting periods. Ask the department to confirm.
7. Compare absolute, percentage and percentage-point changes between 2024 and 2025 using descriptive analysis. If monthly data is later obtained, document an amended plan before examining seasonality or billing lag.
8. Have an independent reviewer check calendars, definitions, boundaries, alternative explanations and provenance. Disclose AI assistance, limitations and unresolved items in the final brief.
