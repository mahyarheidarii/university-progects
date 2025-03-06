import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root
    else:
        return None

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve_quadratic(a, b, c)

if result is None:
    print("No real roots.")
elif isinstance(result, tuple):
    print(f"The real roots are: {result[0]} and {result[1]}")
else:
    print(f"The root is: {result}")
