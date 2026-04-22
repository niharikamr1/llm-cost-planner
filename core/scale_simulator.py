from core.cost_calculator import cost_per_request
from typing import List, Dict
 
USER_TIERS = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]
 
 
def simulate_scale(
    model_id: str,
    input_tokens: int,
    output_tokens: int,
    calls_per_user_per_day: int = 1,
) -> List[Dict]:
    cpr = cost_per_request(model_id, input_tokens, output_tokens)
    return [
        {
            'users':        users,
            'daily_cost':   round(cpr * calls_per_user_per_day * users, 4),
            'monthly_cost': round(cpr * calls_per_user_per_day * users * 30, 2),
            'annual_cost':  round(cpr * calls_per_user_per_day * users * 365, 2),
        }
        for users in USER_TIERS
    ]
