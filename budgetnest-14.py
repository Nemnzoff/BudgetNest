# === Stage 14: Add file load support with fallback demo data ===
# Project: BudgetNest
def load_or_demo(data_file='budget.json'):
    try:
        import json
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        demo = {
            "categories": ["Food", "Transport", "Housing"],
            "goals": [{"name": "Vacation", "target": 5000, "current": 1200}],
            "recurring": [{"item": "Rent", "amount": -1500, "day": 1}]
        }
        return demo
