# Welcome the user and tell them what this application is used for
print('Welcome to use our application')
print('This app is meant for calculating your cents from 1-100')

# Ask the user how many cents do they have
total_cents = int(input('How many cents do you have'))

# Calculate the cents with the following expressions
# Print the final results to the user
# Amount of 50 cents
amount_50_cents = total_cents // 50
total_cents %= 50
print(f'Number of 50 Cent coins: {amount_50_cents}')

# Amount of 20 cents
amount_20_cents = total_cents // 20
total_cents %= 20
print(f'Number of 20 Cent coins: {amount_20_cents}')

# Amount of 10 cents
amount_10_cents = total_cents // 10
total_cents %= 10
print(f'Number of 10 Cent coins: {amount_10_cents}')

# Amount of 5 cents
amount_5_cents = total_cents // 5
total_cents %= 5
print(f'Number of 5 Cent coins: {amount_5_cents}')

# Amount of 2 cents
amount_2_cents = total_cents // 2
total_cents %= 2
print(f'Number of 2 Cent coins: {amount_2_cents}')

# Amount of 1 cents
amount_1_cents = total_cents // 1
total_cents %= 1
print(f'Number of 1 Cent coins: {amount_1_cents}')
