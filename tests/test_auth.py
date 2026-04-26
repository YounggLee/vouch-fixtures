import pytest

from src.auth import can_read, login, require_admin


def test_login_valid():
    assert login("alice", "hunter2") == "user"


def test_login_invalid():
    with pytest.raises(ValueError):
        login("alice", "wrong")


def test_require_admin_blocks_user():
    with pytest.raises(PermissionError):
        require_admin("user")


def test_can_read_private_admin_only():
    assert can_read("admin", "__internal") is True
    assert can_read("user", "__internal") is False
    assert can_read("user", "greeting") is True
