# Print name, birth year, bank balance and date of an update
from datetime import datetime

# Variables to print
name = "John Doe"
birth_year = "(1984)"
balance = "balance: 345"
date = "11.9.2021"
today = datetime.now()
today2 = today.strftime("%d.%m.%Y")

# Printout
print(f"{name} {birth_year}, balance: {balance} €, updated on {today2}.")
