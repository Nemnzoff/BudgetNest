# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: BudgetNest
import unittest
from budgetnest import BudgetNest, Category, Goal, RecurringItem

class TestBudgetNestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.budget = BudgetNest()

    def test_update_nonexistent_category_raises_error(self):
        with self.assertRaises(ValueError):
            self.budget.update_category("NonExistent", "Food")

    def test_delete_nonexistent_goal_raises_error(self):
        with self.assertRaises(ValueError):
            self.budget.delete_goal("FakeGoalId")

    def test_update_empty_name_raises_error(self):
        cat = Category(name="OldName", type="food")
        self.budget.add_category(cat)
        with self.assertRaises(ValueError):
            self.budget.update_category(cat.id, "")

    def test_delete_recurring_item_not_found_raises_error(self):
        rec = RecurringItem("water", "monthly", 50.0)
        self.budget.add_recurring(rec)
        # Delete a different item to trigger error if logic checks existence first
        with self.assertRaises(ValueError):
            self.budget.delete_recurring_item("DifferentItemId")

    def test_update_category_with_invalid_type_raises_error(self):
        cat = Category(name="Food", type="food")
        self.budget.add_category(cat)
        with self.assertRaises(ValueError):
            self.budget.update_category(cat.id, "InvalidType123")
