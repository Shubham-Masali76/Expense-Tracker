import csv
from pathlib import Path
from typing import List, Dict

HEADER = ["id", "date", "amount", "category", "description"]

def init_storage(path: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        with p.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)

def read_expenses(path: str) -> List[Dict]:
    init_storage(path)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def write_expenses(path: str, rows: List[Dict]):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    