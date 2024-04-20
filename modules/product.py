class Product:

    def __init__(self, ID, name, quantity, purchase_price, sell_price) -> None:
        # Initialize the Product object with the provided attributes
        self.ID = ID  # Assigning the product ID
        self.name = name  # Assigning the product name
        self.quantity = quantity  # Assigning the quantity of the product
        self.purchase_price = purchase_price  # Assigning the purchase price of the product
        self.sell_price = sell_price  # Assigning the selling price of the product

    def __str__(self):
        # Return a string representation of the Product object
        return f'ID: {self.ID} Name: {self.name} '+ \
              f'Quantity: {self.quantity} Purchase price: {self.purchase_price} '+\
              f'Sell price: {self.sell_price}'