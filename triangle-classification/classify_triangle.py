def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    elif (a != b and a != c and b != c and
          not (a ** 2 + b ** 2 == c ** 2 or
               a ** 2 + c ** 2 == b ** 2 or
               b ** 2 + c ** 2 == a ** 2)):
        return "Scalene"
    elif (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2):
        return "Right Triangle"
