# Welcome the user to our application
print('Welcome to use our application')

# User input
money = float(input('Give money'))
purchase_cost = float(input('Purchase cost'))

change = money - purchase_cost

# Calculations and expressions
if money < purchase_cost:
    money2 = float(input('This money is not enough for this purchase, enter more money to continue purchase'))
    total_money = money + money2
    change = total_money - purchase_cost
    if total_money < purchase_cost:
        print("You don't have enough money for this item, have a good day")
    elif total_money == purchase_cost:
        print("Thank you for shopping at us today have a nice day")
    elif total_money > purchase_cost:
        print(f"Thank you for shopping at us today, here's your change {change}$ have a nice day!")
elif money > purchase_cost:
    print(f"Thank you for shopping at us today, here's your change {change}$ have a nice day!")

# Thank the user for using our application and welcome them again
print('Thank you for using our application!')
print("You're always welcome to use this application as often and as much as you want.")