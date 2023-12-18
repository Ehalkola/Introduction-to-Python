shop_cart = [
    {"name": "Beehive - lamp", "price": 999.9},
    {"name": "Malm - bed", "price": 169.9},
    {"name": "Moomin - mug set", "price": 59.9},
    {"name": "Nemo - divan", "price": 699.9},
    {"name": "Ritz - armchair", "price": 369.9}
]

# Create a variable, which stores the price from the loop to print out in the end
total_amount = 0

# Create a print for variable called receipt
print("Receipt:")

# Create a for loop, which find items, prices from shop_cart list and adds prices for variable above
for contains in shop_cart:
    contain = contains["name"]
    price = contains["price"]
    total_amount += contains["price"]
    print(f"{contain}: {price}$")

# VAT(tax) = 24%, calculate the total amount without taxes
VAT = 24
taxes = (total_amount / 100) * VAT
total_without_taxes = round(total_amount - taxes, 2)

# Create an empty print to separate items/contains from prices
print()

# Print the total amount first without, then after taxes on separate lines
print(f"Total: {total_amount}$, including taxes.\nPlease come again!")
print(f"Total: {total_without_taxes}$, excluding 24% tax.")
print(f"Taxes total: {taxes}$")
