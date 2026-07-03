# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: BudgetNest
import unittest
from budget_helpers import validate_category_name, calculate_goal_progress

class TestBudgetHelpers(unittest.TestCase):
    def test_validate_category_names(self):
        self.assertTrue(validate_category_name("Food"))
        self.assertFalse(validate_category_name(""))
        self.assertFalse(validate_category_name("Groceries!"))
    
    def test_calculate_goal_progress(self):
        self.assertEqual(calculate_goal_progress(100, 50), 0.5)
        self.assertEqual(calculate_goal_progress(100, 0), 0.0)
        self.assertEqual(calculate_goal_progress(100, 200), 1.0)

if __name__ == "__main__":
    unittest.main()
