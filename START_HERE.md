# Start here

1. Read [AGENTS.md](AGENTS.md), [brief](research/brief.md) and [status](research/STATUS.md).
2. Inspect the [annual audit](reports/annual-audit.md), [source table](data/seed/annual-water.csv) and [bridge](reports/reconciliation-bridge.md).
3. Run `uv sync --locked` and `make check`; `make preflight` regenerates the aggregate audit.
4. Review the first table before drafting final conclusions. AI inspection is complete; independent human review and departmental accounting confirmation remain pending.

## Next research prompt

> Review the seven-year water table and 2024/2025 bridge. Challenge exact source hashes/pages, separated production and billing periods, explicit denominator assumptions, precision checks, 2020/2022 discrepancies and the contextual 2023 billed figure. Consult the hypothesis matrix and existing-work note. Record what was actually inspected and whether the review is independent. Keep the department request draft unsent until authorized. If internal data are unavailable, close this phase as a public-report comparability audit with an unresolved change. Use English throughout.

Do not expand agent/runtime setup or fit a causal model. Existing roles may be used inline; only spawn child agents with explicit delegation authorization.
