# Create a loop, which asks user a number, if number is 0 < number >= 10 loop creates and prints
# multiplication table to the user if input == 0, stop the program
# Create a variable to run
while True:
    try:
        user_input = int(input("Input number between 1-10, 0 stops the application: "))
        if 1 <= user_input <= 10:
            for x in range(0, 11):
                result = user_input * x
                print(f"{user_input} * {x} = {result}")
        elif 0 > user_input:
            raise ValueError
        elif user_input > 10:
            raise ValueError
        elif user_input == 0:
            break
    except ValueError:
        print("Wrong number format, please input number between 1-10.")
