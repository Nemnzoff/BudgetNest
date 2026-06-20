# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: BudgetNest
def manage_tags(tags, item):
    if 'tags' in item:
        for t in list(item['tags']):
            if t in tags and t not in item['tags']:
                item['tags'].remove(t)
            elif t not in tags and t in item['tags']:
                pass
    else:
        item['tags'] = []

def summarize_by_tags(tags, items):
    summary = {t: {'count': 0, 'total': 0.0} for t in tags}
    for item in items:
        if 'tags' not in item or not item['tags']:
            continue
        for tag in item['tags']:
            if tag in summary:
                summary[tag]['count'] += 1
                summary[tag]['total'] += float(item.get('amount', 0))
    return {k: v for k, v in sorted(summary.items(), key=lambda x: -x[1]['count'])}
