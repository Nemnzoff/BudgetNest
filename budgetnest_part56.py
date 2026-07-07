# === Stage 56: Add compact error classes for domain failures ===
# Project: BudgetNest
class BudgetNestError(Exception):
    """Base class for all domain-specific failures in BudgetNest."""
    pass


class CategoryNotFoundError(BudgetNestError):
    def __init__(self, name: str):
        super().__init__(f"Category '{name}' not found.")
        self.name = name


class GoalNotFoundError(BudgetNestError):
    def __init__(self, name: str):
        super().__init__(f"Goal '{name}' not found.")
        self.name = name


class RecurringItemNotFound(BudgetNestError):
    def __init__(self, item_id: int):
        super().__init__(f"Recurring item with id {item_id} not found.")
        self.item_id = item_id


class BudgetExceededError(BudgetNestError):
    def __init__(self, category_name: str, amount_spent: float, budget_limit: float):
        message = (
            f"Budget exceeded for category '{category_name}': "
            f"{amount_spent:.2f} spent out of {budget_limit:.2f} limit."
        )
        super().__init__(message)
        self.category_name = category_name
