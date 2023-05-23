# Open Closed Principal
# Open for extension, closed for modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} - {self.color} - {self.size}"


# without OCP
class ProductFilter:
    def filter_by_color(self, products: list[Product], color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# with OCP
class BaseSpecification:
    def is_satisfied(self, item: Product):
        pass


class BaseFilter:
    def filter(self, items: list[Product], spec: BaseSpecification):
        pass


class ColorSpecification(BaseSpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

    def __and__(self, other):
        return AndSpecification(self, other)


class SizeSpecification(BaseSpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(BaseSpecification):
    def __init__(self, *specs):
        self.specs: list[BaseSpecification] = specs

    def is_satisfied(self, item: Product):
        return all(
            map(
                lambda spec: spec.is_satisfied(item),
                self.specs,
            ),
        )


class OrSpecification(BaseSpecification):
    def __init__(self, *specs):
        self.specs: list[BaseSpecification] = specs

    def is_satisfied(self, item: Product):
        return any(
            map(
                lambda spec: spec.is_satisfied(item),
                self.specs,
            ),
        )


class BetterFilter(BaseFilter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
    bike = Product("Bike", Color.RED, Size.MEDIUM)

    products = [apple, tree, house, bike]

    print("================================================")
    pf = ProductFilter()
    print("Green Products(old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p)
    print("================================================")
    spec_blue = ColorSpecification(Color.BLUE)
    spec_green = ColorSpecification(Color.GREEN)
    spec_red = ColorSpecification(Color.RED)

    spec_small = SizeSpecification(Size.SMALL)
    spec_medium = SizeSpecification(Size.MEDIUM)
    spec_large = SizeSpecification(Size.LARGE)

    bf = BetterFilter()
    print("Green Products(new):")
    for p in bf.filter(products, spec_green):
        print(p)

    print()

    print("Green Large Products:")
    spec_green_large = spec_green & spec_large
    for p in bf.filter(products, spec_green_large):
        print(p)

    print("================================================")
