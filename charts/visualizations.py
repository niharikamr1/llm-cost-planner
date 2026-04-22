import plotly.graph_objects as go
import plotly.express as px
from typing import List
 
 
# ── Shared Theme ─────────────────────────────────────────────────
def apply_chart_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        paper_bgcolor='#1B2430',
        plot_bgcolor='#344250',
        font=dict(color='#A7B0BB', family='Arial', size=12),
        xaxis=dict(gridcolor='#5F6B78', linecolor='#5F6B78',
                   tickfont=dict(color='#A7B0BB'),
                   title_font=dict(color='#A7B0BB')),
        yaxis=dict(gridcolor='#5F6B78', linecolor='#5F6B78',
                   tickfont=dict(color='#A7B0BB'),
                   title_font=dict(color='#A7B0BB')),
        title_font=dict(color='#F3F4F6', size=16),
        legend=dict(bgcolor='#344250', bordercolor='#5F6B78', borderwidth=1),
        margin=dict(l=50, r=30, t=70, b=50),
    )
    return fig
 
 
# ── Chart 1: Scale Projection ─────────────────────────────────────
def scale_projection_chart(scale_data: List[dict]) -> go.Figure:
    users   = [d['users']        for d in scale_data]
    monthly = [d['monthly_cost'] for d in scale_data]
    annual  = [d['annual_cost']  for d in scale_data]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=users, y=monthly, name='Monthly Cost',
        mode='lines+markers',
        line=dict(color='#6E8CA0', width=2),
        marker=dict(color='#6E8CA0', size=7),
    ))
    fig.add_trace(go.Scatter(
        x=users, y=annual, name='Annual Cost',
        mode='lines+markers',
        line=dict(color='#CFC58E', width=2, dash='dot'),
        marker=dict(color='#CFC58E', size=7),
    ))
    fig.update_layout(
        title='Cost vs Daily Active Users',
        xaxis_title='Daily Active Users',
        yaxis_title='Cost (USD)',
    )
    return apply_chart_theme(fig)
 
 
# ── Chart 2: Model Comparison ─────────────────────────────────────
def model_comparison_chart(comparison_data: List) -> go.Figure:
    names  = [r.model_name  for r in comparison_data]
    costs  = [r.annual_cost for r in comparison_data]
    colors = ['#CFC58E' if i == 0 else '#6E8CA0' for i in range(len(names))]
    fig = go.Figure(go.Bar(
        x=names, y=costs,
        marker_color=colors,
        text=[f'${c:,.2f}' for c in costs],
        textposition='outside',
        textfont=dict(color='#F3F4F6', size=11),
    ))
    fig.update_layout(
        title='Annual Cost Comparison — All Models (Same Parameters)',
        yaxis_title='Annual Cost (USD)',
    )
    return apply_chart_theme(fig)
 
 
# ── Chart 3: Caching Savings ──────────────────────────────────────
def caching_savings_chart(original: float, cached: float) -> go.Figure:
    fig = go.Figure(go.Bar(
        x=['Without Caching', 'With Caching'],
        y=[original, cached],
        marker_color=['#7D94A8', '#CFC58E'],
        text=[f'${original:,.2f}', f'${cached:,.2f}'],
        textposition='outside',
        textfont=dict(color='#F3F4F6', size=12),
    ))
    fig.update_layout(
        title='Monthly Cost: Impact of Caching',
        yaxis_title='Monthly Cost (USD)',
    )
    return apply_chart_theme(fig)
