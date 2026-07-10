# === Stage 60: Add saved views for frequently used filters ===
# Project: BudgetNest
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def apply(self, dataset):
        result = list(dataset)
        for key, val in self.filters.items():
            result = [r for r in result if getattr(r, key) == val]
        return result

    def __repr__(self):
        return f"SavedView({self.name}, filters={self.filters})"


def save_view(view_name, filter_dict):
    view = SavedView(view_name, filter_dict)
    budget_data.views.append(view)
