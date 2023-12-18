# Funtion 2
# Create a function count_seconds(hours, minutes, seconds), which defines hours, minutes and seconds to total seconds
def count_seconds(hours, minutes, seconds):
    total_seconds = ((hours * 3600) + (minutes * 60) + seconds)
    return total_seconds


# Create an empty list to add user input into
time = []
# Create an input to ask user for hours, minutes and seconds, add them to the list created above
user_input = input("Input hours, minutes and seconds:\n")
time.append(user_input)
# Create a for loop for time parts in user input, define hours, minutes, seconds with the help of list created above
for time_parts in time:
    time_part = time_parts.split()
    hours = time_part[0].replace("h", "")
    minutes = time_part[1].replace("min", "")
    seconds = time_part[2].replace("sec", "")
    # Create variable called result to store the output of the function
    result = count_seconds(int(hours), int(minutes), int(seconds))
    # Print the result to the user
    print(f"{result} seconds in total.")


