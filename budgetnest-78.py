# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: BudgetNest
def _format_currency(amount):
    return f"${amount:,.2f}"


def _parse_date(date_str, fmt="%Y-%m-%d"):
    try:
        return datetime.strptime(date_str.strip(), fmt)
    except ValueError:
        raise ValueError(f"Unrecognized date format for '{date_str}'")


def _validate_category(category):
    if category not in CATEGORIES:
        raise ValueError(f"'{category}' is not a valid category. Choose from {list(CATEGORIES)}")


def _validate_goal(goal_name):
    if goal_name in GOALS and GOALS[goal_name]["target"] > 0:
        return True
    raise ValueError(f"Goal '{goal_name}' has no target set.")


def _is_recurring_today(item):
    today = datetime.now().date()
    try:
        next_date = datetime.strptime(item["next_occurrence"], "%Y-%m-%d").date()
        if next_date < today:
            return False
        return next_date == today
    except (KeyError, ValueError):
        return False


def _group_transactions_by_category(transactions):
    grouped = {}
    for t in transactions:
        cat = t["category"]
        grouped.setdefault(cat, []).append(t)
    return grouped


def _compute_goal_progress(goal_name):
    if goal_name not in GOALS or GOALS[goal_name]["target"] <= 0:
        return None
    spent = sum(
        t["amount"] for t in transactions if t["category"] == "Goals" and t.get("goal") == goal_name
    )
    target = GOALS[goal_name]["target"]
    pct = (spent / target) * 100 if target > 0 else 0
    return {"name": goal_name, "spent": spent, "target": target, "percent": round(pct, 2)}


def _format_report_section(title, content):
    return f"\n{'='*40}\n{title.upper()}\n{'='*40}\n\n{content}"
