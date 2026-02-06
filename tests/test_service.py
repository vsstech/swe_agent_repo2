import pytest
from swe_demo.service import create_user, deactivate_user


def test_create_user_ok():
    u = create_user(" Alice ")
    assert u["username"] == "alice"
    assert u["active"] is True


def test_create_user_empty():
    with pytest.raises(ValueError):
        create_user("   ")


def test_deactivate_user():
    u = {"username": "bob", "active": True}
    u2 = deactivate_user(u)
    assert u2["active"] is False

