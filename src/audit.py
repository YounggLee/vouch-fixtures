"""Append-only audit log for calc operations."""

_log = []


def make_ctx(audit=False):
    """Build an audit context. Pass to calc functions via the ctx kwarg."""
    return {"audit": audit, "log": _log}


def entries():
    """Snapshot of recorded operations as a list of tuples."""
    return list(_log)


def reset():
    """Clear the log. Used by tests."""
    _log.clear()
