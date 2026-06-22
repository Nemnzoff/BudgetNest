# === Stage 26: Add weekly summary calculations ===
# Project: BudgetNest
def calculate_weekly_summary(transactions, categories):
    week_start = datetime.now() - timedelta(days=7)
    weekly_data = defaultdict(lambda: {'income': 0, 'expense': 0, 'by_category': {}})
    
    for t in transactions:
        if t['date'] < week_start or t['amount'] == 0:
            continue
        
        cat_name = categories.get(t['category_id'], 'Uncategorized')
        
        if t['type'] == 'income':
            weekly_data[t['week_key']]['income'] += t['amount']
        else:
            weekly_data[t['week_key']]['expense'] += t['amount']
            
        cat_total = weekly_data[t['week_key']]['by_category'].setdefault(cat_name, 0)
        
        if t['type'] == 'income':
            cat_total['balance'] += t['amount']
        else:
            cat_total['balance'] -= t['amount']

    summary_list = []
    
    for week_key in sorted(weekly_data.keys()):
        data = weekly_data[week_key]
        net_flow = data['income'] - data['expense']
        
        category_breakdown = []
        for name, info in sorted(data['by_category'].items(), key=lambda x: abs(x[1]['balance']), reverse=True):
            if info['balance'] != 0:
                category_breakdown.append(f"{name}: {info['balance']:+.2f}")

        summary_list.append({
            'week': week_key,
            'total_income': data['income'],
            'total_expense': data['expense'],
            'net_flow': net_flow,
            'top_categories': category_breakdown[:3] if category_breakdown else []
        })

    return summary_list
