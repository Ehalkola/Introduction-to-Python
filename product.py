# Create a class called Product
class Product:
    # Create function to set default values of variables in Product, variables(name=int(-1), name=str("Name missing"),
    # category=str("Other"), price=float(0.0), campaign=bool(False))
    def __init__(self, id=int(-1), name=str("Name missing"), category=str("Other"), original_price=float(0.0),
                 campaign=bool(False)):
        self.id = id
        if name is None or len(name) <= 0:
            self.name = str("Name missing")
        else:
            self.name = name
        if category is None or len(category) <= 0:
            self.category = str("Other")
        else:
            self.category = category
        self.original_price = round(original_price, 1)
        self.campaign = campaign

    # Create function called get_price to calculate campaign_price if campaign is True, else return original_price
    def get_price(self):
        if self.campaign is True:
            campaign_discount = 10
            discount_price = ((self.original_price / 100) * campaign_discount)
            campaign_price = self.original_price - discount_price
            # Round campaign_price into
            return round(campaign_price, 2)
        else:
            return self.original_price

# Create function called print_info to print values of Product
    def print_info(self):
        if self.campaign is True:
            print(f"{self.category}: {self.name} (ID:{self.id}) - {self.get_price()}$ [CAMPAIGN PRICE]")
        else:
            print(f"{self.category}: {self.name} (ID:{self.id}) - {self.get_price()}$")

