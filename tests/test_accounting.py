from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from water_accounting import days_in_year, reconcile, period_days, billing_change_components
from _common import pinned_receipt
from audit_water import daily_production_summary


def calendar_scenario(year, *args, **kwargs):
    return reconcile(year, *args, billing_days=days_in_year(year),
                     billing_denominator_status='assumed_calendar_days', **kwargs)


class AccountingChecks(unittest.TestCase):
    def test_calendar_and_century_leap_years(self):
        self.assertEqual([days_in_year(y) for y in (2024,2025,1900,2000)], [366,365,365,366])
        self.assertEqual(period_days('2024-01-01','2024-12-31'),366)

    def test_2024_reconciliation_does_not_establish_comparability(self):
        result = calendar_scenario(2024,283389000,625159,19.26,774287)
        self.assertEqual(result['derived_annual_billed_gal'],625159*366)
        self.assertLess(abs(result['difference_from_reported_pp']),.01)
        self.assertTrue(result['conditional_rounding_compatible'])
        self.assertFalse(result['comparability_established'])
        self.assertIn('billing_coverage_unconfirmed',result['warnings'])
        self.assertIn('billing_denominator_assumed',result['warnings'])

    def test_no_implicit_annualization(self):
        result = reconcile(2024,283389000,625159,19.26)
        self.assertEqual(result['status'],'denominator_required')
        self.assertNotIn('derived_annual_billed_gal',result)

    def test_period_mismatch_detected_despite_matching_arithmetic(self):
        result = calendar_scenario(2024,283389000,625159,19.26,
            production_start='2024-01-01',production_end='2024-12-31',
            billing_start='2023-12-01',billing_end='2024-11-30')
        self.assertIn('production_billing_period_mismatch',result['warnings'])
        self.assertFalse(result['comparability_established'])

    def test_only_explicit_confirmations_allow_comparability(self):
        result = reconcile(2025,365000,900,10,billing_days=365,
            billing_denominator_status='department_confirmed',boundary_status='confirmed',
            confirmation_refs=dict(billing_coverage='synthetic-ledger',billing_denominator='synthetic-worksheet',measurement_boundary='synthetic-boundary'),
            production_start='2025-01-01',production_end='2025-12-31',
            billing_start='2025-01-01',billing_end='2025-12-31')
        self.assertTrue(result['comparability_established'])

    def test_confirmation_status_without_documents_cannot_establish_comparability(self):
        result=reconcile(2025,365000,900,10,billing_days=365,
            billing_denominator_status='department_confirmed',boundary_status='confirmed',
            production_start='2025-01-01',production_end='2025-12-31',
            billing_start='2025-01-01',billing_end='2025-12-31')
        self.assertFalse(result['comparability_established'])
        self.assertIn('department_confirmation_documentary_references_missing',result['warnings'])

    def test_2021_daily_precision_qualification(self):
        results=[calendar_scenario(2021,280356000,635063,17.32,768098,
                    production_start='2021-01-01',production_end='2021-12-31',
                    annual_production_rounding_half_width_gal=h) for h in (.5,50,500)]
        self.assertAlmostEqual(results[0]['daily_production_difference_gal'],.6301369863)
        self.assertEqual([r['conditional_daily_production_rounding_compatible'] for r in results],[False,True,True])

    def test_historical_discrepancies_survive_annual_nearest_thousand(self):
        for year,P,B,pct,precision in [(2020,287637000,502972,36.6,1),(2022,265762000,635063,13.15,2)]:
            self.assertFalse(calendar_scenario(year,P,B,pct,percentage_decimal_places=precision,
                annual_production_rounding_half_width_gal=500)['conditional_rounding_compatible'])
        counterfactual=reconcile(2020,287637000,502972,36.6,billing_days=365,
            billing_denominator_status='assumed_365_day_sensitivity',percentage_decimal_places=1,
            annual_production_rounding_half_width_gal=500)
        self.assertFalse(counterfactual['conditional_rounding_compatible'])
        self.assertAlmostEqual(counterfactual['derived_unaccounted_pct'],36.1748,places=4)

    def test_daily_narrative_follows_diagnostic_data_including_precision_warning(self):
        row=dict(reporting_year='2021',produced_gal='280356000',production_period_days=365,
                 reported_daily_produced_gal='768098',daily_production_difference_gal=.6301369863,
                 source_precision_sensitivity=[dict(annual_total_rounding_unit_gal=unit,
                    daily_production_compatible=unit!=1) for unit in (1,100,1000)])
        narrative=daily_production_summary([row])
        self.assertIn('2021:',narrative);self.assertIn('+0.6301',narrative)
        self.assertIn('nearest 1 gal: incompatible',narrative)
        self.assertIn('nearest 1,000 gal: compatible',narrative)
        row['reporting_year']='synthetic-future-year'
        self.assertIn('synthetic-future-year:',daily_production_summary([row]))

    def test_billing_bridge_decomposes_rate_and_calendar(self):
        result=billing_change_components(625159,366,531229,365,common_days=365)
        self.assertEqual(result['daily_rate_component_gal'],34284450)
        self.assertEqual(result['calendar_component_gal'],625159)
        self.assertEqual(result['total_decrease_gal'],34909609)
        self.assertEqual(result['daily_rate_component_gal']+result['calendar_component_gal'],result['total_decrease_gal'])

    def test_2020_and_2022_discrepancies_survive_display_precision(self):
        for year,P,B,pct,precision in [(2020,287637000,502972,36.6,1),(2022,265762000,635063,13.15,2)]:
            result=calendar_scenario(year,P,B,pct,percentage_decimal_places=precision)
            self.assertFalse(result['conditional_rounding_compatible'])
            self.assertIn('percentage_outside_conditional_rounding_interval',result['warnings'])

    def test_one_decimal_percentage_can_round_compatibly(self):
        self.assertTrue(calendar_scenario(2019,276677000,552595,27.1,percentage_decimal_places=1)['conditional_rounding_compatible'])

    def test_missing_is_not_zero(self):
        self.assertEqual(calendar_scenario(2025,None,0)['status'],'missing_observation')
        self.assertEqual(calendar_scenario(2025,365000,0)['derived_unaccounted_pct'],100)

    def test_excess_billed_is_not_clamped(self):
        result=calendar_scenario(2025,365000,1100)
        self.assertLess(result['derived_unaccounted_gal'],0)
        self.assertIn('inferred_billed_exceeds_production',result['warnings'])

    def test_percentage_units_and_invalid_period(self):
        with self.assertRaises(ValueError): calendar_scenario(2025,365000,900,125)
        with self.assertRaises(ValueError): period_days('2025-02-01','2025-01-01')

    def test_provenance_never_selects_latest_revision(self):
        receipts=[dict(source_id='s',sha256='inspected'),dict(source_id='s',sha256='newer')]
        self.assertEqual(pinned_receipt('s','inspected',receipts)['sha256'],'inspected')
        with self.assertRaises(ValueError): pinned_receipt('s','uninspected',receipts)

if __name__ == '__main__':
    unittest.main()
