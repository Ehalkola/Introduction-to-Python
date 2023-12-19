# Ask the user to input 2 numbers, which first will be divided by the second
try:
    number1 = float(input("Give a number"))
    number2 = float(input("Give a second number"))

    # Calculation format
    result = (number1 / number2)
    print(result)
    # Solve Errors with except statements
except ValueError:
    print("Incorrect format.")
except ZeroDivisionError:
    print("You can't divide by zero.")
