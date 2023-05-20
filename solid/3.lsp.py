class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    def __str__(self) -> str:
        return f"Square(size={self._width})"

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def print_area(rc):
    w = rc.width
    rc.height = 10
    excepted = w * 10
    print(rc)
    print(f"Expected area: {excepted}, Actual area: {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(3, 4)
    print_area(rc)

    sq = Square(5)
    print_area(sq)
