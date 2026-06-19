# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: BudgetNest
from datetime import datetime, timedelta
import json
import os

ARCHIVE_DIR = "archive"
def archive_records(records, days_old=365):
    cutoff = datetime.now() - timedelta(days=days_old)
    archived = [r for r in records if r.get('date', '') and datetime.fromisoformat(r['date']) < cutoff]
    active = [r for r in records if r not in archived]
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(os.path.join(ARCHIVE_DIR, "old_records.json"), 'w') as f:
        json.dump(archived, f, indent=2)
    return active

def restore_records(records):
    if not records or not os.path.exists("archive/old_records.json"):
        return records
    with open(os.path.join(ARCHIVE_DIR, "old_records.json"), 'r') as f:
        archived = json.load(f)
    return records + archived
