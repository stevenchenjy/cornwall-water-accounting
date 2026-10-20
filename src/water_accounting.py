"""Period-explicit diagnostics; inferred annual billing is never an observation."""
import calendar
from datetime import date
import math


def days_in_year(year: int) -> int:
    return 366 if calendar.isleap(year) else 365


def period_days(start, end):
    if not start or not end:
        return None
    days = (date.fromisoformat(end) - date.fromisoformat(start)).days + 1
    if days <= 0:
        raise ValueError('Period end precedes start')
    return days


def billing_change_components(old_daily, old_days, new_daily, new_days, *, common_days):
    """Exact decomposition of inferred billing decrease, without causal meaning."""
    rate = (old_daily - new_daily) * common_days
    calendar_part = old_daily * (old_days - common_days) - new_daily * (new_days - common_days)
    return dict(common_days=common_days, daily_rate_component_gal=rate,
                calendar_component_gal=calendar_part,
                total_decrease_gal=old_daily * old_days - new_daily * new_days)


def reconcile(year, produced_gal, daily_billed_gal, reported_unaccounted_pct=None,
              daily_produced_gal=None, *, billing_days=None,
              billing_denominator_status='unconfirmed', production_start=None,
              production_end=None, billing_start=None, billing_end=None,
              boundary_status='unconfirmed', percentage_decimal_places=2,
              annual_production_rounding_half_width_gal=.5, confirmation_refs=None):
    """Require an explicit denominator even for a calendar-day scenario.

    Annual-total precision is a scenario input, never inferred from trailing zeros.
    Daily values use a conditional nearest-gallon rule; percentages use the displayed
    decimal unit. Confirmation references are documentary inputs, not proof supplied
    by a boolean or by a test fixture.
    """
    p_days = period_days(production_start, production_end)
    b_days = period_days(billing_start, billing_end)
    warnings = []
    if p_days is None:
        warnings.append('production_period_unconfirmed')
    if b_days is None:
        warnings.append('billing_coverage_unconfirmed')
    if p_days is not None and b_days is not None and (production_start, production_end) != (billing_start, billing_end):
        warnings.append('production_billing_period_mismatch')
    if boundary_status != 'confirmed':
        warnings.append('measurement_boundary_unconfirmed')
    base = dict(status='missing_observation', calendar_days=days_in_year(year),
                production_period_days=p_days, billing_coverage_days=b_days,
                billing_denominator_days=billing_days,
                billing_denominator_status=billing_denominator_status,
                comparability_established=False, warnings=warnings)
    if produced_gal is None or daily_billed_gal is None:
        return base
    if produced_gal <= 0 or daily_billed_gal < 0:
        raise ValueError('Produced volume must be positive; daily billed volume nonnegative')
    if reported_unaccounted_pct is not None and not 0 <= reported_unaccounted_pct <= 100:
        raise ValueError('Reported percentage must use 0–100 units')
    if billing_days is None:
        return {**base, 'status': 'denominator_required'}
    if billing_denominator_status not in {'assumed_calendar_days', 'assumed_365_day_sensitivity', 'department_confirmed'}:
        raise ValueError('An explicit denominator status is required')
    if not isinstance(billing_days, int) or billing_days <= 0:
        raise ValueError('Billing denominator must be a positive integer')
    if percentage_decimal_places < 0:
        raise ValueError('Percentage precision must be nonnegative')
    production_half_width = annual_production_rounding_half_width_gal
    if not math.isfinite(production_half_width) or not 0 <= production_half_width < produced_gal:
        raise ValueError('Annual production rounding half-width must be finite, nonnegative and below production')
    if billing_denominator_status != 'department_confirmed':
        warnings.append('billing_denominator_assumed')
    if b_days is not None and billing_days != b_days:
        warnings.append('billing_denominator_differs_from_coverage_days')
    annual_billed = daily_billed_gal * billing_days
    residual = produced_gal - annual_billed
    implied_pct = 100 * residual / produced_gal
    difference = None if reported_unaccounted_pct is None else implied_pct - reported_unaccounted_pct
    half_width = billing_days / 2
    implied_low = 100 * (1 - (annual_billed + half_width) / (produced_gal - production_half_width))
    implied_high = 100 * (1 - max(0, annual_billed - half_width) / (produced_gal + production_half_width))
    pct_half = .5 * 10 ** (-percentage_decimal_places)
    compatible = None if reported_unaccounted_pct is None else (
        implied_low <= reported_unaccounted_pct + pct_half
        and implied_high >= reported_unaccounted_pct - pct_half)
    daily_check = None if daily_produced_gal is None or p_days is None else produced_gal / p_days - daily_produced_gal
    daily_compatible = None if daily_check is None else (
        (produced_gal - production_half_width) / p_days <= daily_produced_gal + .5
        and (produced_gal + production_half_width) / p_days >= daily_produced_gal - .5)
    if annual_billed > produced_gal + half_width:
        warnings.append('inferred_billed_exceeds_production')
    if difference is not None and abs(difference) > .05:
        warnings.append('percentage_difference_exceeds_0_05_pp_heuristic')
    if compatible is False:
        warnings.append('percentage_outside_conditional_rounding_interval')
    if daily_check is not None and abs(daily_check) > .5:
        warnings.append('daily_production_difference_exceeds_0_5_gal_heuristic')
    refs = confirmation_refs or {}
    documentary_refs_present = all(refs.get(key) for key in ('billing_coverage', 'billing_denominator', 'measurement_boundary'))
    if billing_denominator_status == 'department_confirmed' and not documentary_refs_present:
        warnings.append('department_confirmation_documentary_references_missing')
    comparable = (p_days is not None and b_days is not None
                  and (production_start, production_end) == (billing_start, billing_end)
                  and billing_days == b_days and billing_denominator_status == 'department_confirmed'
                  and boundary_status == 'confirmed' and documentary_refs_present)
    return {**base, 'status': 'conditional_accounting_diagnostic',
            'comparability_established': comparable,
            'derived_annual_billed_gal': annual_billed,
            'inferred_billed_rounding_half_width_gal': half_width,
            'derived_unaccounted_gal': residual,
            'derived_unaccounted_pct': implied_pct,
            'difference_from_reported_pp': difference,
            'conditional_rounding_compatible': compatible,
            'annual_production_rounding_half_width_gal': production_half_width,
            'conditional_implied_pct_interval': [implied_low, implied_high],
            'daily_production_difference_gal': daily_check,
            'conditional_daily_production_rounding_compatible': daily_compatible,
            'confirmation_refs': refs}
