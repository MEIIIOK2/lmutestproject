from modules.inventory import Inventory # Importing the Inventory class from inventory module
from modules.utils import show_help # Importing the show_help function from utils module

inventory = Inventory() # Creating an instance of the Inventory class
inventory.populate() # Populating the inventory with initial products
print('Welcome to the booking system terminal!')  # Displaying a welcome message
show_help() # Displaying the available commands to the user

print('You can always list all avaliable commands buy typing "help" in terminal')

while True:
    command = input('Enter command number: ').strip() # Getting user input for the command
    # Using match-case to handle different commands
    match command:
        case '1':
            inventory.show()
        case '2':
            inventory.add_product()
        case '3':
            inventory.sell_product()
        case '4':
            inventory.restock_product()
        case '5':
            inventory.show_history()
        case '6':
            inventory.show_statistics()
        case 'help':
            show_help()
        case '7':
            break # Exiting the program
        case _:
            print('Wrong command. please try again')
