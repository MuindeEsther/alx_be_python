import math

class Shape:
    def area(self):
        # This ensures subclasses must implement their own area method
        raise NotImplementedError("Subclass must implement this method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Override of Shape.area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Override of Shape.area()
