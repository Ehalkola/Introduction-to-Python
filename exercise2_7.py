import math


# Create a function called solve_quadratic_equation, solve quadratic equation based on user input
def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if the discriminant >= 0, for real solutions of quadratic equation
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)

        # Crate conditional statements to check how many roots there is in discriminant, return the roots to print
        # them to the user
        if x1 == x2:
            return x1  # If x1 == x2 discriminant has only one real solution, return x1
        else:
            return x1, x2  # Return both variables if discriminant has two real roots
    else:
        return None  # If there are no real roots for the discriminant return None

# Create input for the user to input the values of variables in discriminant
a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
c = float(input("Input the value of c: "))

# Create variable solutions to call the results of function above
solutions = solve_quadratic_equation(a, b, c)

# Create a display of solutions for the user with the help of conditional statements, isinstance and tuple
if solutions:
    if isinstance(solutions, tuple):
        print(f"The solutions for x are: {solutions[0]} and {solutions[1]}")
    else:
        print(f"The solution for x in quadratic equation: {solutions}")
else:
    print("The quadratic equation has no real solutions...")
