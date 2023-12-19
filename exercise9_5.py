import functions


# Create a loop to run the application
while True:
    # Create a try loop to define, deal with and inform use from invalid inputs, after this create variable to store
    # result to display to the user, this way we don't need to create print for every single result of the functions
    try:
        result = 0
        # Create an input for the user to determine the calculator type in functions
        calculator_type = int(input("Select operation (1 = box, 2 = ball, 3 = pipe, 0 = stop application):\n"))
        # Check if the input is '0' to stop the application
        if calculator_type == 0:
            print("Thank you for using for using our application!")
            break
        # Define calculator_type to be used in functions
        if calculator_type == 1:
            height = float(input("Input height of the box:\n"))
            width = float(input("Input width of the box:\n"))
            depth = float(input("Input the depth of the box:\n"))
            # Add the result into the result variable created above
            result = functions.box_volume(height, width, depth)
        # Create input for the user to input radius of the ball to be used in calculations in function
        elif calculator_type == 2:
            radius = float(input("Input the radius of the circle:\n"))
            # Add the result into the result variable created above
            result = functions.ball_volume(radius)
        # Create input for the user to input radius, length of the pipe to be used in calculations in function
        elif calculator_type == 3:
            radius = float(input("Input the radius of the pipe:\n"))
            length = float(input("Input the length of the pipe:\n"))
            # Add the result into the result variable created above
            result = functions.pipe_volume(radius, length)
        # Create a print of the result variable above to print the result of the calculation
        print(f"{result} m^3")
    except ValueError:
        print("Invalid input, please try again... Enter a number in 1-3, or 0 to stop the application")
