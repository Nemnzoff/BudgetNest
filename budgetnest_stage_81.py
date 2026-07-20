# === Stage 81: Add final README text as a module string with usage examples ===
# Project: BudgetNest
__USAGE_EXAMPLES = """
# BudgetNest – quick usage examples

import budgetnest as bn

budget = bn.Budget()

# 1. Add categories
food = bn.Category("Groceries", limit=500, recurring=True)
utilities = bn.Category("Electricity & Water", limit=200)
budget.add_category(food)
budget.add_category(utilities)

# 2. Set a savings goal
house_goal = bn.Goal("New Roof", target=8000, deadline="2026-12-31")
budget.set_goal(house_goal)

# 3. Log recurring items (auto-added to the right category each period)
bn.RecurringItem(
    description="Weekly grocery run",
    amount=45.0,
    frequency="weekly",
    next_date=None,
).log_to_category(food)

# 4. Log a one-off expense
food.log_expense("Organic milk & bread", 28.50, "2026-03-10")

# 5. Generate a period report for March
report = budget.generate_report(period="2026-March")
print(report)          # → summary of expenses vs category limits
print(budget.get_goal_progress())   # → bar chart text for each goal

# BudgetNest is dependency-free and runs anywhere Python 3.7+ executes it.
"""
