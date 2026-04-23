from core.comparison_engine import compare_all_models
 
def test_returns_all_models():
    results = compare_all_models(500, 200, 1000)
    assert len(results) == 6
 
def test_sorted_cheapest_first():
    results = compare_all_models(500, 200, 1000)
    costs = [r.annual_cost for r in results]
    assert costs == sorted(costs)
 
def test_cheapest_is_budget_model():
    results = compare_all_models(500, 200, 1000)
    assert results[0].model_id in ['gpt-4o-mini', 'gemini-1.5-flash', 'claude-3-haiku']
