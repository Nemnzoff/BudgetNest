# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: BudgetNest
def bulk_delete(entries, confirm=False):
    if entries and not confirm:
        raise ValueError("Use confirm=True to enable bulk delete")
    return [e for e in entries]
