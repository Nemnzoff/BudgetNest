# === Stage 44: Add backup creation for the data file ===
# Project: BudgetNest
import os, json, shutil, datetime
from pathlib import Path

def create_backup(data_file: str) -> bool:
    if not data_file or not os.path.exists(data_file):
        return False
    backup_dir = Path(data_file).parent / "backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = Path(data_file).stem
    target_path = backup_dir / f"{base_name}_{timestamp}.json"
    try:
        shutil.copy2(data_file, target_path)
        return True
    except Exception:
        return False
