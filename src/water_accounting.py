"""Descriptive accounting diagnostics. Inferred billed volume is not an observation."""
import calendar

def days_in_year(year: int) -> int:
    return 366 if calendar.isleap(year) else 365

def reconcile(year, produced_gal, daily_billed_gal, reported_unaccounted_pct=None, daily_produced_gal=None):
    if produced_gal is None or daily_billed_gal is None:
        return {'status': 'missing_observation', 'days': days_in_year(year)}
    if produced_gal <= 0 or daily_billed_gal < 0:
        raise ValueError('Produced volume must be positive; daily billed volume nonnegative')
    if reported_unaccounted_pct is not None and not 0 <= reported_unaccounted_pct <= 100:
        raise ValueError('Reported percentage must use 0–100 units')
    days = days_in_year(year)
    annual_billed = daily_billed_gal * days
    unaccounted = produced_gal - annual_billed
    implied_pct = 100 * unaccounted / produced_gal
    difference = None if reported_unaccounted_pct is None else implied_pct - reported_unaccounted_pct
    daily_check = None if daily_produced_gal is None else produced_gal / days - daily_produced_gal
    warnings = []
    if annual_billed > produced_gal + days / 2:
        warnings.append('inferred_billed_exceeds_production')
    if difference is not None and abs(difference) > 0.05:
        warnings.append('unaccounted_percentage_inconsistent')
    if daily_check is not None and abs(daily_check) > 0.5:
        warnings.append('reported_daily_production_inconsistent')
    return dict(status='diagnostic_only', days=days, derived_annual_billed_gal=annual_billed,
                inferred_billed_rounding_half_width_gal=days/2, derived_unaccounted_gal=unaccounted,
                derived_unaccounted_pct=implied_pct, difference_from_reported_pp=difference,
                daily_production_difference_gal=daily_check, warnings=warnings)
