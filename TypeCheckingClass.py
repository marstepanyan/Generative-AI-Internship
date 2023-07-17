class TypeCheckingMeta(type):
    def __setattr__(cls, key, value):
        if key in cls.__dict__:
            expected_type = cls.__dict__[key]

            if not isinstance(value, expected_type):
                raise TypeError(f"Attribute '{key}' must be of type {expected_type.__name__}.")

        super(TypeCheckingMeta, cls).__setattr__(key, value)


class MyClass(metaclass=TypeCheckingMeta):
    integer_attr = int
    string_attr = str
    list_attr = list


# Incorrect type assignment - raises TypeError
try:
    MyClass.integer_attr = "wrong_type"
except TypeError as e:
    print(e)

try:
    MyClass.string_attr = 123
except TypeError as e:
    print(e)

try:
    MyClass.list_attr = "wrong_type"
except TypeError as e:
    print(e)

print(MyClass.__dict__)
print()


# Correct type assignment
MyClass.integer_attr = 73
MyClass.string_attr = "Hello"
MyClass.list_attr = [1, 2, 3]
print(MyClass.__dict__)
