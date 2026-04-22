from core.cost_calculator import _load_pricing, monthly_cost
from schemas.outputs import CachingResult
 
 
def estimate_caching_savings(
    model_id: str,
    input_tokens: int,
    output_tokens: int,
    daily_calls: int,
    cache_hit_rate: float,
) -> CachingResult:
    base_monthly  = monthly_cost(model_id, input_tokens, output_tokens, daily_calls)
    pricing       = _load_pricing()[model_id]
    hit_fraction  = cache_hit_rate / 100.0
    # Only input tokens are saved on cache hits
    monthly_input = (
        (input_tokens / 1_000_000)
        * pricing['input_price_per_1m']
        * daily_calls
        * 30
    )
    savings_monthly = round(monthly_input * hit_fraction, 4)
    cached_monthly  = round(base_monthly - savings_monthly, 4)
    savings_pct = round((savings_monthly / base_monthly * 100), 2) if base_monthly > 0 else 0.0
    return CachingResult(
        original_monthly_cost = base_monthly,
        cached_monthly_cost   = cached_monthly,
        monthly_savings       = savings_monthly,
        annual_savings        = round(savings_monthly * 12, 2),
        savings_percentage    = savings_pct,
    )
