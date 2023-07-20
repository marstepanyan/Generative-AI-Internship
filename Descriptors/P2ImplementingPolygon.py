class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.property_name} must be an int")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.property_name} must be greater than {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.property_name} must be less than {self.max_value}")
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self.property_name, None)


class Point2D:
    x = Int(min_value=0, max_value=100)
    y = Int(min_value=0, max_value=10)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError(f"{self.property_name} must be a sequence (list or tuple)")
        if self.min_length and len(value) < self.min_length:
            raise ValueError(f"length of {self.property_name} must be greater than {self.min_length}")
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"length of {self.property_name} must be less than {self.max_length}")

        for item in value:
            if not isinstance(item, Point2D):
                raise ValueError(f"all items must be of type Point2D but {item} is not")

        instance.__dict__[self.property_name] = list(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class Polygon:
    vertices = Point2DSequence(min_length=2, max_length=4)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, point):
        if not isinstance(point, Point2D):
            raise ValueError(f"element for append must be of type Point2D")
        if len(self.vertices) == Polygon.vertices.max_length:
            raise ValueError(f"cannot append, vertices length is at max")
        self.vertices.append(point)

    def __str__(self):
        return f"Polygon object with vertices {self.vertices}"


try:
    p = Polygon(Point2D(-100, 0), Point2D(0, 1), Point2D(1, 0))
except ValueError as e:
    print(e)
print()

p1 = Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(0, 1))
print(f"p1: {p1}")

p1.append(Point2D(3, 3))
print(f"p1 after append: {p1}")

try:
    p1.append((9, 9))
except ValueError as e:
    print(e)

try:
    p1.append(Point2D(9, 9))
except ValueError as e:
    print(e)
