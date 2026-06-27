# === Stage 37: Add recommendations for the next useful action ===
# Project: BudgetNest
import json
from datetime import datetime, timedelta
from pathlib import Path

def generate_next_action(budget_data: dict) -> str:
    """Generates a single actionable recommendation based on current budget state."""
    today = datetime.now().date()
    
    # Check for overdue recurring items
    due_items = [item for item in budget_data.get("recurring", []) 
                 if item["due_date"] < today and not item.get("paid")]
    if due_items:
        return f"⚠️ Action: Pay {len(due_items)} overdue bill(s) immediately."

    # Check for goals nearing completion or needing attention
    active_goals = [g for g in budget_data.get("goals", []) 
                    if g["target_date"] and today <= datetime.strptime(g["target_date"], "%Y-%m-%d").date()]
    
    low_progress = [g for g in active_goals if g["current_amount"] < 0.5 * float(g["target_amount"])]
    high_progress = [g for g in active_goals if g["current_amount"] >= 0.9 * float(g["target_amount"]) and g["current_amount"] < float(g["target_amount"])]

    if low_progress:
        worst_goal = min(low_progress, key=lambda x: x["current_amount"])
        return f"📉 Action: Increase savings for '{worst_goal['name']}' (Current: ${worst_goal['current_amount']:.2f} / Target: ${worst_goal['target_amount']:.2f})."

    if high_progress:
        best_goal = max(high_progress, key=lambda x: float(x["current_amount"]))
        return f"🎉 Action: You are close to completing '{best_goal['name']}'! Keep saving."

    # Check for overspending in current month categories
    category_totals = {}
    transactions = budget_data.get("transactions", [])
    for t in transactions:
        if t["date"].month == today.month and t["category"]:
            cat_name = t["category"]
            category_totals[cat_name] = category_totals.get(cat_name, 0) + float(t["amount"])

    limits = {item["name"]: item["limit"] for item in budget_data.get("categories", [])}
    
    overspent_cats = [cat for cat, total in category_totals.items() 
                      if cat in limits and total > limits[cat]]
    
    if overspent_cats:
        worst_cat = max(overspent_cats, key=lambda x: category_totals[x] - limits[x])
        return f"🛑 Action: Stop spending on '{worst_cat}' immediately. You are over limit by ${category_totals[worst_cat] - limits[worst_cat]:.2f}."

    # Default positive reinforcement if no issues found
    total_balance = sum(t["amount"] for t in transactions) + budget_data.get("initial_balance", 0)
    return f"✅ Action: Your net balance is ${total_balance:.2f}. Continue tracking expenses to stay on track."
