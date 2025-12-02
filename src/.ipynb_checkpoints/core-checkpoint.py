from typing import List, Dict
from datetime import datetime

def next_id(rows: List[Dict]) -> int:
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1

def add_expense(rows: List[Dict], date: str, amount: float, category: str, desc: str) -> Dict:
    new = {
        "id": str(next_id(rows)),
        "date": date,
        "amount": f"{float(amount):.2f}",
        "category": category,
        "description": desc
    }
    rows.append(new)
    return new

def delete_expense(rows: List[Dict], id_: int) -> bool:
    initial = len(rows)
    rows[:] = [r for r in rows if int(r["id"]) != int(id_)]
    return len(rows) != initial

def edit_expense(rows: List[Dict], id_: int, updates: dict) -> bool:
    for r in rows:
        if int(r["id"]) == int(id_):
            r.update({k: str(v) for k, v in updates.items()})
            return True
    return False

def expenses_by_month(rows: List[Dict], year: int, month: int) -> List[Dict]:
    result = []
    for r in rows:
        dt = datetime.fromisoformat(r["date"])
        if dt.year == year and dt.month == month:
            result.append(r)
    return result

def summarize_by_category(rows: List[Dict], year: int, month: int) -> dict:
    month_rows = expenses_by_month(rows, year, month)
    summary = {}
    for r in month_rows:
        cat = r["category"]
        amt = float(r["amount"])
        summary[cat] = summary.get(cat, 0.0) + amt
    return summary
