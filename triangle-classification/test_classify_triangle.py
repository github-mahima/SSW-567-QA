import unittest
from classify_triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle")
        self.assertEqual(classify_triangle(5, 4, 3), "Right Triangle")

if __name__ == '__main__':
    unittest.main()