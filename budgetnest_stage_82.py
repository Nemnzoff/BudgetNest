# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: BudgetNest
def demo_budget_nest():
    """End-to-end walkthrough of BudgetNest."""
    from budgetnest import App, Category, Goal, RecurringItem, Transaction
    app = App()
    cat_food = Category(name="Food", limit=500)
    goal_savings = Goal(name="Emergency Fund", target=10000)
    recurring_gym = RecurringItem("Gym", 30, "monthly")
    for i in range(6): app.add_transaction(Transaction(cat_food, amount=-25.5))
    for i in range(4): app.add_transaction(Transaction(recurring_gym, amount=-30))
    app.save()
    print("=== BudgetNest Demo ===")
    print(f"Food total: {app.get_category_balance(cat_food)} / {cat_food.limit}")
    print(f"Savings goal progress: {app.get_goal_progress(goal_savings)}/{goal_savings.target}")
    print(f"Gym recurring count: {app.get_recurring_count(recurring_gym.name)}")
    app.report()

demo_budget_nest()
