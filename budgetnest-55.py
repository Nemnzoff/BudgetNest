# === Stage 55: Add a setting to disable colorized output ===
# Project: BudgetNest
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="BudgetNest CLI")
    parser.add_argument("--no-color", action="store_true", help="Disable colorized output")
    return parser.parse_args()
