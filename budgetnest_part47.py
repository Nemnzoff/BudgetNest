# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: BudgetNest
from datetime import date, timedelta
import random

def run_demo():
    categories = ["Food", "Transport", "Utilities"]
    goals = {"Emergency Fund": 5000}
    
    # Generate 30 days of random transactions
    for i in range(1, 31):
        day_offset = timedelta(days=i)
        amount = round(random.uniform(-200, 80), 2)
        
        if amount < 0:
            category = random.choice(categories)
            desc = f"Purchase {category}"
        else:
            category = "Income"
            desc = f"Salary Deposit"
            
        print(f"{day_offset.strftime('%Y-%m-%d')} | {desc} | {amount:.2f} | {category}")

    # Simulate a goal check
    current_savings = 1500.00
    target = goals["Emergency Fund"]
    progress = (current_savings / target) * 100
    
    print(f"\nGoal Status: Emergency Fund")
    print(f"Current: {current_savings:.2f} | Target: {target}")
    print(f"Progress: {progress:.1f}%")

if __name__ == "__main__":
    run_demo()
