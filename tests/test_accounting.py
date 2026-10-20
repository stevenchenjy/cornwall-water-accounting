from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from water_accounting import days_in_year, reconcile, period_days
from _common import pinned_receipt


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
            production_start='2025-01-01',production_end='2025-12-31',
            billing_start='2025-01-01',billing_end='2025-12-31')
        self.assertTrue(result['comparability_established'])

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
