from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
        if radius < 0:
            raise ValueError("Radius should be positive")
        return math.pi * radius ** 2

class Triangle(Shape):
    def area(self, a, b, c):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Sides should be positive")
        # Herons formula
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def is_right_triangle(self, a, b, c):
        sides = [a, b, c]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

# Example usage:
if __name__ == "__main__":
    circle = Circle()
    radius = 5
    print(f"Area of circle with radius {radius}: {circle.area(radius)}")

    triangle = Triangle()
    side1, side2, side3 = 3, 4, 5
    print(f"Area of triangle with sides {side1}, {side2}, {side3}: {triangle.area(side1, side2, side3)}")
    print(f"Is triangle with sides {side1}, {side2}, {side3} a right triangle? {triangle.is_right_triangle(side1, side2, side3)}")
