.PHONY: setup check fetch extract preflight chart
setup:
	uv sync --locked
check:
	uv run python -m unittest discover -s tests -v
	uv run python scripts/validate_setup.py
	uv run python scripts/check_language.py
fetch:
	uv run python scripts/fetch_sources.py
extract:
	uv run python scripts/extract_report_text.py
preflight:
	uv run python scripts/audit_water.py
chart: preflight
	uv run --extra plots python scripts/plot_accounts.py
