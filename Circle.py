import math

from Shape2D import Shape2D


class Circle(Shape2D):
    r = 0

    def __init__(self, r):
        self.r = r

    def title(self):
        return f"Shape: Circle, params: r = {self.a}"

    def square(self):
        return (self.r ** 2) * math.pi

    def perimeter(self):
        return 2 * self.r * math.pi