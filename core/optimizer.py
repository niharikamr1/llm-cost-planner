from typing import List, Dict
 
 
def generate_recommendations(
    cost_result,
    comparison_results,
    caching_result,
    margin_result,
    current_model_id: str,
) -> List[Dict]:
    recs = []
 
    # Rule 1 — cheaper model exists with >20% annual savings
    cheapest = comparison_results[0]
    if cheapest.model_id != current_model_id and cost_result.annual_cost > 0:
        pct = (cost_result.annual_cost - cheapest.annual_cost) / cost_result.annual_cost * 100
        if pct >= 20:
            save = cost_result.annual_cost - cheapest.annual_cost
            recs.append({
                'priority': 'HIGH',
                'category': 'Model Switch',
                'recommendation': (
                    f'Switch to {cheapest.model_name} ({cheapest.provider}). '
                    f'Estimated saving: {pct:.0f}% — ${save:,.2f}/year.'
                ),
            })
 
    # Rule 2 — caching saves >10%
    if caching_result.savings_percentage >= 10:
        recs.append({
            'priority': 'MEDIUM',
            'category': 'Enable Caching',
            'recommendation': (
                f'Implement semantic caching. Saves {caching_result.savings_percentage:.1f}% '
                f'— ${caching_result.annual_savings:,.2f}/year at current hit rate.'
            ),
        })
 
    # Rule 3 — margin below target
    if not margin_result.meets_target:
        recs.append({
            'priority': 'HIGH',
            'category': 'Pricing',
            'recommendation': (
                f'Gross margin {margin_result.gross_margin_pct:.1f}% is below your target. '
                'Consider raising subscription pricing or reducing token usage.'
            ),
        })
 
    # Fallback
    if not recs:
        recs.append({
            'priority': 'INFO',
            'category': 'Status',
            'recommendation': 'Setup looks cost-efficient. No immediate actions required.',
        })
 
    return recs
