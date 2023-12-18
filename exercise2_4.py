# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application!')
print('This application is for calculating your gas consumption total within and outside of urban area')

# Ask the user the kilometers inside
km_outside = float(input('How many kilometers did you drive outside of urban area'))
km_inside = float(input('How many kilometers did you drive inside of urban area'))

# Average fuel consumption in urban area is 5.1l, out of urban area it's 7.5l
avg_fuel_consumption_out = 5.1 / 100
avg_fuel_consumption_in = 7.5 / 100

# Use the following expressions to calculate the total fuel consumption in and out of urban area
total_fuel_consumption_out = round(avg_fuel_consumption_out * km_outside, 2)
total_fuel_consumption_in = round(avg_fuel_consumption_in * km_inside, 2)
total_fuel_consumption = round(total_fuel_consumption_out + total_fuel_consumption_in, 2)

# Print the fuel consumption within and out of urban area for the user
print(f"Fuel consumption is {total_fuel_consumption_in}l within and {total_fuel_consumption_out}l out of urban area")

# Print the total consumption to the user
print(f"The total fuel consumption of the trip is {total_fuel_consumption}l")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want!')