# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: BudgetNest
def merge_imports(existing, new):
    """Merge two import lists, dropping obvious duplicates."""
    seen = set()
    merged = []
    for stmt in existing + new:
        s = stmt.strip()
        if not s or s.startswith('#'): continue
        # treat 'from X import Y' and bare 'X' as the same module when names overlap
        parts = [p.strip().lstrip('*').rstrip(',') for p in s.split(',') if ':' not in p]
        key_parts = []
        for p in parts:
            if p.startswith('import'):
                key_parts.append(p.replace('import', '').strip())
            else:
                key_parts.append(p)
        key = tuple(key_parts)
        if key and key[0].lower() not in seen:
            seen.add(key[0].lower())
            merged.append(s)
    return merged
