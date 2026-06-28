# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: BudgetNest
def repair_data_integrity(data):
    if 'transactions' in data:
        for t in data['transactions']:
            if isinstance(t.get('amount'), str) and ',' in t['amount']:
                try:
                    t['amount'] = float(t['amount'].replace(',', ''))
                except ValueError:
                    pass
            elif not isinstance(t.get('date'), (str, type(None))) and len(str(t['date'])) > 10:
                if 'T' in str(t['date']) or '/' in str(t['date']):
                    try:
                        from datetime import datetime
                        t['date'] = datetime.strptime(str(t['date']), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                    except ValueError:
                        pass
    if 'goals' in data and 'target_amount' in data['goals']:
        for g in data['goals'].values():
            if isinstance(g.get('current'), str):
                try:
                    g['current'] = float(g['current'])
                except ValueError:
                    pass
    return data
