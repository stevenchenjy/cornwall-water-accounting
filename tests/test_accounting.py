from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from water_accounting import days_in_year, reconcile

class AccountingChecks(unittest.TestCase):
    def test_calendar_and_century_leap_years(self):
        self.assertEqual([days_in_year(y) for y in (2024,2025,1900,2000)], [366,365,365,366])

    def test_2024_366_day_reconciliation(self):
        result = reconcile(2024, 283389000, 625159, 19.26, 774287)
        self.assertEqual(result['derived_annual_billed_gal'], 625159*366)
        self.assertLess(abs(result['difference_from_reported_pp']), .01)
        wrong_365_pct = 100*(1-625159*365/283389000)
        self.assertGreater(abs(wrong_365_pct-19.26), .2)
        self.assertEqual(result['warnings'], [])

    def test_inconsistent_report_is_flagged(self):
        self.assertIn('unaccounted_percentage_inconsistent', reconcile(2025, 365000, 900, 99)['warnings'])

    def test_missing_is_not_zero(self):
        self.assertEqual(reconcile(2025, None, 0)['status'], 'missing_observation')
        self.assertEqual(reconcile(2025, 365000, 0)['derived_unaccounted_pct'], 100)

    def test_excess_billed_is_anomaly_not_silently_clamped(self):
        result = reconcile(2025, 365000, 1100)
        self.assertLess(result['derived_unaccounted_gal'], 0)
        self.assertIn('inferred_billed_exceeds_production', result['warnings'])

    def test_percentage_unit(self):
        with self.assertRaises(ValueError):
            reconcile(2025, 365000, 900, 125)

if __name__ == '__main__':
    unittest.main()
