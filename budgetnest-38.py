# === Stage 38: Add data integrity checks for broken references ===
# Project: BudgetNest
def validate_references(data):
    valid_categories = set(cat['name'] for cat in data.get('categories', []))
    valid_goals = set(goal['name'] for goal in data.get('goals', []))
    
    errors = []
    for item in data.get('transactions', []):
        if item.get('category') and item['category'] not in valid_categories:
            errors.append(f"Transaction {item.get('id')} references unknown category '{item['category']}'")
        if item.get('goal_id'):
            goal_names = [g['name'] for g in data.get('goals', [])]
            if str(item['goal_id']) not in goal_names:
                errors.append(f"Transaction {item.get('id')} references unknown goal '{item['goal_id']}'")

    for item in data.get('recurring_items', []):
        if item.get('category') and item['category'] not in valid_categories:
            errors.append(f"Recurring item {item.get('id')} references unknown category '{item['category']}'")
        if item.get('goal_id'):
            goal_names = [g['name'] for g in data.get('goals', [])]
            if str(item['goal_id']) not in goal_names:
                errors.append(f"Recurring item {item.get('id')} references unknown goal '{item['goal_id']}'")

    return len(errors) == 0, errors
