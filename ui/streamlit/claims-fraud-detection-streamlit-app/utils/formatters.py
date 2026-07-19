from typing import Any

def format_integer(value: Any) -> str:
    return f"{int(value or 0):,}"

def format_currency(value: Any, decimals: int = 0) -> str:
    return f"${float(value or 0):,.{decimals}f}"

def format_percent(value: Any, decimals: int = 2, ratio: bool = False) -> str:
    number = float(value or 0)
    if ratio:
        number *= 100
    return f"{number:.{decimals}f}%"
