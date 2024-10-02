from Shape import Shape


class Shape2D(Shape):
    def title(self):
        return "Abstract Shape2D class"

    def perimeter(self):
        return Exception("Abstract class Shape2D has ho perimeter")
