# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application!')

# Create a valuable, where the loop will be added for the calculation
storage = 0

# Create valuable for months 12 + 1
months = 12

# Create a loop, which asks user 12 times the rain amount of each month to calculate the average,
# + 1 to the months, so it will calculate correctly, create printout for the result after loop
try:
    for x in range(months):
        rain_amount = float(input("Input the rain amount of the month in millimeters: "))
        storage += rain_amount
except ValueError:
    print("Invalid input please input numbers.")

# Create a statement, which calculates the average rain amount from storage, print it to the user
avg = round(storage / months, 2)
print(f"Year average for rain: {avg} mm")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want.')
