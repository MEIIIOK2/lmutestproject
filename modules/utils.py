
# Basically alsmost the same helper functions
# that perform input to int/float conversions
# and check whether input value is positive.
# In some cases checks whether a value after 
# operation will stay positive or not

def validate_float_positive(input_label = None):
    valid = False
    while not valid:
            value = input(f'{input_label}')
            try: 
                value = float(value)
            except:
                continue
            if not float(value) > 0:
                continue
            valid = True
    return value

def validate_int_positive(input_label = None):
    valid = False
    while not valid:
            value = input(f'{input_label}')
            try: 
                value = int(value)
            except:
                continue
            if not int(value) > 0:
                continue
            valid = True
    return value

def validate_product_ID(input_label, products):
    valid = False
    while not valid:
        ID = input(f'{input_label}')
        try: 
            ID = int(ID)
        except:
            continue
        if not int(ID) >= 0:
            continue
        exists = False
        for product in products:
            if product.ID == ID:
                exists = True
                to_sell = product
        if exists:
            valid = True
        else:
            print('Product with such ID not found')
    return to_sell, ID

def validate_sell_amount(input_value,product):
    valid = False
    while not valid:
        amount = input(input_value)
        try:
            amount = int(amount)
        except:
            continue
        if amount < 0:
            print('Input value greater than zero')
            continue
        if product.quantity < amount:
            print(f"Can't sell more than {product.quantity}")
            continue
        valid = True
    return amount

# A helper function to display list of all awaliable commands
def show_help():
    print("""Here is a list of all avaliable commands:
1 - Show inventory
2 - Add new product
3 - Sell product      
4 - Restock product      
5 - Show transaction history      
6 - Show financial statistics
7 - Exit""")