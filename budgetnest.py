# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: BudgetNest
import json
from datetime import date, timedelta
from typing import List, Dict, Any

class BudgetNest:
    def __init__(self):
        self.categories = ["Food", "Transport", "Utilities", "Entertainment", "Savings"]
        self.goals = {"Emergency Fund": 5000, "Vacation": 2000}
        self.recurring_items = {
            "Rent": {"amount": 1200, "category": "Utilities", "day_of_month": 1},
            "Groceries": {"amount": 300, "category": "Food", "day_of_month": 5}
        }
        self.transactions: List[Dict[str, Any]] = []
        self._init_demo_data()

    def _init_demo_data(self):
        today = date.today()
        for i in range(30):
            d = today - timedelta(days=i)
            if d.day == 1:
                self.transactions.append({
                    "date": d, "amount": -self.recurring_items["Rent"]["amount"],
                    "category": self.recurring_items["Rent"]["category"], "type": "expense"
                })
            elif d.day == 5:
                self.transactions.append({
                    "date": d, "amount": -self.recurring_items["Groceries"]["amount"],
                    "category": self.recurring_items["Groceries"]["category"], "type": "expense"
                })
            if i % 3 == 0:
                self.transactions.append({
                    "date": d, "amount": 100, "category": "Salary", "type": "income"
                })

    def add_transaction(self, date_str: str, amount: float, category: str, type: str = "expense"):
        self.transactions.append({"date": date.fromisoformat(date_str), "amount": amount, "category": category, "type": type})

    def get_balance(self) -> float:
        return sum(t["amount"] for t in self.transactions)

    def get_category_total(self, category: str) -> float:
        return sum(t["amount"] for t in self.transactions if t["category"] == category)

    def get_report(self, days: int = 7) -> Dict[str, Any]:
        end_date = date.today()
        start_date = end_date - timedelta(days=days)
        recent = [t for t in self.transactions if start_date <= t["date"] <= end_date]
        return {
            "period": f"{start_date} to {end_date}",
            "balance": sum(t["amount"] for t in recent),
            "by_category": {cat: sum(t["amount"] for t in recent if t["category"] == cat) for cat in self.categories}
        }

if __name__ == "__main__":
    app = BudgetNest()
    print(f"Current Balance: ${app.get_balance():.2f}")
    print(f"Last 7 Days Report:\n{json.dumps(app.get_report(7), indent=2)}")
