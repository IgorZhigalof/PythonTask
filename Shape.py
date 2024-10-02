class Shape:
    def square(self):
        return Exception("Square in Shape class has no square")

    def title(self):
        return "Abstract Shape class"

    def sqcompare(self, shape):
        return shape.square() == self.square()
