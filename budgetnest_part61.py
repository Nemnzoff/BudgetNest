# === Stage 61: Add performance timing for core list and search operations ===
# Project: BudgetNest
import timeit


def benchmark_budget_ops():
    """Compact performance timing for core list and search operations."""
    setup = "from BudgetNest import DataStore"
    stmts = [
        "ds = DataStore()",
        "for _ in range(100): ds.add('Groceries', 50.0)",
        "for _ in range(100): ds.add('Utilities', 200.0)",
        "list_cost = timeit.timeit('list(ds)', setup=setup, number=20)",
        "item = ds.get('Groceries')",
        "search_cost = timeit.timeit('ds.search(\"G\")', setup=setup, number=10)",
        f"print(f'List  ops: {list_cost:.4f}s | Search ops: {search_cost:.5f}s')",
    ]
    for s in stmts:
        print(s)
