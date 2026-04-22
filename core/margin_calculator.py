from schemas.outputs import MarginResult
 
 
def calculate_margin(
    monthly_ai_cost: float,
    current_users: int,
    price_per_user: float,
    target_margin_pct: float,
) -> MarginResult:
    total_revenue = current_users * price_per_user
    gross_profit  = total_revenue - monthly_ai_cost
    margin_pct    = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0.0
    return MarginResult(
        gross_margin_pct = round(margin_pct, 2),
        total_revenue    = round(total_revenue, 2),
        total_ai_cost    = round(monthly_ai_cost, 2),
        meets_target     = margin_pct >= target_margin_pct,
    )
