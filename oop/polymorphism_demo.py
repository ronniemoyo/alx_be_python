import math

class Shape:
    """Base class for shapes with an abstract area method."""
    
    def area(self):
        """Calculate the area of the shape. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
