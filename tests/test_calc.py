from src.audit import entries, make_ctx, reset
from src.calc import add, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_audit_records_when_enabled():
    reset()
    ctx = make_ctx(audit=True)
    add(1, 2, ctx=ctx)
    multiply(3, 4, ctx=ctx)
    log = entries()
    assert ("add", 1, 2) in log
    assert ("multiply", 3, 4) in log


def test_audit_silent_when_disabled():
    reset()
    ctx = make_ctx(audit=False)
    add(1, 2, ctx=ctx)
    assert entries() == []
