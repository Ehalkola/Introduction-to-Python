# Import Fore, from colorama, import datetime from datetime
from colorama import Fore
from datetime import datetime

# Create a variable to store all user input years together
birth_years = []

# Create a loop, which asks and collects birth years into variable above
for x in range(5):
    birth_year = int(input(f"Input person {x + 1}: birth year: "))
    birth_years.append(birth_year)

# Create a loop, which defines birth year from birth years, defines age by calculating current time - birth year
for x in range(1):
    print("Lets process all the birth years...")
    for birth_year in birth_years:
        birth_year = birth_year.__int__()
        ages = datetime.now().year - birth_year
# Create a conditional statement, which prints ages on Green background if in range 0-125 and red if not in range
        if 0 <= ages <= 125:
            print(Fore.GREEN + f"{ages} years old, age OK!")
        else:
            print(Fore.RED + f"{ages} years old, age incorrect")
    print(Fore.RESET + f"All done!")
