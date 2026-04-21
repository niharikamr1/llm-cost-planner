from pydantic import BaseModel
from typing import List
 
 
class CostResult(BaseModel):
    cost_per_request: float
    daily_cost: float
    monthly_cost: float
    annual_cost: float
 
 
class ComparisonResult(BaseModel):
    model_id: str
    model_name: str
    provider: str
    monthly_cost: float
    annual_cost: float
 
 
class CachingResult(BaseModel):
    original_monthly_cost: float
    cached_monthly_cost: float
    monthly_savings: float
    annual_savings: float
    savings_percentage: float
 
 
class BreakEvenResult(BaseModel):
    breakeven_users: int
    monthly_ai_cost: float
    revenue_per_user: float
 
 
class MarginResult(BaseModel):
    gross_margin_pct: float
    total_revenue: float
    total_ai_cost: float
    meets_target: bool
