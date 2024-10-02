from Shape import Shape


class Shape3D(Shape):
    def volume(self):
        return Exception("Abstract Shape3D class has no volume")