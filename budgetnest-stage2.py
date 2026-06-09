# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: BudgetNest
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


@dataclass
class Transaction:
    id: str
    date: date
    amount: float
    category: CategoryType
    description: str
    notes: Optional[str] = None
    is_recurring: bool = False
    recurring_interval: Optional[str] = None  # e.g., "weekly", "monthly"


@dataclass
class Goal:
    id: str
    name: str
    target_amount: float
    current_amount: float = 0.0
    deadline: Optional[date] = None
    category: Optional[CategoryType] = None


@dataclass
class ReportSummary:
    period_start: date
    period_end: date
    total_income: float = 0.0
    total_expense: float = 0.0
    balance_change: float = 0.0
    top_categories: list[str] = field(default_factory=list)


@dataclass
class BudgetConfig:
    currency: str = "RUB"
    default_category: CategoryType = CategoryType.EXPENSE
    recurring_enabled: bool = True
