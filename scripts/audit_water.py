import csv
import json
import sys
from _common import ROOT, utc_now, latest_receipts
sys.path.insert(0, str(ROOT / 'src'))
from water_accounting import reconcile

def number(v):
    return float(v) if str(v).strip() else None

def main():
    with (ROOT / 'data/seed/annual-water.csv').open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    receipts = latest_receipts()
    audits = []
    lines = ['# Setup preflight — water accounting', '', f'Generated at {utc_now()}.', '',
                 'This is a bootstrap diagnostic, not the completed study or a leakage estimate.', '',
                 'Sources: [source register](../research/source-register.csv), [retrieval timestamps and SHA256 receipts](../data/manifests/retrievals.csv), and [source observations with physical PDF pages](../data/seed/annual-water.csv).', '',
             '| Reporting year | Snapshot | Observation status | Days | Derived annual billed (gal) | Derived unaccounted (%) | Difference from report (pp) |',
             '|---|---|---|---:|---:|---:|---:|']
    for row in rows:
        year = int(row['reporting_year'])
        result = reconcile(year, number(row['produced_gal']), number(row['reported_daily_billed_gal']),
                           number(row['reported_unaccounted_pct']), number(row['reported_daily_produced_gal']))
        audits.append({'reporting_year': year, 'source_id': row['source_id'], 'observation_status': row['verification_status'], **result})
        snapshot = 'downloaded' if row['source_id'] in receipts else 'not downloaded'
        if result['status'] == 'missing_observation':
            lines.append(f"| {year} | {snapshot} | pending extraction | {result['days']} | — | — | — |")
        else:
            lines.append(f"| {year} | {snapshot} | {row['verification_status']} | {result['days']} | {result['derived_annual_billed_gal']:,.0f} | {result['derived_unaccounted_pct']:.4f} | {result['difference_from_reported_pp']:+.4f} |")
    lines += ['', 'Annual billed values above are daily billed values × calendar days. They are derived estimates, not annual billing ledger totals.',
              'The 2024 denominator is 366 days. An integer daily billed figure implies annual rounding half-width ±183 gal (2024) or ±182.5 gal (2025), assuming rounding to nearest gallon.',
              'The percentage check is a calculation-consistency diagnostic; a pass does not establish matching production and billing periods.', '',
              '## Remaining work', '',
              '- Extract and independently verify 2019–2023 observations; blank values are intentional.',
              '- Independently verify the 2024/2025 seed rows against the original PDF, physical page 2.',
              '- Confirm service boundary, monthly ledger periods and components of unaccounted water.',
              '- Evaluate the billing-change lead and other alternatives after a consistent series exists.',
              '- No causal explanation, leakage total or department endorsement is established.']
    (ROOT / 'reports/preflight.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    (ROOT / 'reports/preflight.json').write_text(json.dumps({'generated_at_utc':utc_now(),'stage':'bootstrap_diagnostic','annual_audits':audits}, indent=2)+'\n', encoding='utf-8')
    print('Created reports/preflight.md and preflight.json; 2019–2023 extraction remains pending.')

if __name__ == '__main__':
    main()
