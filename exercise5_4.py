# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application')

# Create a variable, which has cities (Rome, Athens, Stockholm, London, Dublin and Paris) sorted
# alphabetically
Cities = sorted(['Rome', 'Athens', 'Stockholm', 'London', 'Dublin', 'Paris'])

# Create a loop, which enumerates cities and prints them in numerical order
for index, city in enumerate(Cities, start=1):
    print(f"{index}. {city}")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want.')
