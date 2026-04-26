from src.auth import can_read


class Store:
    def __init__(self):
        self.data = {}

    def get(self, key, role="user"):
        if not can_read(role, key):
            raise PermissionError(f"role={role} cannot read {key}")
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]
