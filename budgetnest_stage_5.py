# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: BudgetNest
def update_transaction(txn_id, new_data):
    """Update an existing transaction. Returns updated record or None if not found."""
    try:
        with open("transactions.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        if not rows:
            return None
        
        header = rows[0].keys()
        target_idx = header.index("id")
        
        for i, row in enumerate(rows):
            if row["id"] == str(txn_id):
                for key, value in new_data.items():
                    if key in header:
                        rows[i][key] = str(value) if not isinstance(value, (int, float)) else value
                
                with open("transactions.csv", "w", newline="") as f_out:
                    writer = csv.DictWriter(f_out, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(rows)
                
                return dict(rows[i])
        
        return None  # Record not found
        
    except FileNotFoundError:
        return None
