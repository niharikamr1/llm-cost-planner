def format_currency(value: float) -> str:
    if value >= 1_000_000:
        return f'${value / 1_000_000:,.2f}M'
    if value >= 1_000:
        return f'${value:,.2f}'
    if value >= 1:
        return f'${value:.4f}'
    return f'${value:.6f}'
 
 
def format_pct(value: float) -> str:
    return f'{value:.1f}%'
 
 
def format_tokens(tokens: int) -> str:
    if tokens >= 1_000_000:
        return f'{tokens / 1_000_000:.1f}M tokens'
    if tokens >= 1_000:
        return f'{tokens / 1_000:.1f}K tokens'
    return f'{tokens} tokens'
 
 
def priority_color(priority: str) -> str:
    return {
        'HIGH':   '#DC2626',
        'MEDIUM': '#CFC58E',
        'INFO':   '#0E9F6E',
    }.get(priority, '#A7B0BB')
