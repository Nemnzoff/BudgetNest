# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: BudgetNest
def validate_budget(data):
    warnings = []
    errors = []
    for entry in data:
        if not isinstance(entry, dict) or 'amount' not in entry:
            errors.append(f"Invalid entry structure: {entry}")
            continue
        amount = entry.get('amount')
        date_str = entry.get('date', '')
        category = entry.get('category', '')
        if not isinstance(amount, (int, float)):
            errors.append(f"Non-numeric amount in entry: {entry}")
        elif amount < 0 and entry.get('type') != 'refund':
            warnings.append(f"Negative spending on {date_str}: {amount:.2f}")
        if date_str and ('' not in date_str) and len(date_str) > 10:
            try:
                from datetime import datetime
                datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            except ValueError:
                warnings.append(f"Date format issue on entry: {entry}")
        if category and not isinstance(category, str):
            errors.append(f"Non-string category in entry: {entry}")
    return {'warnings': warnings, 'errors': errors}
