# === Stage 53: Add command help text and usage examples ===
# Project: BudgetNest
import argparse, sys

def print_help():
    parser = argparse.ArgumentParser(prog="BudgetNest", description="Household budget notebook with categories, goals, and reports.")
    parser.add_argument("--add-category", help="Add a new category (e.g., Food)")
    parser.add_argument("--set-goal", nargs=2, metavar=("NAME", "AMOUNT"), help="Set a savings goal")
    parser.add_argument("--log-expense", nargs=3, metavar=("CATEGORY", "AMOUNT", "NOTE"), help="Log an expense")
    parser.add_argument("--report-month", type=int, help="Generate report for month YYYY-MM (e.g., 2024-10)")
    args = parser.parse_args()

    if not any([args.add_category, args.set_goal, args.log_expense, args.report_month]):
        print("Usage examples:")
        print(f"  python budgetnest.py --add-category Food")
        print(f'  python budgetnest.py --set-goal Vacation 500')
        print('  python budgetnest.py --log-expense Food 25 "Groceries"')
        print('  python budgetnest.py --report-month 10')

if __name__ == "__main__":
    print_help()
