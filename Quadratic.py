import math

def quadratic_equation(a, b, c):
    x0 = (-b + math.sqrt(b * b - 4 * a * c)) / 2/a
    x1 = (-b - math.sqrt(b * b + 4 * a * c)) / 2/a
    return x0,x1
    
    
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)