# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application!')

# Create a loop using while statement
print("This loop uses while statement to print numbers in range 0-50")
# Create a variable for the while and for loop
n = 0
# Create while loop, which adds +1 into the variable everytime when run and print the results to the user
while n in range(0, 51):
    print(n)
    n += 1

# Create a loop while using for statement, which prints n in range of 0, 50 (+1)
print("\n""This loop uses for statement to print numbers in range 0-50")
for n in range(0, 51):
    print(n)

# Create a variable, which stores all calculations from the loop
end_result = 0
# Create a loop which sums every number between 1-30 together using for statement, print only summary and -
# - remember to create a variable, which stores the summary, so it can be printed out for the user
print("\n""This self summarizing loop")
for numbers in range(1, 31):
    end_result += numbers
# Here is printout
print(f"Sum: {end_result}")

# Create variable for the loop below
yr = range(2005, 2011)
# Create a loop, which prints years between 2005-2010 on the same line, + 1 to 2010, because without this
# -loop only prints years between 2005-2009, print the years on the same line
print("\n""Here are years between 2005-2010:")
# Here is loop for years with printout
for yr in range(2005, 2011):
    print(yr, end=" ")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want.')