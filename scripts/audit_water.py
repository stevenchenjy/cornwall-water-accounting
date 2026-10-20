"""Generate a pinned, period-explicit public-source audit and arithmetic bridge."""
import csv
import hashlib
import json
import sys
from _common import ROOT, utc_now, pinned_receipt
sys.path.insert(0, str(ROOT / 'src'))
from water_accounting import reconcile, billing_change_components


def number(v):
    return float(v) if str(v).strip() else None


def daily_production_summary(audits):
    """Build narrative from the same diagnostics used by the JSON/table."""
    flagged = [a for a in audits if a['daily_production_difference_gal'] is not None
               and abs(a['daily_production_difference_gal']) > .5]
    withheld = [str(a['reporting_year']) for a in audits if a['daily_production_difference_gal'] is None]
    parts = []
    for a in flagged:
        checks = '; '.join(f"nearest {c['annual_total_rounding_unit_gal']:,} gal: "
                          + ('compatible' if c['daily_production_compatible'] else 'incompatible')
                          for c in a['source_precision_sensitivity'])
        parts.append(f"{a['reporting_year']}: reported annual production / explicit period days = "
                     f"{float(a['produced_gal'])/a['production_period_days']:,.4f} gallons/day, "
                     f"versus {float(a['reported_daily_produced_gal']):,.0f} printed "
                     f"(difference {a['daily_production_difference_gal']:+.4f}). "
                     f"This exceeds the 0.5-gallon/day heuristic; {checks}.")
    passed = sum(a['daily_production_difference_gal'] is not None
                 and all(c['daily_production_compatible'] for c in a['source_precision_sensitivity']) for a in audits)
    parts.append(f'{passed} explicitly dated years are compatible under all tested production-precision scenarios.')
    if withheld:
        parts.append('Daily-production checks withheld for lack of explicit production dates: '+', '.join(withheld)+'.')
    parts.append('These are conditional precision qualifications, not established reporting errors.')
    return ' '.join(parts)


def main():
    with (ROOT / 'data/seed/annual-water.csv').open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    with (ROOT / 'data/manifests/retrievals.csv').open(newline='', encoding='utf-8') as stream:
        receipts = list(csv.DictReader(stream))
    audits = []
    for row in rows:
        receipt = pinned_receipt(row['source_id'], row['source_sha256'], receipts)
        original = ROOT / receipt['local_path']
        source_check = 'pinned_receipt_only_local_original_unavailable'
        if original.exists():
            if hashlib.sha256(original.read_bytes()).hexdigest() != row['source_sha256']:
                raise ValueError('Pinned source bytes do not match observation hash')
            source_check = 'local_original_hash_matches'
        kwargs = dict(
            billing_days=int(row['billing_denominator_days']) if row['billing_denominator_days'] else None,
            billing_denominator_status=row['billing_denominator_status'],
            production_start=row['production_start'], production_end=row['production_end'],
            billing_start=row['billing_coverage_start'], billing_end=row['billing_coverage_end'],
            boundary_status=row['measurement_boundary_status'],
            percentage_decimal_places=int(row['percentage_decimal_places']))
        inputs = (int(row['reporting_year']), number(row['produced_gal']),
                  number(row['reported_daily_billed_gal']), number(row['reported_unaccounted_pct']),
                  number(row['reported_daily_produced_gal']))
        result = reconcile(*inputs, **kwargs)
        sensitivity = []
        for unit in (1, 100, 1000):
            check = reconcile(*inputs, **kwargs, annual_production_rounding_half_width_gal=unit/2)
            sensitivity.append(dict(annual_total_rounding_unit_gal=unit,
                percentage_compatible=check['conditional_rounding_compatible'],
                implied_pct_interval=check['conditional_implied_pct_interval'],
                daily_production_compatible=check['conditional_daily_production_rounding_compatible']))
        result['source_precision_sensitivity'] = sensitivity
        audits.append({**row, 'source_url': receipt['requested_url'],
            'source_retrieved_at_utc': receipt['retrieved_at_utc'], 'source_integrity': source_check, **result})
    stamp = utc_now()
    payload = dict(generated_at_utc=stamp, stage='public_source_comparability_audit',
        rounding_assumption='Annual total nearest 1, 100 or 1000 gallons tested conditionally; daily values nearest 1 gallon and percentage nearest displayed unit. No convention confirmed.',
        independent_human_review='pending', annual_audits=audits)
    lines = ['# Annual water accounts: revised public-source audit', '', f'Generated {stamp}.', '',
        '**Result:** all seven accounting pages were checked against extracted text and rendered original PDFs by AI. No independent human verification or departmental confirmation is claimed. Production and billing comparability remains unestablished in every year.', '',
        'Source observations are [pinned to exact PDF hashes](../data/seed/annual-water.csv), with [retrieval receipts](../data/manifests/retrievals.csv). Pages below are physical PDF pages, starting at 1.', '',
        '| Year / PDF page | Reported production (gal) | Reported daily billed (gal/day) | Reported residual (%) | Calendar-day implied residual (%) | Difference (pp) | Percentage rounding compatible (1-gal annual scenario)? |',
        '|---|---:|---:|---:|---:|---:|---|']
    for a in audits:
        lines.append(f"| [{a['reporting_year']}, p. {a['physical_pdf_page']}]({a['source_url']}) | {float(a['produced_gal']):,.0f} | {float(a['reported_daily_billed_gal']):,.0f} | {a['reported_unaccounted_pct']} | {a['derived_unaccounted_pct']:.4f} | {a['difference_from_reported_pp']:+.4f} | {'yes' if a['conditional_rounding_compatible'] else 'NO'} |")
    lines += ['', '## What the table establishes', '',
        '- The 2020 report gives 36.6%, while the calendar-day calculation gives approximately 36.00%. The 2022 report gives 13.15%, while the same calculation gives approximately 12.78%. These differences exceed conditional rounding intervals and the separately retained 0.05 pp diagnostic heuristic. They require clarification; they do not identify which input or definition is responsible.',
        '- The 2021 and 2022 reports print the same daily billed volume, 635,063 gallons/day. Repetition alone does not establish a copying error.',
        '- The other five years have compatible unaccounted percentages under all three tested annual-total precision scenarios. This percentage result does not mean every daily-production check passes or that billing periods and boundaries align.',
        '- The 2023 billed figure has a contextual daily interpretation. Its production paragraph identifies the year without explicit start/end dates. The exact production dates remain empty in the source table.', '',
        '## Periods and precision', '',
        'Water-quality testing coverage, production coverage, billing-volume coverage and the daily-billing denominator have separate fields. Billing coverage and customer/measurement boundaries are unconfirmed for all seven rows. The 365/366 billing denominators are explicit analytical assumptions. ' + daily_production_summary(audits), '',

        'Inferred annual billing = printed daily billed volume × assumed calendar days. It is not an observed annual ledger total. Conditional rounding uses ±0.5 gallon/day and half the displayed percentage unit (0.05 pp in 2019–2020; 0.005 pp in 2021–2025). Annual-production half-widths of ±0.5, ±50 and ±500 gallons are tested separately. Trailing zeros do not establish a rounding rule; all scenarios remain unconfirmed. The 2020 and 2022 percentage discrepancies survive all three scenarios.', '',
        'The 0.05 pp difference threshold remains a labeled diagnostic heuristic and does not replace the precision-aware overlap check. Neither check estimates physical leakage. Unaccounted water includes authorized unbilled uses and possible losses.', '',
        '## Next decision', '',
        'Review this table and the [2024–2025 bridge](reconciliation-bridge.md) before any final brief. Ask first for the 2024/2025 calculation worksheets, billing periods/denominators, adjustments, system boundary and existing Water Master Plan analysis. Keep 2020/2022 as targeted historical clarification items. See the [draft request](../research/questions-for-water-department.md) and [hypothesis matrix](../research/hypothesis-evidence.csv).', '',
        'If those records are unavailable, the defensible endpoint is a public-report comparability audit with an unresolved change. A causal explanation remains outside the available evidence.']
    lines += ['', '## Source-precision sensitivity', '', '| Year | Nearest 1 gal: percentage / daily production | Nearest 100 gal | Nearest 1000 gal |', '|---|---|---|---|']
    for a in audits:
        cells=[]
        for check in a['source_precision_sensitivity']:
            pct='compatible' if check['percentage_compatible'] else 'incompatible'
            daily='withheld' if check['daily_production_compatible'] is None else ('compatible' if check['daily_production_compatible'] else 'incompatible')
            cells.append(pct+' / '+daily)
        lines.append('| '+a['reporting_year']+' | '+' | '.join(cells)+' |')
    y2020=next(a for a in audits if a['reporting_year']=='2020')
    leap_check=reconcile(2020, float(y2020['produced_gal']), float(y2020['reported_daily_billed_gal']), 36.6, billing_days=365, billing_denominator_status='assumed_365_day_sensitivity', percentage_decimal_places=1, annual_production_rounding_half_width_gal=500)
    payload['2020_365_day_sensitivity']=leap_check
    lines += ['', f"For 2020, using 365 rather than 366 billed days yields {leap_check['derived_unaccounted_pct']:.4f}%, still incompatible with 36.6% even under ±500-gallon annual-production precision. An ordinary one-day annualization change alone is insufficient.", '', 'Confirmation statuses require traceable departmental documents. The code also requires billing-coverage, denominator and boundary reference fields before returning comparability established; references still require substantive human validation. No such confirmations have been supplied. The 2023 daily billed interpretation remains contextual and is not a verified comparable trend observation.', '', 'The [public-source follow-up](../research/public-source-audit.md) records the shortened transition-period announcement, a billing-schedule/late-fee resolution and existing Master Plan discussion. It supplies no actual reading dates, annual-volume adjustment or confirmed boundary; the calculations above remain conditional.', '', 'Next-stage handoff: [independent source-review guide](../research/source-review-guide.md), [checklist](../research/source-review-checklist.csv), [departmental request draft](../research/department-request.md), and [data-intake plan](../research/data-intake-plan.md).']
    (ROOT / 'reports/annual-audit.md').write_text('\n'.join(lines)+'\n')
    (ROOT / 'reports/annual-audit.json').write_text(json.dumps(payload,indent=2)+'\n')
    fields=['reporting_year','source_sha256','physical_pdf_page','produced_gal','reported_daily_billed_gal','reported_unaccounted_pct','billing_denominator_days','billing_denominator_status','derived_annual_billed_gal','derived_unaccounted_gal','derived_unaccounted_pct','difference_from_reported_pp','conditional_rounding_compatible','daily_production_difference_gal','conditional_daily_production_rounding_compatible','comparability_established']
    with (ROOT / 'reports/annual-audit.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore',lineterminator='\n');writer.writeheader();writer.writerows(audits)
    a,b = [next(x for x in audits if x['reporting_year']==str(y)) for y in (2024,2025)]
    delta_p=float(b['produced_gal'])-float(a['produced_gal'])
    delta_b=b['derived_annual_billed_gal']-a['derived_annual_billed_gal']
    delta_r=b['derived_unaccounted_gal']-a['derived_unaccounted_gal']
    pct_change=float(b['reported_unaccounted_pct'])-float(a['reported_unaccounted_pct'])
    billing_components=billing_change_components(float(a['reported_daily_billed_gal']), int(a['billing_denominator_days']), float(b['reported_daily_billed_gal']), int(b['billing_denominator_days']), common_days=365)
    bridge=dict(generated_at_utc=stamp, basis='explicit_calendar_day_assumption_unconfirmed_billing_coverage',
        reported_percentage_change_pp=pct_change, production_change_gal=delta_p,
        inferred_annual_billed_change_gal=delta_b, inferred_residual_change_gal=delta_r,
        documented_causal_adjustments_gal=None, unexplained_conditional_residual_change_gal=delta_r,
        inferred_billing_decrease_components=billing_components,
        interpretation='Arithmetic decomposition only; no volume has been attributed to a documented causal explanation.')
    bridge_lines=['# 2024–2025 reconciliation bridge', '',
        f'The reported residual rises from 19.26% to 33.25%: **{pct_change:.2f} percentage points**. Production increases **{100*delta_p/float(a["produced_gal"]):.2f}%**; reported daily billed volume falls **{100*(1-float(b["reported_daily_billed_gal"])/float(a["reported_daily_billed_gal"])):.2f}%**.', '',
        '| Arithmetic bridge, under calendar-day billing assumption | Gallons |', '|---|---:|',
        f'| 2024 inferred residual | {a["derived_unaccounted_gal"]:,.0f} |',
        f'| Add reported production change | +{delta_p:,.0f} |',
        f'| Subtract inferred billed-volume change ({delta_b:,.0f} gal) | +{-delta_b:,.0f} |',
        f'| 2025 inferred residual | {b["derived_unaccounted_gal"]:,.0f} |',
        f'| Unexplained change in the conditionally calculated residual | {delta_r:,.0f} |', '',
        'The inferred billing decrease has two arithmetic components:', '',
        '| Component of inferred annual billing decrease | Gallons |', '|---|---:|',
        f"| Change in printed daily billed rates over a common 365 days | {billing_components['daily_rate_component_gal']:,.0f} |",
        f"| Extra 2024 calendar day at its printed daily billed rate | {billing_components['calendar_component_gal']:,.0f} |",
        f"| Total inferred billing decrease | {billing_components['total_decrease_gal']:,.0f} |", '',
        f'The inferred annual billed volumes are {a["derived_annual_billed_gal"]:,.0f} and {b["derived_annual_billed_gal"]:,.0f} gallons, using 366 and 365 days respectively. Annual inferred billing therefore changes by {100*delta_b/a["derived_annual_billed_gal"]:.2f}%, which differs from the daily billed percentage change.', '',
        '## Explanatory bridge', '',
        '| Potential documented component | Amount attributable so far | Evidence required |', '|---|---|---|',
        '| Period/cutoff reassignment | Unknown | Native bill-cycle coverage and adjacent year-boundary cycles |',
        '| Corrections, estimates or omitted accounts | Unknown | Calculation worksheets and adjustment totals |',
        '| Customer/measurement boundary change | Unknown | Consistent boundary and included-account definitions |',
        '| Authorized unbilled use or measurement changes | Unknown | Recorded uses, meter calibration and reconciliation records |',
        f'| Unexplained change in the conditionally calculated residual | {delta_r:,.0f} inferred gal | None of the components above has yet been documented |', '',
        'Unknown amounts are not zero. This unexplained change is conditional on annualization; physical losses, authorized unbilled uses, measurement differences and timing adjustments remain possible components. It is not a measured loss. No amount is attributed to leakage or the July 2024 billing transition.', '',
        'The [public-source follow-up](../research/public-source-audit.md) documents a shortened transition-period announcement and a board resolution about overlapping billing schedules and late fees. These records do not quantify a volume adjustment. Monetary late-fee waivers cannot be counted as gallon adjustments.', '',
        '**Stopping gate:** obtain focused departmental records and test the [alternative explanations](../research/hypothesis-evidence.csv). If unavailable, publish this unresolved bridge as part of a public-report comparability audit. Expand to monthly/native-cycle reconciliation only after the initial worksheets and definitions are assessed.', '',
        'Source figures and pinned provenance: [annual audit](annual-audit.md).']
    (ROOT / 'reports/reconciliation-bridge.md').write_text('\n'.join(bridge_lines)+'\n')
    (ROOT / 'reports/reconciliation-bridge.json').write_text(json.dumps(bridge,indent=2)+'\n')
    (ROOT / 'reports/preflight.md').write_text('# Water accounting entry point\n\nThe setup diagnostic has been superseded by the [seven-year public-source audit](annual-audit.md) and [2024–2025 reconciliation bridge](reconciliation-bridge.md).\n\nAll seven accounting pages have AI text and visual checks. Independent human review and departmental period/boundary confirmation remain pending.\n')
    (ROOT / 'reports/preflight.json').write_text(json.dumps({'stage':'superseded','current_report':'reports/annual-audit.json'},indent=2)+'\n')
    print(f'Generated precision-sensitive audit and bridge; unexplained conditional residual change {delta_r:,.0f} gal.')

if __name__ == '__main__':
    main()
