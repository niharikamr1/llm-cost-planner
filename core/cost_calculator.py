import json
from pathlib import Path
from schemas.outputs import CostResult
 
 
def _load_pricing() -> dict:
    """Load model pricing from config. Uses absolute path — safe for any cwd."""
    path = Path(__file__).parent.parent / 'config' / 'model_pricing.json'
    with open(path) as f:
        return json.load(f)['models']
 
 
def cost_per_request(
    model_id: str,
    input_tokens: int,
    output_tokens: int,
) -> float:
    pricing = _load_pricing()
    if model_id not in pricing:
        raise KeyError(f'Unknown model: {model_id!r}. Check config/model_pricing.json')
    m = pricing[model_id]
    in_cost  = (input_tokens  / 1_000_000) * m['input_price_per_1m']
    out_cost = (output_tokens / 1_000_000) * m['output_price_per_1m']
    return round(in_cost + out_cost, 8)
 
 
def daily_cost(
    model_id: str, input_tokens: int, output_tokens: int, daily_calls: int
) -> float:
    return round(cost_per_request(model_id, input_tokens, output_tokens) * daily_calls, 6)
 
 
def monthly_cost(
    model_id: str, input_tokens: int, output_tokens: int, daily_calls: int
) -> float:
    return round(daily_cost(model_id, input_tokens, output_tokens, daily_calls) * 30, 4)
 
 
def annual_cost(
    model_id: str, input_tokens: int, output_tokens: int, daily_calls: int
) -> float:
    return round(monthly_cost(model_id, input_tokens, output_tokens, daily_calls) * 12, 4)
 
 
def full_cost_result(
    model_id: str, input_tokens: int, output_tokens: int, daily_calls: int
) -> CostResult:
    return CostResult(
        cost_per_request = cost_per_request(model_id, input_tokens, output_tokens),
        daily_cost       = daily_cost(model_id, input_tokens, output_tokens, daily_calls),
        monthly_cost     = monthly_cost(model_id, input_tokens, output_tokens, daily_calls),
        annual_cost      = annual_cost(model_id, input_tokens, output_tokens, daily_calls),
    )
