# === Stage 42: Add CSV export without external dependencies ===
# Project: BudgetNest
def export_to_csv(data, filename="budget.csv"):
    import csv
    if not data: return
    headers = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            # Convert non-string values to string safely
            clean_row = {k: str(v) if v is not None else "" for k, v in row.items()}
            writer.writerow(clean_row)
