# === Stage 51: Add unit tests for search and filter behavior ===
# Project: BudgetNest
import unittest
from budget_nest import BudgetNest, Transaction, Category, Goal

class TestBudgetNestSearch(unittest.TestCase):
    def setUp(self):
        self.budget = BudgetNest()
        self.budget.add_category(Category("Food", "expense"))
        self.budget.add_goal(Goal("Savings", 1000))
        self.budget.add_transaction(Transaction(2023, 1, 15, "Grocery", 50.0, Category("Food")))
        self.budget.add_transaction(Transaction(2023, 1, 16, "Restaurant", 20.0, Category("Food")))
        self.budget.add_transaction(Transaction(2023, 2, 1, "Salary", 5000.0))

    def test_search_by_category(self):
        results = self.budget.search_transactions(category="Food")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r.category.name == "Food" for r in results))

    def test_filter_by_date_range(self):
        results = self.budget.filter_transactions(start_date=2023, end_date=1)
        self.assertEqual(len(results), 2)

    def test_search_with_no_matches(self):
        results = self.budget.search_transactions(category="Travel")
        self.assertEqual(len(results), 0)
