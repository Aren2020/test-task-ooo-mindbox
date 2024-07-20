import unittest
from shapes import Circle, Triangle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle()
        self.assertAlmostEqual(circle.area(1), 3.141592653589793, places = 6)
        self.assertAlmostEqual(circle.area(0), 0.0, places = 6)
        with self.assertRaises(ValueError):
            circle.area(-1)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle()
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6.0, places = 6)
        self.assertAlmostEqual(triangle.area(6, 8, 10), 24.0, places = 6)
        with self.assertRaises(ValueError):
            triangle.area(-3, 4, 5)
    
    def test_is_right_triangle(self):
        triangle = Triangle()
        self.assertTrue(triangle.is_right_triangle(3, 4, 5))
        self.assertTrue(triangle.is_right_triangle(6, 8, 10))
        self.assertFalse(triangle.is_right_triangle(5, 12, 14))

if __name__ == "__main__":
    unittest.main()
