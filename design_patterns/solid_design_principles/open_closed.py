"""
Open for extension, closed for modification.
Once you created class let it be extended not modified.
"""
from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    """Not good."""
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color: yield p


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, item, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('apple', Color.GREEN, Size.SMALL)
    tree = Product('tree', Color.GREEN, Size.LARGE)
    house = Product('house', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    product_filter = ProductFilter()
    print('green products (old):')
    for p in product_filter.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green.')

    better_filter = BetterFilter()
    print('green products: (new):')
    green = ColorSpecification(Color.GREEN)
    for p in better_filter.filter(products, green):
        print(f' - {p.name} is green.')

    print('large products:')
    large = SizeSpecification(Size.LARGE)
    for p in better_filter.filter(products, large):
        print(f' - {p.name} is large.')

    print('Large blue items:')
    blue = ColorSpecification(Color.BLUE)
    large_blue = large & blue
    for p in better_filter.filter(products, large_blue):
        print(f' - {p.name} is large and blue.')