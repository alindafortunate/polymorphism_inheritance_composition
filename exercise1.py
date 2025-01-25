# Exercise 1: Single Inheritance Instruction:

# Create a base class Shape with a method calculate_area().
# Create a subclass Rectangle that inherits from Shape
# and overrides calculate_area() to calculate the area of a rectangle.


class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        print("I am calculating the area.")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle(6, 3)
print(rectangle.calculate_area())
