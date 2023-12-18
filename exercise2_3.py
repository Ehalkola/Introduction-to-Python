# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application!')
print('This application is meant to calculate how much of your salary goes to yourself and how much goes towards taxes')

# Ask user their salary and tax percentage
salary = float(input('Input your salary'))
tax = float(input('Input your tax percentage'))

# Use the following expression to calculate how much goes towards taxes and how much goes to the user
final_salary = round(salary - (salary * tax) / 100, 2)
final_taxes = round((salary * tax / 100), 2)

# Print the final result to the user
print(f"From your {salary}$ salary, you get to keep {final_salary}$ yourself and {final_taxes}$ goes towards taxes")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want!')