import pytest
from pydantic import ValidationError
from schemas.inputs import TokenCostInput, CachingInput, RevenueInput
 
def test_negative_input_tokens_rejected():
    with pytest.raises(ValidationError):
        TokenCostInput(model_id='gpt-4o',input_tokens=-1,output_tokens=200,daily_calls=100)
 
def test_zero_output_tokens_rejected():
    with pytest.raises(ValidationError):
        TokenCostInput(model_id='gpt-4o',input_tokens=500,output_tokens=0,daily_calls=100)
 
def test_zero_daily_calls_rejected():
    with pytest.raises(ValidationError):
        TokenCostInput(model_id='gpt-4o',input_tokens=500,output_tokens=200,daily_calls=0)
 
def test_cache_rate_above_100_rejected():
    with pytest.raises(ValidationError):
        CachingInput(cache_hit_rate=101.0)
 
def test_cache_rate_negative_rejected():
    with pytest.raises(ValidationError):
        CachingInput(cache_hit_rate=-5.0)
 
def test_cache_rate_100_accepted():
    c = CachingInput(cache_hit_rate=100.0)
    assert c.cache_hit_rate == 100.0
 
def test_zero_users_rejected():
    with pytest.raises(ValidationError):
        RevenueInput(monthly_revenue_per_user=10.0,current_users=0,target_margin_pct=60)
 
def test_negative_revenue_rejected():
    with pytest.raises(ValidationError):
        RevenueInput(monthly_revenue_per_user=-1.0,current_users=100,target_margin_pct=60)
 
def test_margin_above_100_rejected():
    with pytest.raises(ValidationError):
        RevenueInput(monthly_revenue_per_user=10.0,current_users=100,target_margin_pct=120)
