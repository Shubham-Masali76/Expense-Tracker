# src/__init__.py
"""
Expense Tracker package
Expose main utilities for importing in tests and external scripts.
"""
from .core import add_expense, delete_expense, edit_expense, expenses_by_month, summarize_by_category
from .storage import init_storage, read_expenses, write_expenses

__all__ = [
    "add_expense", "delete_expense", "edit_expense",
    "expenses_by_month", "summarize_by_category",
    "init_storage", "read_expenses", "write_expenses"
]
