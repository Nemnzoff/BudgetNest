# === Stage 36: Add templates for quickly creating common records ===
# Project: BudgetNest
def create_common_records():
    """Factory to quickly instantiate common budget records without boilerplate."""
    from datetime import date, timedelta
    
    def make_recurring(name: str, amount: float, frequency_days: int):
        return {
            "type": "recurring",
            "name": name,
            "amount": -abs(amount),
            "frequency_days": frequency_days,
            "next_date": date.today() + timedelta(days=frequency_days)
        }

    def make_goal(name: str, target_amount: float, current_amount: float = 0.0):
        return {
            "type": "goal",
            "name": name,
            "target_amount": target_amount,
            "current_amount": current_amount
        }

    def make_category_group(group_name: str, color_code: str):
        return {
            "type": "group",
            "name": group_name,
            "color_code": color_code
        }

    # Example usage for quick insertion into main data structure
    groceries = make_recurring("Groceries", 150.0, 7)
    rent = make_recurring("Rent", -800.0, 30)
    savings_goal = make_goal("Emergency Fund", 10000.0, 2500.0)
    food_group = make_category_group("Food & Drink", "#FF6B6B")

    return [groceries, rent, savings_goal, food_group]
