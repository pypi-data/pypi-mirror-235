import math
import unittest

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
    
class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(circle.calculate_area(), 25 * math.pi)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.calculate_area(), 6.0)

    def test_right_triangle_check(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

if __name__ == "__main__":
    unittest.main()