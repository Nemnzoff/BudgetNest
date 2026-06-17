# === Stage 18: Add an activity log with timestamps and action names ===
# Project: BudgetNest
from datetime import datetime, timedelta
import random

def log_activity(action: str, category: str = "General", amount: float = 0.0):
    """Records a transaction with timestamp and action name."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "category": category,
        "amount": round(amount, 2) if isinstance(amount, (int, float)) else amount
    }
    print(f"[{entry['timestamp']}] Action: {entry['action']} | Category: {entry['category']} | Amount: {entry['amount']}")

def simulate_daily_spending(days: int = 7):
    """Generates random daily spending logs for demonstration."""
    actions = ["Groceries", "Utilities", "Transport", "Entertainment", "Health"]
    categories = {"Groceries": "Food", "Utilities": "Home", "Transport": "Travel", 
                  "Entertainment": "Fun", "Health": "Medical"}
    
    for _ in range(days):
        action = random.choice(actions)
        cost = round(random.uniform(5.0, 150.0), 2)
        log_activity(action=action, category=categories.get(action, "Other"), amount=-cost)

if __name__ == "__main__":
    simulate_daily_spending()
