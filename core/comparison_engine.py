from core.cost_calculator import _load_pricing, monthly_cost, annual_cost
from schemas.outputs import ComparisonResult
from typing import List
 
 
def compare_all_models(
    input_tokens: int,
    output_tokens: int,
    daily_calls: int,
) -> List[ComparisonResult]:
    pricing = _load_pricing()
    results = []
    for model_id, model in pricing.items():
        results.append(ComparisonResult(
            model_id     = model_id,
            model_name   = model['name'],
            provider     = model['provider'],
            monthly_cost = monthly_cost(model_id, input_tokens, output_tokens, daily_calls),
            annual_cost  = annual_cost(model_id, input_tokens, output_tokens, daily_calls),
        ))
    return sorted(results, key=lambda x: x.annual_cost)
