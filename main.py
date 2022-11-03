import functional
from easygui import *
import os.path

choices = []
path1 = os.path.join("", "text1.txt")
file1 = open(path1, "r")
for item in file1.readlines():
    choices.append(item)
file1.close()

customers = []
file2 = open(functional.product.path3, "r")
for cust_item in file2.readlines():
    customers.append(cust_item)
file2.close()

start_program = buttonbox("What's the option?", "Starting process", ["Add new item to the Menue", "Delete item", "New customer", "Regular customer", "Nothing"])
if start_program == "Add new item to the Menue":
    new_item = multenterbox("Input new data:", "New item", ["Item's name:", "Price BANKNOTES", "Price CHANGE"])
    functional.product.add_new_item(path1=functional.product.path1, new_item=new_item)
elif start_program == "New customer":
    pocket = multenterbox("How much money in ZLOTE does customer have?", "Customer's balance", ["BANKNOTES", "CHANGE"])
    functional.product.set_pocket("ZLOTE", banknotes=pocket[0], change=pocket[1])
    functional.product.add_new_customer(path2=functional.product.path2, path3=functional.product.path3)
    functional.product.buy_product(currency=buttonbox("Choose currency for shopping:", "Currency", ["DOLLARS", "EUROS", "HRIVNAS", "ZLOTE"]),
                                   cost=functional.product.cost, choice=multchoicebox("CHOOSE!", "Menue", choices))
    functional.product.common_cost(cost=functional.product.cost, path2=functional.product.path2, customer_name=functional.product.customer_name,
                                   common=functional.product.common)
    functional.product.change_balance(finance=functional.product.finance, cost=functional.product.cost)
    functional.product.show_balance(finance=functional.product.finance, currency=functional.product.currency)
elif start_program == "Regular customer":
    pocket = multenterbox("How much money in ZLOTE does customer have?", "Customer's balance", ["BANKNOTES", "CHANGE"])
    functional.product.set_pocket("ZLOTE", banknotes=pocket[0], change=pocket[1])
    functional.product.get_name(customer_name=choicebox("Choose the customer's number: ", "CUSTOMERS", customers))
    functional.product.buy_product(
        currency=buttonbox("Choose currency for shopping:", "Currency", ["DOLLARS", "EUROS", "HRIVNAS", "ZLOTE"]),
        cost=functional.product.cost, choice=multchoicebox("CHOOSE!", "Menue", choices))
    functional.product.common_cost(cost=functional.product.cost, path2=functional.product.path2,
                                   customer_name=functional.product.customer_name,
                                   common=functional.product.common)
    functional.product.change_balance(finance=functional.product.finance, cost=functional.product.cost)
    functional.product.show_balance(finance=functional.product.finance, currency=functional.product.currency)
elif start_program == "Delete item":
    delete_choice = choicebox("CHOOSE!", "Menue", choices)
    functional.product.delete_item(path1=functional.product.path1, item=delete_choice)
else:
    pass


