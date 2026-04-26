def add(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("add", a, b))
    value = a + b
    return value


def subtract(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("subtract", a, b))
    value = a - b
    return value


def multiply(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("multiply", a, b))
    value = a * b
    return value
