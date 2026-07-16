# === Stage 72: Add Markdown report export ===
# Project: BudgetNest
def export_markdown_report(data, path="budget_report.md"):
    with open(path, "w") as f:
        f.write("# BudgetNest Report\n\n")
        cats = data.get("categories", [])
        goals = data.get("goals", [])
        recs = data.get("recurring_items", [])
        entries = data.get("transactions", [])
        if cats:
            f.write("## Categories\n")
            for c in cats:
                f.write(f"- **{c['name']}**: ${sum(e['amount'] for e in entries if e.get('category') == c['id']):.2f}\n")
        if goals:
            f.write("\n## Goals\n")
            for g in goals:
                pct = (g["spent"] / g["target"]) * 100 if g["target"] else 0
                f.write(f"- **{g['name']}**: ${g['spent']:.2f} / ${g['target']:.2f} ({pct:.1f}%)\n")
        if recs:
            f.write("\n## Recurring Items\n")
            for r in recs:
                total = sum(e["amount"] for e in entries if e.get("item_id") == r["id"])
                f.write(f"- **{r['name']}**: ${total:.2f}\n")
        if entries:
            total_spend = sum(abs(e["amount"]) for e in entries)
            f.write(f"\n## Summary\nTotal spent: **${total_spend:.2f}**\n")
