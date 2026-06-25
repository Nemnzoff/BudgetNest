# === Stage 34: Add support for multiple local user profiles ===
# Project: BudgetNest
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.profiles_file = self.data_dir / "profiles.json"
        if not self.data_dir.exists():
            self.data_dir.mkdir()
    
    def load_profiles(self):
        with open(self.profiles_file, 'r') as f:
            return json.load(f)
    
    def save_profile(self, name, data):
        profiles = self.load_profiles()
        profiles[name] = data
        with open(self.profiles_file, 'w') as f:
            json.dump(profiles, f, indent=2)
    
    def get_default_profile(self):
        if not os.path.exists(self.profiles_file):
            return "default"
        profiles = self.load_profiles()
        for name in ["default", *profiles.keys()]:
            if name in profiles:
                return name
        return list(profiles.keys())[0]
