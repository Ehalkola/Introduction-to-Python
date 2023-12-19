def show_personal_information():
    name = "Eemil Halkola"
    home_city = "Rovaniemi"
    profession = "Machine learning student"
    print(f"{name}")
    print(f"{home_city}")
    print(f"{profession}")


# Function 2
# Create a function count_seconds(hours, minutes, seconds), which defines hours, minutes and seconds to total seconds
def count_seconds(hours, minutes, seconds):
    total_seconds = ((hours * 3600) + (minutes * 60) + seconds)
    return total_seconds


# Funtion 3
# Create a function _magazine_serial_check(serial), which defines/checks if user input is Valid or Incorrect ISSN
def magazine_serial_check(issn_serial):
    # Check if the length of the serial is 9 and the 5th character is a dash
    if len(issn_serial) == 9 and issn_serial[4] == '-':
        # Check if the first 4 characters are numeric and the last 4 characters are alphanumeric
        if issn_serial[:4].isdigit() and issn_serial[5:].isdigit():
            return True
    else:
        return False


# Function 4
# Create a function show_number_list, which numerates participants to be sorted with the help of sorted(lambda) function
# in the code
def show_number_list(title, data):
    print(title)
    for i, participant in enumerate(data, start=1):
        print(f"{i}. {participant}")

# Function 5
import math


# Create function to calculate the volume of a box
def box_volume(height, width, depth):
    volume = height * width * depth
    return round(volume, 2)


# Create a function to calculate the volume of a ball
def ball_volume(radius):
    volume = (4 * math.pi * radius ** 3) / 3
    return round(volume, 2)


# Create function to calculate the volume of a pipe
def pipe_volume(radius, length):
    volume = math.pi * radius ** 2 * length
    return round(volume, 2)
