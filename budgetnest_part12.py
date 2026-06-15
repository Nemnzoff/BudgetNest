# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: BudgetNest
import json, os
from pathlib import Path

def load_budget_data(file_path: str) -> dict | None:
    """Load budget JSON with robust error handling for malformed data."""
    path = Path(file_path)
    if not path.exists():
        print(f"[WARN] File not found: {file_path}")
        return {}
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError as e:
        print(f"[ERROR] Cannot read file: {e}")
        return {}

    if not content.strip():
        print("[WARN] File is empty.")
        return {}

    try:
        data = json.loads(content)
        if isinstance(data, dict):
            # Validate top-level keys exist to prevent crashes later
            required_keys = ['categories', 'goals', 'recurring']
            missing = [k for k in required_keys if k not in data]
            if missing:
                print(f"[WARN] Missing expected keys: {missing}")
            return data
        else:
            print("[ERROR] Root element must be a JSON object.")
            return {}
    except json.JSONDecodeError as e:
        error_msg = f"[CRITICAL] Invalid JSON format at line {e.lineno}, col {e.colno}: {e.msg}"
        print(error_msg)
        # Attempt to show the problematic snippet for debugging if possible
        try:
            lines = content.splitlines()
            start = max(0, e.lineno - 2)
            end = min(len(lines), e.lineno + 3)
            context = "\n".join(f"[{i}] {line}" for i, line in enumerate(lines[start:end], start=e.lineno-2))
            print(f"Context:\n{context}")
        except:
            pass
        return {}

if __name__ == "__main__":
    # Demo usage
    sample = "invalid json {"
    result = load_budget_data(sample)
    if not result:
        print("Data loaded safely (empty dict returned on error).")
