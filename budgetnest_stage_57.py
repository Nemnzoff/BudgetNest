# === Stage 57: Add structured result objects for command handlers ===
# Project: BudgetNest
class BudgetEntry:
    """Structured result for a budget transaction."""
    def __init__(self, category, amount, date=None):
        self.category = category
        self.amount = abs(float(amount))
        self.date = date or datetime.now().date()

    @property
    def description(self):
        return f"{self.category}: {self.amount:.2f}"

class GoalProgress:
    """Structured result for a goal's current state."""
    def __init__(self, name, target, saved):
        self.name = name
        self.target = float(target)
        self.saved = float(saved)

    @property
    def percentage(self):
        return (self.saved / self.target * 100) if self.target else 0.0

class RecurringSchedule:
    """Structured result for a recurring expense."""
    def __init__(self, name, amount, interval="monthly"):
        self.name = name
        self.amount = abs(float(amount))
        self.interval = interval

class MonthlyReport:
    """Structured result for a monthly budget report."""
    def __init__(self, month, income, expenses):
        self.month = month
        self.income = float(income)
        self.expenses = float(expenses)

    @property
    def balance(self):
        return self.income - self.expenses

    def is_surplus(self):
        return self.balance > 0
