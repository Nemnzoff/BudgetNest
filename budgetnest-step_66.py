# === Stage 66: Add export of a short status dashboard ===
# Project: BudgetNest
def export_status_dashboard(data):
    """Export a compact status dashboard from accumulated budget data."""
    total_income = sum(entry['amount'] for entry in data if entry.get('type') == 'income')
    total_expense = sum(entry['amount'] for entry in data if entry.get('type') == 'expense')
    balance = total_income - total_expense

    goals = {}
    for goal in data:
        if goal.get('type') == 'goal':
            name = goal.get('name', '')
            target = goal.get('target', 0)
            spent = sum(entry['amount'] for entry in data if entry.get('category', '').startswith(name))
            goals[name] = {'spent': spent, 'target': target}

    status = {
        'balance': balance,
        'total_income': total_income,
        'total_expense': total_expense,
        'goals_status': goals if goals else {}
    }
    return status
