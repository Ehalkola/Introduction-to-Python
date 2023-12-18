# Funtion 1
# Create and define a function called show_personal_information(), which contains name, home city and profession
def show_personal_information():
    name = "Eemil Halkola"
    home_city = "Rovaniemi"
    profession = "Machine learning student"
    print(f"{name}\n{home_city}\n{profession}")
    return name, home_city, profession


# Show the information to the user
callable(show_personal_information())

# Funtion 2
# Create a function count_seconds(hours, minutes, seconds), which takes hours, minutes and seconds as parameters
# Define count_seconds(hours, minutes, seconds)
def count_seconds(hours, minutes, seconds:
    total_seconds = ((hours * 3600) + (minutes * 60) + seconds),
    return total_seconds

user_input = input("Input hours, minutes and seconds: ")
example = "2h 25min 33sec"
print(example)

for hours, minutes, seconds in user_input:
    time = user_input.split("_")
    hours = time[0]
    minutes = time[1]
    seconds = time[2]
