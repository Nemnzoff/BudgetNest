# === Stage 16: Add argparse support for the most common commands ===
# Project: BudgetNest
import argparse

def main():
    parser = argparse.ArgumentParser(description="BudgetNest: Household Budget Notebook")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add transaction command
    trans_parser = subparsers.add_parser("add-transaction", help="Add a new expense or income")
    trans_parser.add_argument("--category", required=True, help="Category name (e.g., Food)")
    trans_parser.add_argument("--amount", type=float, required=True, help="Amount in currency")
    trans_parser.add_argument("--date", default=None, help="Date of transaction (YYYY-MM-DD)")

    # Add report command
    rep_parser = subparsers.add_parser("report", help="Generate a summary report")
    rep_parser.add_argument("--period", choices=["week", "month", "year"], default="month", help="Report period")
    rep_parser.add_argument("--format", choices=["text", "csv"], default="text", help="Output format")

    # Add goal command
    goal_parser = subparsers.add_parser("goal", help="Manage savings goals")
    sub_goal = goal_parser.add_subparsers(dest="subcommand", required=True)
    
    add_goal = sub_goal.add_parser("add", help="Add a new goal")
    add_goal.add_argument("--name", required=True, help="Goal name (e.g., Vacation)")
    add_goal.add_argument("--target", type=float, required=True, help="Target amount")

    show_goal = sub_goal.add_parser("show", help="Show all active goals")
    
    delete_goal = sub_goal.add_parser("delete", help="Delete a goal by name")
    delete_goal.add_argument("--name", required=True, help="Goal name to remove")

    args = parser.parse_args()
    if not hasattr(args, 'command'):
        parser.print_help()
        return
    
    # Placeholder for actual logic execution based on parsed arguments
    print(f"Command '{args.command}' executed with arguments: {vars(args)}")

if __name__ == "__main__":
    main()
