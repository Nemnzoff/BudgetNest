# === Stage 11: Add JSON export for the current application state ===
# Project: BudgetNest
def export_state_json(data, filename="budget_nest.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"State exported to {filename}")
