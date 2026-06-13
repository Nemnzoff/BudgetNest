# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: BudgetNest
def sort_entries(entries, key='last_update'):
    valid_keys = {'title', 'date', 'priority', 'last_update'}
    if key not in valid_keys:
        raise ValueError(f"Invalid key '{key}'. Use one of {valid_keys}.")
    reverse = False
    if key == 'priority':
        reverse = True
    return sorted(entries, key=lambda e: e.get(key, ''), reverse=reverse)
