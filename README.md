# Water Accounting and Unaccounted Water in the Cornwall-on-Hudson Water System, 2019–2025

Independent research workspace. Established October 19, 2026 (America/New_York).

Why did reported billed consumption and unaccounted water change substantially between 2024 and 2025 while total water production changed relatively little? First build a consistent 2019–2025 water account and identify records requiring reconciliation with the Water Department.

**Current stage: research preparation.** The workspace contains a reproducible starting point; the study and departmental validation remain pending.

Start with [START_HERE.md](START_HERE.md). See the [research brief](research/brief.md), [task board](research/TASKS.md), [agent roles](agents/README.md) and [initial data diagnostic](reports/preflight.md).

## Quick start

```sh
uv sync --locked
make check
make fetch
make preflight
```

`make fetch` saves local snapshots of public sources. `make preflight` generates a preparation-stage diagnostic. Raw files and record-level derivatives stay outside Git. After cloning, fetch the raw sources locally before running the diagnostic. Python 3.11 or later is required; resolved dependencies are recorded in `uv.lock`.

For page-numbered automatic text, run `make extract`. The extractor prefers Poppler `pdftotext` and otherwise falls back to pypdf. The complex 2019 PDF requires Poppler. If it is outside PATH, use `PDFTOTEXT=/absolute/path/to/pdftotext make extract`. Automatic extraction does not count as independent human verification.

## Workspace contents

- `.codex/agents/`: project-scoped Codex custom-agent definitions that inherit the parent's model and permissions.
- `research/`: scope, analysis plan, source and claim registers, tasks and decisions.
- `data/seed/`, `data/schema/`, `data/manifests/`: versioned seed observations, field definitions and retrieval receipts.
- `data/raw/`, `data/interim/`, `data/processed/`, `data/restricted/`: local-only originals and record-level working files.
- `src/`, `scripts/`, `tests/`: reproducible methods and checks for consequential accounting and inventory assumptions.
- `reports/`: reviewable aggregate outputs without household addresses or coordinates.

## Working language and research status

English is the required language for authored documents, agent instructions, reports, prompts and user-facing responses. `make check` includes a language regression check for authored workspace files. Original evidence remains immutable.

The intended user is the Cornwall-on-Hudson Water Department. Departmental cooperation and access to internal records have not been established. Future external reports must disclose AI assistance. Agents run only when invoked; no recurring monitor or background research task has been scheduled.
