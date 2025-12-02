from pathlib import Path
import tempfile
import os
from src import storage

def test_init_and_read_write(tmp_path):
    p = tmp_path / "data" / "expenses.csv"
    storage.init_storage(str(p))
    assert p.exists()

    rows = [
        {"id":"1","date":"2025-01-01","amount":"100.00","category":"food","description":"d"}
    ]
    storage.write_expenses(str(p), rows)
    read = storage.read_expenses(str(p))
    assert isinstance(read, list)
    assert len(read) == 1
    assert read[0]["id"] == "1"
