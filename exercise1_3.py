# Ask user the length of the trip
trips_length = float(input('How long is your roadtrip?'))

# Use liters as a unit
# Average vehicles fuel consumption is 6.5l/100km
avg_fuel_consumption = 6.5 / 100

# Calculate trips total fuel consumption with users input data
total_fuel_consumption = round(avg_fuel_consumption * trips_length, 1)

# Print the total consumption to the user
print(f'The total fuel consumption of your trip is {total_fuel_consumption}l')
