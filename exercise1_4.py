# Ask the user to input minutes
minutes = (float(input('Enter your choice of minutes')))

# 1 hour = 60 minutes, 1 minute = 1 hour / 60
hours = round(minutes / 60, 1)
remaining_minutes = round(minutes % 60,)

# Now show the result to the user
str(print(f'Your input {minutes} minutes equals to {hours}h and {remaining_minutes} minutes'))
