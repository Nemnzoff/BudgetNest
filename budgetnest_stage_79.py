# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: BudgetNest
def self_check():
    from budgetnest import categories, goals, recurring, reports
    print("Categories:", list(categories.get_all()))
    print("Goals:", list(goals.get_all()))
    print("Recurring items sample:", list(recurring.get_all()[:3]))
    summary = reports.summary_report()
    print("Summary report generated successfully")
