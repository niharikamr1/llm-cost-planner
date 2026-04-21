import pytest

from core.cost_calculator import (
    cost_per_request,
    daily_cost,
    monthly_cost,
    annual_cost
)


def test_cost_per_request_gpt4o_known_value():
    # 500 in @ $5/M + 200 out @ $15/M = 0.0055
    result = cost_per_request("gpt-4o", 500, 200)
    assert abs(result - 0.0055) < 0.0001


def test_daily_equals_cpr_times_calls():
    cpr = cost_per_request("gpt-4o", 500, 200)
    d = daily_cost("gpt-4o", 500, 200, 100)
    assert abs(d - round(cpr * 100, 6)) < 1e-5


def test_monthly_equals_daily_times_30():
    d = daily_cost("gpt-4o", 500, 200, 1000)
    m = monthly_cost("gpt-4o", 500, 200, 1000)
    assert abs(m - round(d * 30, 4)) < 0.001


def test_annual_equals_monthly_times_12():
    m = monthly_cost("gpt-4o", 500, 200, 1000)
    a = annual_cost("gpt-4o", 500, 200, 1000)
    assert abs(a - round(m * 12, 4)) < 0.01


def test_unknown_model_raises_key_error():
    with pytest.raises(KeyError):
        cost_per_request("nonexistent-model-xyz", 500, 200)


def test_mini_cheaper_than_gpt4o():
    gpt4o = annual_cost("gpt-4o", 500, 200, 1000)
    mini = annual_cost("gpt-4o-mini", 500, 200, 1000)
    assert mini < gpt4o