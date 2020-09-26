# Circles and squares
# Each can be rendered in vector or raster form

"""
Bridge is mechanism that decouples an interface from implementation.
Bridge prevents "cartesian product" explosion.

Decouple abstraction from implementation.
Both can exist as hierarchies.
A strong from of encapsulation
"""


class Renderer:
    """interface for implementation"""
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    """implementation for drawing vector"""
    def render_circle(self, radius):
        # implement rendering
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    """implementation for drawing raster"""
    def render_circle(self, radius):
        # implement rendering
        print(f'Drawing pixels for circle of radius {radius}')


class Shape:
    """abstraction for interface"""
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    """
        interface for drawing circle.
        accepts renderer as implementation.
    """
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    """
    Any shape can be drawn by numerous renderer. ex) shape: circle, renderer: vector. 
    If shapes are 100, and renderers are 100, the possible combinations of shape and renderer are 100,000.
    the possible combinations of shape and renderer is called cartesian product.
    Bridge can decouple shape class and renderer class.
    """

    raster = RasterRenderer()
    vector = VectorRenderer()

    # feed renderer to circle class
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
