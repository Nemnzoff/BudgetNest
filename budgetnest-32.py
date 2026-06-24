# === Stage 32: Add pagination helpers for long console output ===
# Project: BudgetNest
def paginate_output(text, max_lines=15):
    """Yields chunks of text limited to max_lines."""
    lines = text.splitlines()
    while lines:
        chunk_size = min(max_lines, len(lines))
        yield '\n'.join(lines[:chunk_size])
        del lines[:chunk_size]

def print_paginated(text, title="Output", max_lines=15):
    """Prints long output in pagated chunks with separators."""
    if not text:
        return
    print(f"\n{title}")
    for chunk in paginate_output(text, max_lines):
        print(chunk)
        print("-" * 40)
