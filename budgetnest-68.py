# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: BudgetNest
def generate_changelog(activity_log):
    """Generate a compact changelog from the activity log."""
    lines = []
    for entry in sorted(activity_log, key=lambda x: x.get("date", "")):
        date = entry.get("date", "unknown")
        action = entry.get("action", "")
        detail = entry.get("detail", "")
        if detail:
            lines.append(f"{date} | {action}: {detail}")
        else:
            lines.append(f"{date} | {action}")
    return "\n".join(lines)

if __name__ == "__main__":
    sample_log = [
        {"date": "2024-01-15", "action": "Added category", "detail": "Groceries"},
        {"date": "2024-01-20", "action": "Created goal", "detail": "Save for vacation"},
        {"date": "2024-02-01", "action": "Set up recurring item", "detail": "Weekly gym membership"},
    ]
    print(generate_changelog(sample_log))
