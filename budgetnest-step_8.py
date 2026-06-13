# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: BudgetNest
def filter_transactions(transactions, filters=None):
    if filters is None:
        return transactions
    status = filters.get('status')
    category = filters.get('category')
    owner = filters.get('owner')
    tag = filters.get('tag')
    result = []
    for t in transactions:
        if status and t['status'] != status:
            continue
        if category and t.get('category', '').lower() != category.lower():
            continue
        if owner and t.get('owner', '').lower() != owner.lower():
            continue
        if tag and tag not in t.get('tags', []):
            continue
        result.append(t)
    return result
