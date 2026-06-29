# === Stage 41: Add plain text import for a simple line-based format ===
# Project: BudgetNest
def load_plain_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def parse_line(line):
    parts = line.split(',')
    if len(parts) < 3:
        raise ValueError(f"Invalid format: {line}")
    category, amount, note = parts[0].strip(), float(parts[1]), parts[2]
    return {'category': category, 'amount': amount, 'note': note}

def load_budget_from_text(filepath):
    lines = load_plain_text(filepath)
    budget = []
    for line in lines:
        try:
            entry = parse_line(line)
            budget.append(entry)
        except ValueError as e:
            print(f"Skipping invalid line: {line} - Error: {e}")
    return budget

def save_budget_to_text(budget, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for entry in budget:
            line = f"{entry['category']},{entry['amount']},{entry['note']}"
            f.write(line + '\n')

if __name__ == "__main__":
    try:
        data = load_budget_from_text("budget.txt")
        print(f"Loaded {len(data)} entries.")
        save_budget_to_text(data, "backup_budget.txt")
        print("Backup saved successfully.")
    except FileNotFoundError:
        print("No budget file found. Please create 'budget.txt'.")
