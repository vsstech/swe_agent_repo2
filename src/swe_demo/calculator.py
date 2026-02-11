def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b


def is_even(n: int) -> bool:
    return n % 2 == 0
    
def add(a: float, b: float) -> float:
    return a+b
def substract(a: float, b: float) -> float:
    return a-b
