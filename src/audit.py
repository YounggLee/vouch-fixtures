_log = []


def make_ctx(audit=False):
    return {"audit": audit, "log": _log}


def entries():
    return list(_log)


def reset():
    _log.clear()
