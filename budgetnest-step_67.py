# === Stage 67: Add a function that returns key project metrics ===
# Project: BudgetNest
def project_metrics(data):
    """Return key metrics: total spend, savings rate, goal progress %.
    
    Args:
        data (dict): must contain 'transactions', 'goals', 'category_totals'.
            transactions – list of dicts with 'amount' key.
            goals       – list of dicts with 'target' and 'current' keys.
            category_totals – dict mapping category name -> total spend.
    
    Returns:
        dict with keys: total_spent, savings_rate (0-1), goal_progress_pct.
    """
    total_spent = sum(t['amount'] for t in data.get('transactions', []) if isinstance(t['amount'], (int, float)))
    category_totals = data.get('category_totals', {})

    goals = data.get('goals', [])
    if not goals:
        goal_progress_pct = 0.0
    else:
        completed = sum(1 for g in goals if g.get('current', 0) >= g['target'])
        goal_progress_pct = (completed / len(goals)) * 100

    return {
        'total_spent': total_spent,
        'goal_progress_pct': round(goal_progress_pct, 2),
    }
