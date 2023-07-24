class SlottedStruct(type):
    def __new__(mcs, name, bases, namespace):
        if "_dimension" in namespace:
            dimension = namespace["_dimension"]

            if not isinstance(dimension, int):
                raise ValueError("Dimension should be integer for N-dimensional point.")

            if dimension < 2:
                raise ValueError("Dimension should be more than 2 for N-dimensional point.")

            def __init__(self, *args):
                for arg in args:
                    if not isinstance(arg, int):
                        raise ValueError("Cords should be integer for N-dimensional point.")

                if len(args) != dimension:
                    raise ValueError(f"Expected {dimension} coordinates, but got {len(args)}.")
                self.cords = args

            def __eq__(self, other):
                if not isinstance(other, self.__class__):
                    return False
                return self.cords == other.cords

            def __hash__(self):
                return hash(self.cords)

            def __repr__(self):
                return f"{self.__class__.__name__}{self.cords}"

            namespace["__init__"] = __init__
            namespace["__eq__"] = __eq__
            namespace["__hash__"] = __hash__
            namespace["__repr__"] = __repr__

        print(f"For {name=} {namespace=}")

        return super().__new__(mcs, name, bases, namespace)


class Point2D(metaclass=SlottedStruct):
    _dimension = 2


class Point3D(metaclass=SlottedStruct):
    _dimension = 3


class Point4D(metaclass=SlottedStruct):
    _dimension = 4


class Point5D(metaclass=SlottedStruct):
    _dimension = 5


print()
point2d_1 = Point2D(1, 2)
point2d_2 = Point2D(3, 4)
point2d_3 = Point2D(1, 2)

point3d_1 = Point3D(1, 2, 3)
point3d_2 = Point3D(1, 2, 3)

point4d_1 = Point4D(1, 2, 3, 4)

point5d_1 = Point5D(1, 2, 3, 4, 5)

print(f"Is {point2d_1} equal to {point2d_2}: {point2d_1 == point2d_2}")
print(f"Is {point2d_1} equal to {point2d_3}: {point2d_1 == point2d_3}")
print()
print(f"{point3d_2} hashed: {hash(point3d_2)}")
print(f"{point5d_1} hashed: {hash(point5d_1)}")
print()
print(f"Is {point2d_1} equal to {point3d_1}: {point2d_1 == point3d_1}")
print()
print(f"{point3d_1=}")
print(f"{point4d_1=}")
print()
try:
    point4d_2 = Point4D(1, 2, 3)
except ValueError as e:
    print(e)

try:
    point5d_2 = Point5D(1, 2, 1.3, 4, 5.7)
except ValueError as e:
    print(e)
