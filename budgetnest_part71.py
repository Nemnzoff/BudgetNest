# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: BudgetNest
def seed_demo_data(db, categories, goals, recurring):
    """Populate a fresh BudgetNest database with deterministic sample data."""
    import hashlib

    rng = lambda s: int(hashlib.md5(s.encode()).hexdigest()[:8], 16) % 100

    demo_cats = [
        ("Groceries", "Food"),
        ("Rent", "Housing"),
        ("Utilities", "Housing"),
        ("Transport", "Lifestyle"),
        ("Entertainment", "Lifestyle"),
        ("Healthcare", "Wellness"),
        ("Education", "Growth"),
    ]
    for name, group in demo_cats:
        categories.append({"name": name, "group": group})

    demo_goals = [
        {"name": "Emergency Fund", "target": 5000.0},
        {"name": "Vacation Savings", "target": 2000.0},
        {"name": "New Laptop", "target": 1200.0},
    ]
    for g in demo_goals:
        goals.append(g)

    demo_recurring = [
        {"category": "Groceries", "amount": 350.0, "day_of_week": 4},
        {"category": "Rent", "amount": 1200.0, "day_of_week": 1},
        {"category": "Utilities", "amount": 120.0, "day_of_week": 3},
        {"category": "Transport", "amount": 50.0, "day_of_week": 4},
    ]
    for r in demo_recurring:
        recurring.append(r)

    return categories, goals, recurring
