def add(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("add", a, b))
    result = a + b
    return result


def subtract(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("subtract", a, b))
    result = a - b
    return result


def multiply(a, b, *, ctx=None):
    if ctx is not None and ctx.get("audit"):
        ctx["log"].append(("multiply", a, b))
    result = a * b
    return result
