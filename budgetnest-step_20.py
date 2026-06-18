# === Stage 20: Add duplicate detection for newly created records ===
# Project: BudgetNest
def detect_duplicates(new_record, all_records):
    if new_record['name'].lower() in [r['name'].lower() for r in all_records]:
        return True
    if new_record.get('category') and any(r.get('category', '').lower() == new_record['category'].lower() 
                                          and abs(r.get('amount', 0) - new_record.get('amount', 0)) < 1e-9 
                                          for r in all_records):
        return True
    if new_record.get('goal') and any(r.get('goal', '').lower() == new_record['goal'].lower() 
                                      and abs(r.get('target_amount', 0) - new_record.get('target_amount', 0)) < 1e-9 
                                      for r in all_records):
        return True
    if new_record.get('frequency') and any(r.get('frequency', '').lower() == new_record['frequency'].lower() 
                                           and abs(r.get('next_date', None) - new_record.get('next_date')) < 1e-9 
                                           for r in all_records):
        return True
    if new_record.get('description') and any(new_record['description'].lower() in r.get('description', '').lower() or 
                                             r.get('description', '').lower() in new_record['description'].lower() 
                                             for r in all_records):
        return True
    return False
