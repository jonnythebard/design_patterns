"""
You should be able to substitute a base type for a subtype.

Following implementation violates liskov substitution principle.
In this case, Square should be implemented the other way
rather than getting inherited from Rectangle class.
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def ues_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    ues_it(rc)

    sq = Square(5)
    ues_it(sq)  # not working properly
