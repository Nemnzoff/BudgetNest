# === Stage 24: Add grouped summaries by category or status ===
# Project: BudgetNest
def generate_grouped_summary(data, group_by='category'):
    groups = {}
    for item in data:
        key = item.get(group_by)
        if key is None: continue
        if key not in groups: groups[key] = {'in': 0, 'out': 0}
        amount = float(item['amount'])
        sign = -1 if item['type'] == 'expense' else 1
        groups[key][item['type']] += abs(amount)

    total_in = sum(g['in'] for g in groups.values())
    total_out = sum(g['out'] for g in groups.values())
    net = total_in - total_out

    print(f"\n=== Grouped Summary by {group_by} ===")
    for name, vals in sorted(groups.items()):
        status = 'balance' if group_by == 'category' else 'status'
        balance = vals['in'] - vals['out']
        bar_len = int(abs(balance) / max(total_in, total_out) * 20) if total_in or total_out else 0
        sign_char = '+' if balance >= 0 else '-'
        print(f"{name:15} | In:{vals['in']:7.2f} Out:{vals['out']:7.2f} Net:{sign_char}{balance:8.2f}")

    print("-" * 40)
    print(f"{'TOTAL':<15} | {total_in:7.2f} {total_out:7.2f} {net:+8.2f}")
