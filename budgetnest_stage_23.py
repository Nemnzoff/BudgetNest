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

# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: BudgetNest
def manage_tags(tags: dict, item_id: str) -> tuple[dict, list[str]]:
    actions = []
    if tags is None:
        return {item_id: set()}, [f"Item {item_id} has no tags."]
    current = tags.get(item_id, set())
    for tag in current.copy():
        if not any(tag in str(v) for v in tags.values()):
            actions.append(f"Removing orphaned tag '{tag}'")
            del tags[item_id][tag]
    return {k: sorted(set(v)) for k, v in tags.items()}, actions

def summarize_by_tags(tags: dict) -> list[dict]:
    if not tags or all(not v for v in tags.values()):
        return []
    summary = {}
    for item_id, tag_set in tags.items():
        for tag in sorted(tag_set):
            key = f"{tag} ({item_id})"
            summary[key] = summary.get(key, 0) + 1
    return [{"category": k, "count": v} for k, v in sorted(summary.items(), key=lambda x: -x[1])]
