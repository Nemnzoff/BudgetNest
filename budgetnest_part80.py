# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: BudgetNest
# Step 80: Polish user-facing messages, names, and examples for consistency.
MESSAGES = {
    "welcome": (
        "Welcome to BudgetNest! This is your household budget notebook.\n"
        "You can track expenses by category, set savings goals, log recurring items,\n"
        "and generate clear reports to stay on top of your finances."
    ),
    "category_added": "Category '{name}' added successfully.",
    "goal_added": (
        f"Savings goal created: target ${target:.2f}, current ${current:.2f}.\n"
        f"Progress: {current/target*100:.1f}%."
    ),
    "recurring_added": (
        f"Recurring item '{name}' set for every {period}. Next due: {next_date.date()}."
    ),
    "expense_logged": (
        f"Expense logged: ${amount:.2f} in category '{category}'.\n"
        f"Remaining this month: ${remaining:.2f} of budget ${budget:.2f}." if budget else None
    ),
    "report_summary": (
        f"\n=== BudgetNest Monthly Report ===\n"
        f"Total spent: ${total_spent:.2f}\n"
        f"Savings total: ${savings_total:.2f}\n"
        f"Goals progress:\n{goals_text}" if goals_text else "No goals set yet."
    ),
}

EXAMPLES = [
    {
        "category": "Groceries",
        "amount": 150.00,
        "note": "Weekly grocery run at the market.",
    },
    {
        "goal_name": "Emergency Fund",
        "target": 5000.00,
        "current": 2340.75,
    },
    {
        "recurring_name": "Netflix Subscription",
        "amount": 15.99,
        "period": "monthly",
    },
]
