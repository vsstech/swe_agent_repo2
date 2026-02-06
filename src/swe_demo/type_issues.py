from typing import List


def first_item(values: List[int]) -> int:
    return values[0]


bad: int = "not an int"  # mypy should fail

