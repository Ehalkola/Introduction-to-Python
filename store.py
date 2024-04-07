from product import Product


# Create function called store_products, create variable called products consisting of 5 objects, for these objects
# create variables called id, name, category, original_price and boolean variable called campaign
def main():
    products = [
        Product(id=12, name="Dishwasher", category="Appliances", original_price=699, campaign=False),
        Product(id=49, name="Kitchen table", category="Furniture", original_price=1499, campaign=True),
        Product(id=76, name="Oven", category="Appliances", original_price=1899, campaign=False),
        Product(id=101, name="Mobile phone", category="Phone", original_price=499, campaign=False),
        Product(id=7, name="Coffee maker", category="Appliances", original_price=199, campaign=True)]
    # Create a display for the original order of products to the user, use for statement to get product to call
    # function called print_info to print information of each product to the user
    print("Original order of products:")
    for product in products:
        product.print_info()

    # Create a variable to sort products based on category, use lambda
    # Create print for sorted products, use for statement to call print_info()
    sorted_products = sorted(products, key=lambda x: x.category)
    print("\n" "Products sorted by category:")
    for product in sorted_products:
        product.print_info()


# Create if statement to call the main function
if __name__ == "__main__":
    main()
