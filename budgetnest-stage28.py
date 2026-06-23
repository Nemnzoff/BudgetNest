# === Stage 28: Add overdue item detection based on due dates ===
# Project: BudgetNest
from datetime import date, timedelta
from typing import List, Dict, Optional

def detect_overdue_items(transactions: List[Dict], categories: Dict[str, str]) -> List[Dict]:
    """Identify recurring items that are past their due date."""
    overdue = []
    today = date.today()
    
    for item in transactions:
        if not item.get('is_recurring') or 'due_date' not in item:
            continue
        
        try:
            due = datetime.strptime(item['due_date'], '%Y-%m-%d').date()
            days_overdue = (today - due).days
            
            if days_overdue > 0 and item.get('status') != 'paid':
                overdue.append({
                    **item,
                    'overdue_days': days_overdue,
                    'category': categories.get(item['category'], item['category'])
                })
        except ValueError:
            continue
            
    return sorted(overdue, key=lambda x: x['overdue_days'], reverse=True)
