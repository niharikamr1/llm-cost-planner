from pydantic import BaseModel, field_validator
 
 
class TokenCostInput(BaseModel):
    model_id: str
    input_tokens: int
    output_tokens: int
    daily_calls: int
 
    @field_validator('input_tokens', 'output_tokens', 'daily_calls')
    @classmethod
    def must_be_positive(cls, v, info):
        if v <= 0:
            raise ValueError(f'{info.field_name} must be greater than zero')
        return v
 
 
class CachingInput(BaseModel):
    cache_hit_rate: float  # 0.0 – 100.0
 
    @field_validator('cache_hit_rate')
    @classmethod
    def valid_percentage(cls, v):
        if not 0.0 <= v <= 100.0:
            raise ValueError('cache_hit_rate must be between 0 and 100')
        return v
 
 
class RevenueInput(BaseModel):
    monthly_revenue_per_user: float
    current_users: int
    target_margin_pct: float
 
    @field_validator('monthly_revenue_per_user')
    @classmethod
    def positive_revenue(cls, v):
        if v <= 0:
            raise ValueError('monthly_revenue_per_user must be positive')
        return v
 
    @field_validator('current_users')
    @classmethod
    def positive_users(cls, v):
        if v < 1:
            raise ValueError('current_users must be at least 1')
        return v
 
    @field_validator('target_margin_pct')
    @classmethod
    def valid_margin_target(cls, v):
        if not 0.0 <= v <= 100.0:
            raise ValueError('target_margin_pct must be 0 to 100')
        return v
