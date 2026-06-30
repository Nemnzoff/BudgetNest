# === Stage 43: Add CSV import for the primary record type ===
# Project: BudgetNest
import csv

def import_transactions(file_path):
    records = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row['amount']) if 'amount' in row else 0.0
                date_str = row.get('date', '') or ''
                records.append({
                    'id': len(records) + 1,
                    'category': row.get('category', ''),
                    'description': row.get('description', ''),
                    'amount': amount,
                    'date': date_str,
                    'type': 'transaction'
                })
            except ValueError:
                continue
    return records
