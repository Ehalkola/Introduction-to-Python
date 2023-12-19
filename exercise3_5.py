# Welcome the user to our application
print('Welcome to use our application')

# User input
points = float(input("Enter your points here"))

if 0 <= points < 101:
    if points <= 50:
        print(f"Here is your grade {0}")
    elif points <= 61:
        print(f"Here is your grade {1}")
    if points <= 71:
        print(f"Here is your grade {2}")
    if points <= 81:
        print(f"Here is your grade {3}")
    elif points <= 91:
        print(f"Here is your grade {4}")
    elif points <= 100:
        print(f"Here is your grade {5}")
else:
    input("Invalid points value.")
