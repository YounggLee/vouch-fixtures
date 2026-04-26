import sys

from src.calc import add, multiply, subtract
from src.store import Store


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    store = Store()
    store.set("greeting", "hello")
    print(store.get("greeting"))
    print("add 2 + 3 =", add(2, 3))
    print("sub 10 - 4 =", subtract(10, 4))
    print("mul 6 * 7 =", multiply(6, 7))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
