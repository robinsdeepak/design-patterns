from enum import Enum
import math


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * math.cos(b)
            self.y = a * math.sin(b)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point2(x, y)

    @staticmethod
    def new_polar_point(r, theta):
        return Point2(r * math.cos(theta), r * math.sin(theta))

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


p1 = Point(2, 3)
p2 = Point(10, math.pi / 6, system=CoordinateSystem.POLAR)
print(p1)
print(p2)

p3 = Point2.new_cartesian_point(2, 3)
p4 = Point2.new_polar_point(10, math.pi / 6)
print(p3)
print(p4)
