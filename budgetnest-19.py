# === Stage 19: Add undo support for the last simple mutation ===
# Project: BudgetNest
import json
from typing import List, Optional, Dict, Any

class BudgetNest:
    def __init__(self):
        self.history_stack: List[Dict[str, Any]] = []
    
    def _save_state(self) -> None:
        if len(self.history_stack) > 100:
            self.history_stack.pop(0)
        self.history_stack.append({
            'items': list(self.items),
            'goals': dict(self.goals),
            'categories': dict(self.categories),
            'recurring': dict(self.recurring)
        })
    
    def add_item(self, item: Dict[str, Any]) -> None:
        self._save_state()
        self.items.append(item)
    
    def delete_item(self, index: int) -> None:
        if 0 <= index < len(self.items):
            self._save_state()
            del self.items[index]
    
    def undo_last_change(self) -> Optional[Dict[str, Any]]:
        if not self.history_stack:
            return None
        state = self.history_stack.pop()
        self.items[:] = state['items']
        self.goals.clear()
        self.goals.update(state['goals'])
        self.categories.clear()
        self.categories.update(state['categories'])
        self.recurring.clear()
        self.recurring.update(state['recurring'])
        return state
