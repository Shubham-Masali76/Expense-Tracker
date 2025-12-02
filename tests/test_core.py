from src import core

def sample_rows():
    return [
        {"id":"1","date":"2025-12-01","amount":"100.00","category":"food","description":"x"},
        {"id":"2","date":"2025-12-02","amount":"200.50","category":"fuel","description":"y"},
    ]

def test_add_and_next_id():
    rows = sample_rows()
    new = core.add_expense(rows, "2025-12-05", 50, "misc", "note")
    assert new["id"] == "3"
    assert any(r["id"] == "3" for r in rows)

def test_delete_edit_summary():
    rows = sample_rows()
    deleted = core.delete_expense(rows, 1)
    assert deleted is True
    assert len(rows) == 1

    rows = sample_rows()
    edited = core.edit_expense(rows, 2, {"category": "groceries", "amount": "300"})
    assert edited is True
    assert any(r["category"] == "groceries" for r in rows)

def test_expenses_by_month_and_summary():
    rows = sample_rows()
    subset = core.expenses_by_month(rows, 2025, 12)
    assert len(subset) == 2
    summary = core.summarize_by_category(rows, 2025, 12)
    assert "food" in summary and "fuel" in summary
    assert abs(summary["food"] - 100.0) < 1e-6
