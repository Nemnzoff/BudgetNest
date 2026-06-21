# === Stage 25: Add daily summary calculations ===
# Project: BudgetNest
def calculate_daily_summary(transactions, date):
    daily_data = {}
    for t in transactions:
        if t['date'] == date and 'category' in t:
            cat = t['category'].lower()
            amount = float(t.get('amount', 0))
            if cat not in daily_data:
                daily_data[cat] = {'income': 0, 'expense': 0}
            sign = -1.0 if t.get('type') == 'expense' else 1.0
            daily_data[cat][t['type']] += amount * sign
    total_income = sum(v['income'] for v in daily_data.values())
    total_expense = sum(v['expense'] for v in daily_data.values())
    balance = total_income - total_expense
    return {'categories': daily_data, 'total_income': round(total_income, 2), 'total_expense': round(total_expense, 2), 'balance': round(balance, 2)}
