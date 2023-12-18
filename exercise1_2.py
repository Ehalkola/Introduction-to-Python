# Ask users products price without VAT
price = float(input('Give your products price without VAT'))

# Vat/Tax = 24%
VAT = 1.24

# Calculate the price with what with following expression
final_price = round(price * VAT, 2)
print(f'The final price of your product with {VAT} is {final_price}')
