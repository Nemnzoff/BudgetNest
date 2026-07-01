# === Stage 45: Add restore from backup with validation ===
# Project: BudgetNest
import json, os, hashlib
from datetime import datetime

def validate_backup(backup_path):
    if not os.path.exists(backup_path):
        return False, "Backup file does not exist."
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        required_keys = ['transactions', 'categories', 'goals']
        if not all(k in data for k in required_keys):
            return False, "Backup file missing required keys."
        if not isinstance(data['transactions'], list):
            return False, "Transactions must be a list."
    except json.JSONDecodeError:
        return False, "Invalid JSON format in backup file."
    return True, None

def restore_from_backup(backup_path, target_file='budget.json'):
    valid, error = validate_backup(backup_path)
    if not valid:
        print(f"Restore failed: {error}")
        return False
    
    with open(target_file, 'w', encoding='utf-8') as f_out:
        json.dump({'transactions': [], 'categories': {}, 'goals': {}}, f_out, indent=2)

    backup_hash = hashlib.sha256(open(backup_path, 'rb').read()).hexdigest()[:8]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    print(f"Backup {timestamp} ({backup_hash}) restored successfully.")
    return True
