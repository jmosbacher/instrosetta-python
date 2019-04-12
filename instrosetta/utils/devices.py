import enum

class TestableEnum(enum.Enum):
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

def test_connection(f):
    def wrapped(self, *args, **kwargs):
        if not self.connected:
            raise ConnectionError("Device not connected.")
        return f(self, *args, **kwargs)
    return wrapped
