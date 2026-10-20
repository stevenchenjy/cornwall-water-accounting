# Data lifecycle

`seed/annual-water.csv` contains reported quantities with exact source SHA256 and physical pages. Production coverage, report testing coverage, billing coverage and the denominator are separate. `schema/` defines fields; `manifests/` records retrievals. Derived values belong in `reports/`.

Raw/interim/processed/restricted directories are local-only and ignored. Never force-add them. Snapshots are immutable; a new retrieval makes a new timestamped file. A hash proves file integrity, not independent human verification.

`make preflight` can audit the versioned observations and pinned receipts without original files; it explicitly records missing originals and checks byte hashes when present. `make fetch` downloads new snapshots but does not change an observation's inspected hash. A changed source requires an explicit new inspection and observation revision. `make extract` aids checking; complex 2019 text requires Poppler. `make chart` regenerates the comparison using the locked optional plotting dependencies.

Only aggregate outputs without household identifiers belong in this public repository. AI inspection is labeled; independent human and departmental verification remain pending.

The [public-source evidence table](../research/public-source-evidence.csv) pins the follow-up notices, examples and minutes. Two manifest entries are explicitly labeled captures: selected browser-rendered auto-captions and an AI archive-navigation observation. They are distinct from original downloaded HTML/PDF bytes; their `content_type` and audit notes record the capture method. They are not full video bytes, a full transcript, a municipal directory export or independent verification. Only the underlying network documents appear in the fetchable source register.

`data/interim/source-review/index.html` is a local-only human-review aid containing accounting-page renders and links to the pinned original PDFs. Its index/capture artifacts remain ignored. No household identifiers, sample-bill names/addresses/account identifiers or source-page images have been copied into the public research tables.
