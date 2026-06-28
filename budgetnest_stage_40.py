# === Stage 40: Add plain text report export ===
# Project: BudgetNest
def export_text_report(data):
    """Export budget data to a plain text report."""
    lines = ["BudgetNest Report", "=" * 40]
    
    # Categories summary
    cat_lines = [f"\nCategories:", "-" * 20, f"{'Name':<15} {'Income':>10} {'Expense':>10}", ""]
    for name, inc, exp in data.get("categories", []):
        net = inc - exp
        cat_lines.append(f"{name:<15} {inc:>10.2f} {exp:>10.2f}")
    
    # Goals summary
    goal_lines = [f"\nGoals:", "-" * 20, f"{'Name':<20} {'Target':>10} {'Current':>10}", ""]
    for name, target, current in data.get("goals", []):
        progress = (current / target) * 100 if target else 0
        goal_lines.append(f"{name:<20} {target:>10.2f} {current:>10.2f}")
    
    # Recurring items summary
    rec_lines = [f"\nRecurring Items:", "-" * 20, f"{'Name':<25} {'Amount':>10}", ""]
    for name, amount in data.get("recurring", []):
        rec_lines.append(f"{name:<25} {amount:>10.2f}")
    
    # Total summary
    total_income = sum(c[1] for c in data.get("categories", []))
    total_expense = sum(c[2] for c in data.get("categories", []))
    net_balance = total_income - total_expense
    
    lines.append(f"\nTotal Income: {total_income:.2f}")
    lines.append(f"Total Expense: {total_expense:.2f}")
    lines.append(f"Net Balance: {net_balance:.2f}")
    
    return "\n".join(lines)
