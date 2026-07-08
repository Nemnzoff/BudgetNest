# === Stage 58: Add bulk update behavior for selected records ===
# Project: BudgetNest
def bulk_update_records(self, record_ids: List[int], updates: Dict[str, Any]) -> List[Dict]:
    """Apply common field changes to many records at once."""
    for rid in record_ids:
        if rid not in self._records:
            raise KeyError(f"Record {rid} does not exist")
        rec = self._records[rid]
        existing = dict(rec)
        for key, value in updates.items():
            existing[key] = value
        self._records[rid] = existing
    return [dict(self._records[r]) for r in record_ids]
