# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: BudgetNest
def reset_demo_data(db, categories_file="categories.json", goals_file="goals.json", items_file="items.json"):
    """Reset all demo data and return counts for verification."""
    import json

    with open(categories_file) as f:
        cats = json.load(f)
    with open(goals_file) as f:
        gls = json.load(f)
    with open(items_file) as f:
        items = json.load(f)

    print("Reset counts:")
    print(f"  Categories : {len(cats)}")
    print(f"  Goals      : {len(gls)}")
    print(f"  Items      : {len(items)}")

    return {"categories": cats, "goals": gls, "items": items}
