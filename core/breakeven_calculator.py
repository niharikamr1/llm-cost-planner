import math
from schemas.outputs import BreakEvenResult
 
 
def calculate_breakeven(
    monthly_ai_cost: float,
    revenue_per_user: float,
) -> BreakEvenResult:
    if revenue_per_user <= 0:
        raise ValueError('revenue_per_user must be positive')
    breakeven = math.ceil(monthly_ai_cost / revenue_per_user)
    return BreakEvenResult(
        breakeven_users  = breakeven,
        monthly_ai_cost  = monthly_ai_cost,
        revenue_per_user = revenue_per_user,
    )
