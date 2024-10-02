from Shape2D import Shape2D
from Shape3D import Shape3D


class Bar(Shape3D):
    base = None
    h = 0

    def __init__(self, base: Shape2D, h):
        self.base = base
        self.h = h

    def volume(self):
        return self.base.square() * self.h

    def square(self):
        return self.base.perimeter() * self.h + 2 * self.base.square()

    def title(self):
        return f"Shape: Bar. Params: base = {self.base.title()}, h = {self.h}"