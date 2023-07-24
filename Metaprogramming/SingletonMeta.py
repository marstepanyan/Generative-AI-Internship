class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Hundred(metaclass=SingletonMeta):
    def __init__(self):
        setattr(self, 'name', 'hundred')
        setattr(self, 'value', 100)


class Hundred1(metaclass=SingletonMeta):
    def __init__(self):
        self.name = "hundred1"
        self.value = 111


h1 = Hundred()
h2 = Hundred()
# print(h1)
# print(h2)

print(f"Is the instance of {h1.__class__.__name__} the same: {h1 is h2}")
print()

h11 = Hundred1()
h22 = Hundred1()
# print(h11)
# print(h22)

print(f"Is the instance of {h11.__class__.__name__} the same: {h11 is h22}")
