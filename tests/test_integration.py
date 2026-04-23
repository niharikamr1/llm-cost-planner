from core.cost_calculator      import full_cost_result
from core.comparison_engine    import compare_all_models
from core.caching_estimator    import estimate_caching_savings
from core.breakeven_calculator import calculate_breakeven
from core.margin_calculator    import calculate_margin
from core.optimizer            import generate_recommendations
 
def test_scenario_1_basic_cost():
    r = full_cost_result('gpt-4o', 500, 200, 1000)
    assert r.daily_cost > 0
    assert r.monthly_cost == round(r.daily_cost * 30, 4)
    assert r.annual_cost  == round(r.monthly_cost * 12, 4)
 
def test_scenario_2_model_comparison():
    results = compare_all_models(500, 200, 1000)
    assert len(results) > 0
    assert all(r.annual_cost >= 0 for r in results)
 
def test_scenario_3_caching_enabled():
    result = estimate_caching_savings('gpt-4o', 500, 200, 1000, 30)
    assert result.monthly_savings > 0
    assert result.cached_monthly_cost < result.original_monthly_cost
    assert 0 <= result.savings_percentage <= 100
 
def test_scenario_4_breakeven_margin():
    cost  = full_cost_result('gpt-4o', 500, 200, 1000)
    beven = calculate_breakeven(cost.monthly_cost, 10.0)
    marg  = calculate_margin(cost.monthly_cost, 500, 10.0, 60.0)
    assert beven.breakeven_users > 0
    assert isinstance(marg.meets_target, bool)
 
def test_scenario_5_optimizer_returns_recs():
    cost  = full_cost_result('gpt-4o', 500, 200, 1000)
    comps = compare_all_models(500, 200, 1000)
    cache = estimate_caching_savings('gpt-4o', 500, 200, 1000, 30)
    marg  = calculate_margin(cost.monthly_cost, 100, 5.0, 80.0)
    recs  = generate_recommendations(cost, comps, cache, marg, 'gpt-4o')
    assert len(recs) > 0
    assert all('recommendation' in r and 'priority' in r for r in recs)
