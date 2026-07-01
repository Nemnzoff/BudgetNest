# === Stage 46: Add a schema version field and migration helper ===
# Project: BudgetNest
SCHEMA_VERSION = "1.1"

def migrate_data(data):
    if data.get("schema_version") != SCHEMA_VERSION:
        old_v = data.get("schema_version", "0.9")
        print(f"Migrating from v{old_v} to v{SCHEMA_VERSION}")
        if old_v == "0.9":
            # Add new fields with defaults for backward compatibility
            data.setdefault("goals_enabled", True)
            data.setdefault("recurring_items_enabled", False)
            data["schema_version"] = SCHEMA_VERSION
    return data
