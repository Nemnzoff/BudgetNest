# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: BudgetNest
def _format_currency(value: float) -> str:
    """Format a numeric value as currency string with two decimal places."""
    return f"{value:.2f}"


def _parse_date(date_str: str, format_type: str = "iso") -> datetime.date | None:
    """Parse a date string into a standard date object using the specified format type.

    Args:
        date_str: The input date string to parse.
        format_type: One of 'iso', 'us', or 'eu'. Defaults to 'iso'.

    Returns:
        A datetime.date object if parsing succeeds, otherwise None.
    """
    formats = {
        "iso": "%Y-%m-%d",
        "us": "%m/%d/%Y",
        "eu": "%d.%m.%Y"
    }
    fmt = formats.get(format_type, "%Y-%m-%d")
    try:
        return datetime.strptime(date_str.strip(), fmt).date()
    except ValueError:
        return None


def _calculate_category_balance(
    transactions: list[dict], category_name: str, date_range: tuple[datetime.date, datetime.date]
) -> float:
    """Calculate the net balance for a specific category within a given date range.

    Args:
        transactions: List of transaction dictionaries with 'amount' and 'category'.
        category_name: The name of the category to filter by.
        date_range: A tuple containing (start_date, end_date) inclusive boundaries.

    Returns:
        The sum of amounts for matching transactions within the date range.
    """
    start, end = date_range
    total = 0.0
    for tx in transactions:
        if tx.get("category") == category_name and _parse_date(tx["date"]) is not None:
            tx_date = _parse_date(tx["date"])
            if start <= tx_date <= end:
                total += float(tx["amount"])
    return total


def _generate_summary_report(transactions: list[dict], categories: dict[str, str]) -> dict[str, Any]:
    """Generate a summary report aggregating data by category.

    Args:
        transactions: List of all transaction records.
        categories: Dictionary mapping category IDs to their display names.

    Returns:
        A dictionary containing total income, total expenses, and per-category breakdowns.
    """
    income = 0.0
    expenses = 0.0
    category_totals: dict[str, float] = {}

    for tx in transactions:
        amount = float(tx["amount"])
        cat_id = tx.get("category") or "uncategorized"
        display_name = categories.get(cat_id, cat_id)

        if amount > 0:
            income += amount
        else:
            expenses -= amount

        category_totals[display_name] = category_totals.get(display_name, 0.0) + amount

    return {
        "total_income": income,
        "total_expenses": -expenses,
        "category_breakdown": category_totals
    }
