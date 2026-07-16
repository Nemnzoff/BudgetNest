# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: BudgetNest
def clear_state(confirm_flag: bool) -> None:
    """Reset all in-memory budget data to default state."""
    if not confirm_flag:
        raise ValueError("Clear operation cancelled")
    categories = []
    goals = []
    recurring_items = []
    transactions = []
