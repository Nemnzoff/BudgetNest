# === Stage 64: Add validation for relationship references ===
# Project: BudgetNest
def validate_references(data):
    """Validate that all relationship references in data are present."""
    errors = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and value.startswith("ref:"):
                ref_name = value[4:]
                if ref_name not in data:
                    errors.append(f"Missing reference: {value}")
    elif isinstance(data, list):
        for item in data:
            validate_references(item)
    return errors
