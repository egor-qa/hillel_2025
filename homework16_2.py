from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rhombus(Figure):
    def __init__(self, diag_a, diag_b):  # diagonal = diag
        self.diag_a = diag_a
        self.diag_b = diag_b

    def area(self):
        return (self.diag_a * self.diag_b) / 2

    def perimeter(self):
        # Side of a rhombus = sqrt((diag_a/2)^2 + (diag_b/2)^2)
        side = math.sqrt((self.diag_a / 2) ** 2 + (self.diag_b / 2) ** 2)
        return 4 * side

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * 2 * self.radius

figures = [
    Rhombus(7, 6),
    Square(5),
    Rectangle(2, 6),
    Triangle(4, 7, 9),
    Circle(8)
]

for figure in figures:
    if isinstance(figure, Rhombus):
        print("Rhombus:")
    elif isinstance(figure, Square):
        print("Square:")
    elif isinstance(figure, Rectangle):
        print("Rectangle:")
    elif isinstance(figure, Triangle):
        print("Triangle:")
    elif isinstance(figure, Circle):
        print("Circle:")
    else:
        print("Figure:")

    print(f"Area: {figure.area()}")
    print(f"Perimeter: {figure.perimeter()}")