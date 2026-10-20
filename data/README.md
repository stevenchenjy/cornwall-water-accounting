# Data lifecycle

`seed/annual-water.csv` contains reported quantities with exact source SHA256 and physical pages. Production coverage, report testing coverage, billing coverage and the denominator are separate. `schema/` defines fields; `manifests/` records retrievals. Derived values belong in `reports/`.

Raw/interim/processed/restricted directories are local-only and ignored. Never force-add them. Snapshots are immutable; a new retrieval makes a new timestamped file. A hash proves file integrity, not independent human verification.

`make preflight` can audit the versioned observations and pinned receipts without original files; it explicitly records missing originals and checks byte hashes when present. `make fetch` downloads new snapshots but does not change an observation's inspected hash. A changed source requires an explicit new inspection and observation revision. `make extract` aids checking; complex 2019 text requires Poppler. `make chart` regenerates the comparison using the locked optional plotting dependencies.

Only aggregate outputs without household identifiers belong in this public repository. AI inspection is labeled; independent human and departmental verification remain pending.
