import sqlite3


_conn = sqlite3.connect(":memory:")
_conn.execute("CREATE TABLE users (name TEXT, password TEXT, role TEXT)")
_conn.execute("INSERT INTO users VALUES ('alice', 'hunter2', 'user')")
_conn.execute("INSERT INTO users VALUES ('root', 'toor', 'admin')")
_conn.commit()


def login(name, password):
    query = f"SELECT role FROM users WHERE name = '{name}' AND password = '{password}'"
    row = _conn.execute(query).fetchone()
    if not row:
        raise ValueError("invalid credentials")
    return row[0]


def require_admin(role):
    if role != "admin":
        raise PermissionError("admin only")


def can_read(role, key):
    if key.startswith("__"):
        return role == "admin"
    return True
