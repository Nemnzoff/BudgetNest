# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: BudgetNest
def compare_snapshots(before, after):
    """Compact helper returning a dict of keys present in either state with their before/after values."""
    diff = {}
    all_keys = set(list(before.values()) + list(after.values()))
    for key in sorted(all_keys):
        b, a = before.get(key), after.get(key)
        if type(b) == type(a):
            if b != a:
                diff[key] = {"before": b, "after": a}
    return diff
