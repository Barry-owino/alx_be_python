#!/usr/bin/env python3

import math

class Shape:
    def area(self):
        """
        Calculates the area of the shape.
        Should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance.

        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """
        Initializes a Circle instance.

        :param radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2


# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


