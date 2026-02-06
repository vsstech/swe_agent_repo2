from swe_demo.utils import normalize_name


def create_user(username: str) -> dict:
    username = normalize_name(username)
    if not username:
        raise ValueError("username required")
    return {"username": username, "active": True}


def deactivate_user(user: dict) -> dict:
    user["active"] = False
    return user


def risky_logic(x: int) -> int:
    # intentionally weird logic to require tests
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x % 3 == 0:
        return x * 10
    return x + 5

