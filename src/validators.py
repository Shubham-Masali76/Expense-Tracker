from datetime import datetime

def validate_date(s: str) -> bool:
    try:
        datetime.fromisoformat(s)
        return True
    except Exception:
        return False

def validate_amount(s: str) -> bool:
    try:
        float(s)
        return True
    except Exception:
        return False
