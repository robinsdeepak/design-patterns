import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(r, theta):
            return Point(r * math.cos(theta), r * math.sin(theta))

    factory = PointFactory()


if __name__ == "__main__":
    p1 = Point.factory.new_cartesian_point(1, 2)
    p2 = Point.factory.new_polar_point(10, math.pi / 3)
    print(p1)
    print(p2)
