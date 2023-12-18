# Import Back from colorama, import randint from random
from colorama import Back
from random import randint

# Create a random randint for the user to guess, outside loop, so it is easier for the user
x = randint(1, 20)

# Create a loop, which asks user a number and if same as x print CONGRATULATIONS! on green back color, if lower
# than x, change back color of the print to blue and if it's higher than x, change it to red
while True:
    try:
        user_input = int(input(Back.RESET + "Guess a number between 1-20: "))
        if user_input in range(1, 20):
            if user_input == x:
                print(Back.GREEN + f"CONGRATULATIONS!")
                break
            elif user_input < x:
                print(Back.BLUE + f"You guessed too low")
            elif user_input > x:
                print(Back.RED + f"You guessed too high")
        elif user_input not in range(1, 20):
            print("Please input full numbers")
    except ValueError:
        print("Please input full numbers")
