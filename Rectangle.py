from Shape2D import Shape2D


class Rectangle(Shape2D):
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def title(self):
        return f"Shape: Rectangle, params: a = {self.a}, b = {self.b}"

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2
