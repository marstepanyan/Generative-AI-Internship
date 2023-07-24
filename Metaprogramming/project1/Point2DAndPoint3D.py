class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"


class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"


point1 = Point2D(1, 1)
point2 = Point2D(0, 1)
point3 = Point2D(1, 1)

print(f"Is {point1} equal to {point2}: {point1 == point2}")
print(f"Is {point1} equal to {point3}: {point1 == point3}")
print(f"{point1} hashed: {hash(point1)}, {point2} hashed: {hash(point2)}, {point3} hashed: {hash(point3)}")
print()

point11 = Point3D(1, 1, 1)
point22 = Point3D(0, 1, 2)
point33 = Point3D(1, 1, 1)

print(f"Is {point11} equal to {point22}: {point11 == point22}")
print(f"Is {point11} equal to {point33}: {point11 == point33}")
print(f"{point11} hashed: {hash(point11)}, {point22} hashed: {hash(point22)}, {point33} hashed: {hash(point33)}")
print()

print(f"Is {point11} equal to {point2}: {point11 == point2}")
