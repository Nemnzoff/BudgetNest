# === Stage 13: Add file save support using a configurable path ===
# Project: BudgetNest
import os, json
from pathlib import Path
class Config:
    def __init__(self):
        self.data_dir = Path.home() / ".budgetnest"
        self.file_path = self.data_dir / "data.json"
        self.cache_file = self.data_dir / "cache.json"
    
    def ensure_dirs(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def save_data(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Save error: {e}")
            return False
            
    def load_data(self):
        if self.file_path.exists():
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {"transactions": [], "categories": {}, "goals": []}

    def save_cache(self, cache):
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache, f)
            return True
        except Exception as e:
            print(f"Cache error: {e}")
            return False
            
    def load_cache(self):
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

cfg = Config()
cfg.ensure_dirs()
