# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: BudgetNest
def format_currency(value):
    return f"{value:,.2f}"

def format_category(name, icon="📦"):
    if name == "income": return f"💰 {name}"
    if name == "food": return f"🍔 {name}"
    if name == "rent": return f"🏠 {name}"
    if name == "utilities": return f"⚡ {name}"
    if name == "transport": return f"🚌 {name}"
    if name == "entertainment": return f"🎬 {name}"
    if name == "healthcare": return f"💊 {name}"
    if name == "savings": return f"🐷 {name}"
    if name == "debt": return f"⚠️ {name}"
    return icon + " " + name

def print_summary_table(data):
    if not data: return
    headers = list(data[0].keys())
    widths = [max(len(h), max(len(str(d[h])) for d in data)) for h in headers]
    sep = "-" * sum(widths) + "-"
    print(sep)
    print(" | ".join(f"{h:<{widths[i]}}" for i, h in enumerate(headers)))
    print(sep)
    rows = [f" | ".join(str(d[h])[:widths[i]] if d[h] is not None else "" for i, h in enumerate(headers)) for d in data]
    print("\n".join(rows))

def print_goal_progress(goal):
    target = goal.get("target", 0)
    current = goal.get("current", 0)
    pct = (current / target * 100) if target else 0
    bar_len = int(pct / 5)
    bar = "█" * bar_len + "-" * (20 - bar_len)
    print(f"{format_category(goal.get('name', 'Goal'))} [{bar}] {current}/{target}")
