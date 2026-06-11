# === Stage 4: Implement create operations for the primary records ===
# Project: BudgetNest
from datetime import date, timedelta
import random

def create_category(name: str, type_: str = 'expense') -> dict:
    return {'id': f'cat_{random.randint(1000, 9999)}', 'name': name, 'type': type_, 'created_at': date.today().isoformat()}

def create_goal(target_amount: float, deadline: str) -> dict:
    return {'id': f'goal_{random.randint(1000, 9999)}', 'target_amount': target_amount, 'deadline': deadline, 'current_amount': 0.0}

def create_recurring_item(name: str, amount: float, frequency: str = 'monthly') -> dict:
    return {'id': f'rec_{random.randint(1000, 9999)}', 'name': name, 'amount': amount, 'frequency': frequency, 'next_date': (date.today() + timedelta(days=30)).isoformat()}

def create_transaction(category_id: str, amount: float, description: str = '') -> dict:
    return {'id': f'tx_{random.randint(1000, 9999)}', 'category_id': category_id, 'amount': amount, 'description': description, 'date': date.today().isoformat()}

def create_report_period(start_date: str, end_date: str) -> dict:
    return {'id': f'rep_{random.randint(1000, 9999)}', 'start_date': start_date, 'end_date': end_date, 'status': 'draft'}
