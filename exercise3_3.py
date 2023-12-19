# Welcome the user to our application
print('Welcome to use our application')
print('This application is meant for calculating your salary based on your hourly wage and work hours')

# User input
hours = float(input('Input your work hours'))
wage = float(input('Input your hourly wage'))

# Calculations
salary = hours * wage
if hours <= 40:
    salary1 = hours * wage
    print(f"Here's your salary {salary1}$")
elif hours > 40:
    wage2 = wage * 1.5
    ovr_tm_hours = hours - 40
    salary2 = 40 * wage + ovr_tm_hours * wage2
    print(f"Here's your salary {salary2}$")

# Thank the user for using our application and welcome them again
print('Thank you for using our application!')
print("You're always welcome to use this application as often and as much as you want.")