from modules.product import Product # Importing the Product class
from modules.utils import validate_float_positive, validate_int_positive, \
    validate_product_ID, validate_sell_amount # Importing validation functions from utils module

class Inventory:

    # Initializing the Inventory class with default values
    def __init__(self):  
        self.products = []  # List to store products
        self.revenue = 0  # Total revenue earned
        self.costs = 0  # Total costs incurred
        self.next_ID = 0  # Next available ID for a new product
        self.history = []  # List to store transaction history
    
    def populate(self):  # Method to populate the inventory with initial products
        products = [
            Product(0, 'Apples', 10, 10, 12),
            Product(1, 'Berries', 50, 4, 5),
            Product(2, 'Banabas', 26, 11, 12),
            Product(3, 'Celery', 40, 7, 9),
            Product(4, 'Redis', 2, 6, 17),
            Product(5, 'Pineapple', 4, 30, 55),
            Product(6, 'Watermelon', 5, 26, 41),
            Product(7, 'Strawberry', 40, 2, 4),
            Product(8, 'Cherry', 100, 4, 5),
            Product(9, 'Carrot', 17, 15, 17),
        ]
        self.products = products
        for product in products:

             # Calculating total costs and updating next_ID
            self.costs = product.quantity* product.purchase_price
            self.next_ID +=1
            
    # Method to register a transaction in the history
    def register_tranasction(self, operation_type, amount, product):
        self.history.append({
            'type':operation_type,
            'amount': amount,
            'product': product
        })

    # Method to display the transaction history
    def show_history(self):

        # Dictionary mapping operation types to user-friendly strings
        operation_types={
            'add':'Bought',
            'sell':'Sold',
            'restock': 'Restocked'
        }
        if len(self.history) == 0:
            print('Transaction history is empty')
            return
        # Displaying each transaction in the history in history is not empty
        for i, transaction in enumerate(self.history,0):
            product:Product = transaction['product']
            print(f'{i+1}) {operation_types[transaction['type']]} {transaction['amount'] } '+\
                  f'{product.name} - ID {product.ID}')
        print('\n')

    # Method to display financial statistics
    def show_statistics(self):
        filter = input("Enter product ID's separated by whitespace. Enter to skip ")
        if filter: # Checking if a filter is provided by the user
            try:
                filter = filter.split(' ') # Splitting the input into a list of IDs
                filter = [int(num) for num in filter] # Converting IDs to integers
            except:
                print('wrong input format. Skipping filter')
                filter = None
        inventory_value = 0
        value_msg = 'Total inventory value: '
        # Calculating total inventory value based on filter
        for product in self.products:
            if filter:
                value_msg = 'Inventory value for selected products: '
                if product.ID in filter:
                    inventory_value += product.purchase_price * product.quantity
        
        print(f'Total revenue:{self.revenue}\n'+\
              f'Total costs: {self.costs}\n'+\
              f'Total profit: {self.revenue - self.costs}\n'+\
              f'{value_msg}{inventory_value}')
        print('\n')

    # Method to display all products in the inventory
    def show(self): 
        for product in self.products:
            print(product)
        print('\n')
    
    # Method for adding a product to inventory
    def add_product(self) -> None:
        name = input('Please input product name: ')
        quantity = validate_int_positive('Please input quantity: ')
        purchase_price = validate_float_positive('Please input purchase price: ')
        sell_price = validate_float_positive('Please input sell price: ')
        # Creating instance of a product and addint it to inventory
        product = Product(self.next_ID, name, quantity, purchase_price, sell_price)       
        self.products.append(product)
        self.costs += quantity * purchase_price
        self.next_ID+=1
        self.register_tranasction('add',quantity,product) # Adding transaction to history
        print('\n')

    # Method for selling a product 
    def sell_product(self) -> None:
        
        to_sell, ID = validate_product_ID('Please input product ID: ', self.products)
        amount = validate_sell_amount('Please input amount to sell: ', to_sell)

        # Macthing product by id
        for product in self.products:
            if product.ID == ID:
                product.quantity -= amount
                self.revenue += amount * product.sell_price
        self.register_tranasction('sell',amount,to_sell) # Adding transaction to history
        print('\n')
        
    # Method for restocking a product 
    def restock_product(self)-> None:
        to_restock, ID = validate_product_ID('Please input product ID: ', self.products)
        amount = validate_int_positive('Please input amount to sell: ')

        # Macthing product by id
        for product in self.products:
            if product.ID == ID:
                product.quantity += amount
                self.costs += amount * product.purchase_price
        self.register_tranasction('restock',amount,to_restock) # Adding transaction to history
        print('\n')

