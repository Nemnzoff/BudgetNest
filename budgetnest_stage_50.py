# === Stage 50: Add unit tests for import and export behavior ===
# Project: BudgetNest
import json, os, tempfile
from pathlib import Path
from budget_nest.core.storage import BudgetStorage

def test_storage_import_export():
    with tempfile.TemporaryDirectory() as tmpdir:
        storage = BudgetStorage(Path(tmpdir) / "data.json")
        
        # Setup initial state
        storage.add_category("Food", 500.0, ["Groceries", "Eating Out"])
        storage.set_goal("Savings", target=10000.0, deadline="2026-01-01")
        storage.add_recurring_item("Rent", amount=-800.0, category_id="Housing")

        # Export to JSON string
        exported_json = storage.export()
        
        # Verify structure and content
        assert isinstance(exported_json, str)
        data = json.loads(exported_json)
        assert "categories" in data
        assert any(c["name"] == "Food" for c in data["categories"])
        assert any(g["target"] == 10000.0 for g in data.get("goals", []))

        # Create new storage instance and import back
        with tempfile.TemporaryDirectory() as tmpdir2:
            new_storage = BudgetStorage(Path(tmpdir2) / "data.json")
            
            # Simulate writing the exported string to a file then loading it (standard workflow)
            temp_file = Path(tmpdir2) / "import_test.json"
            with open(temp_file, 'w') as f:
                f.write(exported_json)
            
            new_storage.import_from_file(temp_file)

        # Verify data integrity after round-trip
        assert len(new_storage.get_categories()) == 1
        assert any(c["name"] == "Food" for c in new_storage.get_categories())
