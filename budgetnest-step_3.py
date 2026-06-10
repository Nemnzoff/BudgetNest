# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: BudgetNest
def validate_budget_entry(entry: dict) -> tuple[bool, str]:
    if not entry.get("id"):
        return False, "Missing required field: id"
    if not isinstance(entry.get("category"), str) or len(entry["category"]) > 50:
        return False, "Category must be a string under 50 characters"
    if not isinstance(entry.get("description"), str) or len(entry["description"]) > 200:
        return False, "Description must be a string under 200 characters"
    if entry.get("amount") is None or (isinstance(entry["amount"], (int, float)) and entry["amount"] <= 0):
        return False, "Amount must be a positive number"
    if entry.get("type") not in ["income", "expense"]:
        return False, "Type must be either 'income' or 'expense'"
    if entry.get("goal_id") is not None and not isinstance(entry["goal_id"], str):
        return False, "Goal ID must be a string or omitted"
    if entry.get("is_recurring", False) and not isinstance(entry.get("frequency"), str):
        return False, "Recurring items must specify a frequency string (e.g., 'weekly')"
    return True, "Valid"

def sanitize_identifier(value: str, max_len: int = 32) -> str:
    if not value:
        return ""
    cleaned = "".join(c for c in value.lower() if c.isalnum() or c in "-_")
    return cleaned[:max_len]

def validate_short_text(text: str, max_len: int = 100) -> bool:
    return isinstance(text, str) and len(text) <= max_len
