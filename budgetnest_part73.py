# === Stage 73: Add a lightweight HTML report export ===
# Project: BudgetNest
def export_html_report(data, path="budget_nest.html"):
    """Export budget data to a standalone HTML report."""
    lines = []
    lines.append("<!DOCTYPE html>")
    lines.append("<html><head><meta charset='utf-8'>")
    lines.append('<title>BudgetNest Report</title>')
    lines.append("<style>body{font-family:monospace;margin:20px}table{border-collapse:collapse;width:100%%}th,td{padding:6px;border:1px solid #ccc;text-align:left}</style>")
    lines.append("</head><body>")
    lines.append(f"<h1>BudgetNest Report</h1>")
    if "categories" in data and data["categories"]:
        lines.append("<h2>Categories</h2><table><tr><th>Name</th><th>Total Spent</th></tr>")
        for c in data["categories"]:
            total = sum(item.get("amount", 0) for item in c.get("items", []))
            lines.append(f"<tr><td>{c['name']}</td><td>${total:.2f}</td></tr>")
        lines.append("</table>")
    if "goals" in data and data["goals"]:
        lines.append("<h2>Goals</h2><table><tr><th>Name</th><th>Target</th><th>Saved</th></tr>")
        for g in data["goals"]:
            saved = sum(item.get("amount", 0) for item in g.get("items", []))
            lines.append(f"<tr><td>{g['name']}</td><td>${g['target']:.2f}</td><td>${saved:.2f}</td></tr>")
        lines.append("</table>")
    if "recurring" in data and data["recurring"]:
        lines.append("<h2>Recurring Items</h2><table><tr><th>Name</th><th>Amount</th><th>Frequency</th></tr>")
        for r in data["recurring"]:
            lines.append(f"<tr><td>{r['name']}</td><td>${r['amount']:.2f}</td><td>{r.get('frequency','')}</td></tr>")
        lines.append("</table>")
    if "transactions" in data and data["transactions"]:
        lines.append("<h2>Recent Transactions</h2><table><tr><th>Date</th><th>Description</th><th>Amount</th></tr>")
        for t in sorted(data["transactions"], key=lambda x: x.get("date",""), reverse=True)[:20]:
            lines.append(f"<tr><td>{t['date']}</td><td>{t.get('description','')}</td><td>${t['amount']:.2f}</td></tr>")
        lines.append("</table>")
    lines.append("</body></html>")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
