class ValidType:
    def __init__(self, attr_type):
        self._type = attr_type

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.property_name} must be of type {self._type.__name__}')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self.property_name, None)


class Int(ValidType):
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    def __init__(self):
        super().__init__(list)


class Tuple(ValidType):
    def __init__(self):
        super().__init__(tuple)


class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = Tuple()
    name = ValidType(str)

    def __init__(self, age, height, tags, favorite_foods, name):
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods
        self.name = name


# Test correct types
person1 = Person(age=25, height=1.75, tags=["Developer", "Python"], favorite_foods=("Pizza", "Sushi"), name="James")
print(f"Age: {person1.age}")
print(f"Height: {person1.height}")
print(f"Tags: {person1.tags}")
print(f"Fav foods: {person1.favorite_foods}")
print(f"Name: {person1.name}")
print()

# Test incorrect types
try:
    person1.age = 25.03
except ValueError as e:
    print(e)

try:
    person1.height = "1.75"
except ValueError as e:
    print(e)

try:
    person1.tags = ("Developer",)
except ValueError as e:
    print(e)

try:
    person1.favorite_foods = "Sushi"
except ValueError as e:
    print(e)

try:
    person1.name = 777
except ValueError as e:
    print(e)
