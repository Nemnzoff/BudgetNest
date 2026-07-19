# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: BudgetNest
def format_currency(value: float) -> str:
    """Format a monetary value with currency symbol and comma separators."""
    return f"${value:,.2f}"


def categorize_items(
    items: list[dict[str, Any]],
    goal_categories: dict[str, Goal],
) -> dict[str, list[Item]]:
    """Group items into categories based on the category field and match to goals."""
    categorized = {cat.name: [] for cat in goal_categories.values()}
    uncategorized = []
    for item in items:
        if item.category in categorized:
            categorized[item.category].append(item)
        else:
            uncategorized.append(item)
    return categorized, uncategorized


def calculate_savings_progress(
    total_saved: int, target_amount: int
) -> dict[str, Any]:
    """Calculate the savings progress towards a goal."""
    percentage = (total_saved / target_amount * 100) if target_amount else 0
    return {
        "saved": total_saved,
        "target": target_amount,
        "percentage": round(percentage, 2),
        "remaining": target_amount - total_saved,
    }


def generate_summary_report(
    transactions: list[Transaction], goals: dict[str, Goal]
) -> dict[str, Any]:
    """Generate a summary report of all transactions and goal progress."""
    total_spent = sum(t.amount for t in transactions if t.type == "expense")
    total_income = sum(t.amount for t in transactions if t.type == "income")
    net_balance = total_income - total_spent

    goals_summary = {}
    for goal_name, goal in goals.items():
        progress = calculate_savings_progress(goal.current_amount, goal.target_amount)
        goals_summary[goal_name] = progress

    return {
        "total_income": total_income,
        "total_expenses": total_spent,
        "net_balance": net_balance,
        "goals_progress": goals_summary,
    }


def validate_transaction(transaction: Transaction) -> tuple[bool, str]:
    """Validate a transaction to ensure it meets all requirements."""
    if not isinstance(transaction.amount, (int, float)):
        return False, "Amount must be a number"
    if transaction.amount <= 0:
        return False, "Amount must be positive"
    if not transaction.category or len(transaction.category.strip()) == 0:
        return False, "Category is required and must not be empty"
    if not isinstance(transaction.date, datetime):
        return False, "Date must be a datetime object"
    valid_categories = ["food", "transport", "utilities", "entertainment", "other"]
    if transaction.category.lower() not in valid_categories:
        return False, f"Invalid category: {transaction.category}"
    return True, "Transaction is valid"


if __name__ == "__main__":
    # Test the helper functions with sample data
    test_items = [
        {"category": "food", "amount": 50},
        {"category": "transport", "amount": 20},
        {"category": "other", "amount": 30},
        {"category": "invalid_category", "amount": 15},
    ]

    test_goals = {
        "savings_goal": Goal(name="Emergency Fund", amount=1000, target_amount=5000),
        "investment_goal": Goal(name="Investments", amount=200, target_amount=3000),
    }

    categorized, uncategorized = categorize_items(test_items, test_goals)
    print("Categorized:", categorized)
    print("Uncategorized:", uncategorized)

    progress = calculate_savings_progress(1500, 5000)
    print("Savings Progress:", progress)

    transactions = [
        Transaction(type="expense", category="food", amount=50, date=datetime.now()),
        Transaction(type="income", category="other", amount=2000, date=datetime.now()),
    ]
    report = generate_summary_report(transactions, test_goals)
    print("Summary Report:", report)

    valid_transaction = Transaction(
        type="expense", category="food", amount=50, date=datetime.now()
    )
    is_valid, message = validate_transaction(valid_transaction)
    print(f"Is Valid: {is_valid}, Message: {message}")
