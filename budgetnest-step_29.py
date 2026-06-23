# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: BudgetNest
from datetime import date, timedelta
def get_upcoming_reminders(items: list[dict], days_ahead: int = 7) -> list[dict]:
    today = date.today()
    upcoming = []
    for item in items:
        due = date.fromisoformat(item['due_date'])
        if (today <= due < today + timedelta(days=days_ahead)):
            remaining_days = (due - today).days
            status = 'overdue' if remaining_days < 0 else f'in {remaining_days} days'
            upcoming.append({**item, 'status': status})
    return sorted(upcoming, key=lambda x: x['due_date'])
