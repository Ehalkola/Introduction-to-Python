import math

# Welcome the user to our application and tell them what this application is used for
print('Welcome to use our application')
print('This application is meant for calculating plums worth in numbers with other fruits worth')

# How to calculate the fruits worth
# Apple
apple = math.sqrt(3 + 10 - 4) / 3
apple_2 = apple + + ((5 ** 3) - 5) / 20
apple_3 = round(apple + apple_2 + 3,)
print(f'An apple is worth {apple_3}')

# Cherry
cherry = 2 + 2 * 2 + 2 - 2 * 2
print(f'Cherry is worth {cherry}')

# Orange
orange = apple_3 - 9
print(f'Orange is worth {orange}')

# Banana
banana = (cherry - 10) / 3
print(f'Banana is worth {banana}')

# Pear
pear = (banana * 3 - 8) * (-1)
print(f'Pear is worth {pear}')

# The final result expression and the final result
total = apple_3 - (banana * 2) + (orange * 2) * (pear + cherry)
print(f'The total is {total}')

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want')