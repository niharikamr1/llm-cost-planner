import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import json
import pandas as pd

from schemas.inputs import TokenCostInput
from core.cost_calculator import full_cost_result
from core.comparison_engine import compare_all_models
from core.scale_simulator import simulate_scale
from core.caching_estimator import estimate_caching_savings
from core.breakeven_calculator import calculate_breakeven
from core.margin_calculator import calculate_margin
from core.optimizer import generate_recommendations
from charts.visualizations import (
    scale_projection_chart,
    model_comparison_chart,
    caching_savings_chart,
)
from utils.helpers import format_currency, format_pct, priority_color


# ── Page Config ─────────────────────────────────────────────
st.set_page_config(page_title="LLM Cost Planner", layout="wide")


# ── Theme ───────────────────────────────────────────────────
def apply_theme():
    st.markdown("""
    <style>
    * {font-family: Inter, sans-serif;}

    .stApp {background:#1B2430}

    section[data-testid="stSidebar"] {
        background:#1B2430;
        border-right:1px solid #5F6B78;
        padding-top:20px;
    }

    div[data-testid="stNumberInput"],
    div[data-testid="stSlider"] {
        background:#2A3441;
        padding:10px;
        border-radius:8px;
        border:1px solid #5F6B78;
    }

    [data-testid="metric-container"] {
        background:linear-gradient(145deg,#2A3441,#344250);
        border-radius:10px;
        padding:18px;
        border:1px solid #5F6B78;
        box-shadow:0 4px 12px rgba(0,0,0,0.3);
    }

    .stButton>button[kind="primary"]{
        background:linear-gradient(90deg,#CFC58E,#E5D89C);
        color:#1B2430!important;
        font-weight:700;
        border:none;
        border-radius:10px;
        padding:12px;
        transition:0.2s;
    }

    .stButton>button:hover{
        transform:translateY(-1px);
        box-shadow:0 6px 16px rgba(0,0,0,0.4);
    }

    .stTabs [data-baseweb="tab-panel"] {
        background:#2A3441;
        border-radius:10px;
        padding:20px;
        border:1px solid #5F6B78;
    }
    </style>
    """, unsafe_allow_html=True)


@st.cache_data
def load_models():
    with open("config/model_pricing.json") as f:
        return json.load(f)["models"]


# ── Main ────────────────────────────────────────────────────
def main():
    apply_theme()
    MODELS = load_models()

    # ── Header ───────────────────────────────────────────────
    st.title("LLM Cost Planner")
    st.caption("Forecast • Compare • Optimize AI Inference Costs")

    st.markdown("""
    <div style='display:flex;justify-content:space-between;
    border-bottom:1px solid #5F6B78;padding-bottom:10px;margin-bottom:20px'>
        <div style='color:#A7B0BB'>Dashboard</div>
        <div style='color:#A7B0BB'>Real-time AI Cost Analytics</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Sidebar ──────────────────────────────────────────────
    with st.sidebar:
        st.markdown("## Configuration")
        st.markdown("<hr>", unsafe_allow_html=True)

        model_id = st.selectbox(
            "Model",
            list(MODELS.keys()),
            format_func=lambda x: f"{MODELS[x]['name']} ({MODELS[x]['provider']})"
        )

        st.markdown("#### Token Usage")
        st.caption("Define request-level token consumption")

        input_tokens = st.number_input("Input tokens", 100, 200000, 500)
        output_tokens = st.number_input("Output tokens", 50, 50000, 200)
        daily_calls = st.number_input("Daily calls", 100, 10000000, 1000)

        st.markdown("#### Caching")
        st.caption("Reuse repeated responses")

        cache_hit_rate = st.slider("Cache hit rate (%)", 0, 100, 30)

        st.markdown("#### Revenue & Margin")
        st.caption("Business profitability inputs")

        revenue_per_user = st.number_input("Revenue per user ($)", 0.01, 1000.0, 10.0)
        current_users = st.number_input("Users", 1, 1000000, 500)
        target_margin_pct = st.slider("Target margin (%)", 0, 100, 60)

        run = st.button("Calculate Costs", type="primary", use_container_width=True)

    if not run:
        st.markdown("""
        <div style='padding:20px;background:#2A3441;border-radius:10px;
        border:1px solid #5F6B78;text-align:center;color:#A7B0BB'>
        <h4 style='color:#F3F4F6'>No Data Yet</h4>
        Configure parameters and run calculation
        </div>
        """, unsafe_allow_html=True)
        return

    # ── Compute ──────────────────────────────────────────────
    with st.spinner("Calculating..."):
        try:
            TokenCostInput(
                model_id=model_id,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                daily_calls=daily_calls,
            )

            cost = full_cost_result(model_id, input_tokens, output_tokens, daily_calls)
            comps = compare_all_models(input_tokens, output_tokens, daily_calls)
            scale = simulate_scale(model_id, input_tokens, output_tokens)
            cache = estimate_caching_savings(model_id, input_tokens, output_tokens, daily_calls, cache_hit_rate)
            beven = calculate_breakeven(cost.monthly_cost, revenue_per_user)
            marg = calculate_margin(cost.monthly_cost, current_users, revenue_per_user, target_margin_pct)
            opts = generate_recommendations(cost, comps, cache, marg, model_id)

        except Exception:
            st.error("Invalid inputs — please check values")
            return

    st.success("Calculation completed successfully")

    # ── Tabs ────────────────────────────────────────────────
    tabs = st.tabs([
        "Cost Overview",
        "Model Comparison",
        "Scale Simulation",
        "Caching Impact",
        "Break-even",
        "Margin",
        "Recommendations"
    ])

    with tabs[0]:
        st.markdown("### Key Metrics")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Per Request", format_currency(cost.cost_per_request))
        c2.metric("Daily", format_currency(cost.daily_cost))
        c3.metric("Monthly", format_currency(cost.monthly_cost))
        c4.metric("Annual", format_currency(cost.annual_cost))

    with tabs[1]:
        st.plotly_chart(
            model_comparison_chart(comps),
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with tabs[2]:
        st.plotly_chart(
            scale_projection_chart(scale),
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with tabs[3]:
        st.plotly_chart(
            caching_savings_chart(cache.original_monthly_cost, cache.cached_monthly_cost),
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with tabs[4]:
        st.metric("Break-even users", f"{beven.breakeven_users:,}")

    with tabs[5]:
        st.metric("Margin", format_pct(marg.gross_margin_pct))

    with tabs[6]:
        for rec in opts:
            col = priority_color(rec["priority"])
            st.markdown(f"""
            <div style='padding:14px;border-radius:10px;
            background:#2A3441;border:1px solid #5F6B78;
            border-left:5px solid {col};margin-bottom:12px'>
            <div style='color:{col};font-weight:600'>{rec['priority']}</div>
            <div style='color:#CFC58E'>{rec['category']}</div>
            <div>{rec['recommendation']}</div>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()