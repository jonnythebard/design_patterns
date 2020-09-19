# take two
from math import cos, sin


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    class Factory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polor_point(rho, theta):
            x = rho * cos(theta)
            y = rho * sin(theta)
            return Point(x, y)

    # acts as a singleton
    factory = Factory()


if __name__ == "__main__":
    # could let it use this way, but in here __init__ is supposed to
    # invoked only by new_cartesian_point or new_polor_point method.
    p = Point(1, 1)

    # this way allows me to kinda override __init__ method.
    p_1 = Point.factory.new_cartesian_point(1, 1)
    p_2 = Point.factory.new_polor_point(1, 1)