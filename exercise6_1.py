# Create a variable, which stores the loops value
biggest_number = 0

x = 0
y = 5

# Create a loop, which asks user to input number 5 times and defines the biggest number in user input
while x in range(5):
    try:
        if biggest_number >= 0:
            user_input = int(input("Input number: "))
            x += 1
            if user_input > biggest_number:
                biggest_number = user_input
    except ValueError:
        print("Invalid input, please input positive numbers.")
# Print the biggest number to the user
print(f"The biggest number from user: {biggest_number}")
