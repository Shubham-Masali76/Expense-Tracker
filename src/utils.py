# src/utils.py
from datetime import datetime
from typing import List, Dict
from tabulate import tabulate

def format_currency(amount: float) -> str:
    return f"{amount:,.2f}"

def parse_iso_date(s: str) -> datetime:
    """Parse ISO date 'YYYY-MM-DD' -> datetime. Raises ValueError if invalid."""
    return datetime.fromisoformat(s)

def pretty_print_rows(rows: List[Dict]):
    """Print list of dict rows as a nice table using tabulate (fallback to simple print)."""
    if not rows:
        print("No rows to show.")
        return
    headers = rows[0].keys()
    table = [[r[h] for h in headers] for r in rows]
    try:
        print(tabulate(table, headers=headers, tablefmt="github"))
    except Exception:
        # fallback
        for r in rows:
            print(r)
