"""Classify triangles based on their side lengths."""


def classify_triangle(a, b, c):
    """Return the classification of a triangle."""
    if a == b and b == c:
        return "Equilateral"
    if a == b or a == c or b == c:
        return "Isosceles"
    if (a != b and a != c and b != c and
          not (a ** 2 + b ** 2 == c ** 2 or
               a ** 2 + c ** 2 == b ** 2 or
               b ** 2 + c ** 2 == a ** 2)):
        return "Scalene"
    if (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2):
        return "Right Triangle"
    return None
