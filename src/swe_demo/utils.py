import os  # unused import


def normalize_name(name: str) -> str:
    # intentionally bad formatting and redundant logic
    if name == None:  # noqa: E711 (also bad practice)
        return ""
    name = name.strip()
    if len(name) == 0:
        return ""
    return name.lower()


def very_long_function(n: int) -> int:
    # intentionally long and repetitive to simulate "needs refactor"
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += i
        else:
            total += i * 2

    for j in range(n):
        if j % 2 == 0:
            total += j
        else:
            total += j * 2

    return total

