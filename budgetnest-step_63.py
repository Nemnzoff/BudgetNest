# === Stage 63: Add relationships between records where useful ===
# Project: BudgetNest
def get_relationships(budget_nest):
    """Return a dict of useful relationships between records in BudgetNest."""
    rels = {}
    
    # Category -> total spending this month (by transaction)
    for cat, data in budget_nest.get('categories', {}).items():
        cat_id = data['id'] if 'id' in data else None
        monthly_spending = sum(
            t['amount'] for t in budget_nest.get('transactions', [])
            if t.get('category') == cat or t.get('category_id') == cat_id
        )
        rels[cat_id] = {'monthly_spending': monthly_spending}

    # Goal -> progress as percentage of target
    for goal, data in budget_nest.get('goals', {}).items():
        goal_id = data['id'] if 'id' in data else None
        current = sum(
            t['amount'] for t in budget_nest.get('transactions', [])
            if t.get('goal') == goal or t.get('goal_id') == goal_id
        )
        target = data.get('target', 0)
        pct = (current / target * 100) if target else 0
        rels[goal_id] = {'progress_pct': pct}

    # Recurring item -> next scheduled date (approximate, using last transaction + frequency)
    for rec, data in budget_nest.get('recurring_items', {}).items():
        rec_id = data['id'] if 'id' in data else None
        freq_days = data.get('frequency_days', 30)
        rels[rec_id] = {'next_scheduled_day': freq_days}

    return rels
