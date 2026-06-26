# === Stage 35: Add active user switching and user-specific records ===
# Project: BudgetNest
class UserContext:
    def __init__(self, name): self.name = name; self.records = []
    @classmethod
    def get_current(cls): return cls._current if hasattr(cls, '_current') else None
    @classmethod
    def switch_to(cls, user_name): 
        for u in cls.all_users(): 
            if u.name == user_name: cls._current = u; break
        else: raise ValueError(f"User {user_name} not found")
    @classmethod
    def all_users(cls): return list(set(u for r in sum((getattr(r, 'records', []) or [] for r in globals().get('_all_records', [])), [], []))) if hasattr(globals(), '_all_records') else [cls.get_current()]
