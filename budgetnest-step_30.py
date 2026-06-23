# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: BudgetNest
def parse_date(date_str: str) -> datetime.date | None:
    """Parse date string with clear error messages."""
    if not date_str.strip():
        return None
    
    formats = [
        "%Y-%m-%d",      # 2023-10-25
        "%d.%m.%Y",      # 25.10.2023 (common in RU)
        "%d/%m/%Y",      # 25/10/2023
        "%m/%d/%Y",      # US format fallback
        "%B %d, %Y",     # October 25, 2023
        "%b %d, %Y",     # Oct 25, 2023
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: YYYY-MM-DD, DD.MM.YYYY, MM/DD/YYYY.")
