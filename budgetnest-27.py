# === Stage 27: Add monthly summary calculations ===
# Project: BudgetNest
def calculate_monthly_summary(transactions, categories):
    monthly_data = {}
    for cat in categories:
        monthly_data[cat] = {"income": 0, "expense": 0}
    for t in transactions:
        if t["category"] in monthly_data and t["month"]:
            month_key = f"{t['year']}-{t['month']:02d}"
            val = abs(t["amount"])
            if t["type"] == "income":
                monthly_data[t["category"]]["income"] += val
            else:
                monthly_data[t["category"]]["expense"] += val
    total_income = sum(d["income"] for d in monthly_data.values())
    total_expense = sum(d["expense"] for d in monthly_data.values())
    balance = total_income - total_expense
    return {k: v.copy() for k, v in monthly_data.items()}, {"total_income": total_income, "total_expense": total_expense, "balance": balance}
