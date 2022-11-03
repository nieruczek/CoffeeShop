import os.path
import random

from easygui import *
from random import randint



class Money:
    def __init__(self, finance, currency, customer_name):
        self.finance = finance
        self.currency = currency
        self.customer_name = customer_name
        self.path1 = os.path.join("", "text1.txt")
        self.path2 = os.path.join("", "text2.txt")
        self.path3 = os.path.join("", "text3.txt")

    def __repr__(self):
        return f'{self.finance}, {self.currency}, {self.customer_name}'

    def get_name(self, customer_name):
        self.customer_name = customer_name
        return self.customer_name

    def set_pocket(self, currency, banknotes, change):
        line1 = banknotes
        line2 = change
        line3 = float(line1 + "." + line2)
        self.finance = line3
        return self.finance, self.currency

    def show_balance(self, finance, currency):
        self.currency = "ZLOTE"
        information2 = msgbox(f"Your balance is: {round((self.finance), 2)} {self.currency}", "Balance", "OK")
        return self.finance, self.currency

    def add_new_customer(self, path2, path3):
        new_customer_file = open(path2, "a")
        file4 = open(path3, "r")
        list1 = file4.readlines()
        file4.close()
        file4 = open(path3, "a")
        self.customer_name = str(random.randint(1, 1000))
        while self.customer_name not in list1:
            if self.customer_name in list1:
                self.customer_name = str(random.randint(1, 1000))
            else:
                file4.write(self.customer_name + "\n")
                break
        new_customer_file.write(self.customer_name + "-" + "0" + "\n")
        new_customer_file.close()
        file4.close()
        return self.customer_name


class Product(Money):
    def __init__(self, finance, currency, customer_name, cost, common):
        super(). __init__(finance, currency, customer_name)
        self.cost = cost
        self.common = common


    def __repr__(self):
        return f'{self.finance}, {self.currency}, {self.cost}'

    def add_new_item(self, path1, new_item):
        file_item = open(path1, "a")
        file_item.write("\n" + new_item[0] + "-" + new_item[1] + "." + new_item[2])
        file_item.close()
        return "OK"

    def delete_item(self, path1, item):
        stay_here = []
        file_item = open(path1, "r")
        my_del = file_item.readlines()
        for element in my_del:
            if element.startswith(item):
                pass
            else:
                stay_here.append(element)
        file_item.close()
        file_item = open(path1, "w")
        for elem in stay_here:
            file_item.write(elem)
        file_item.close()
        return "OK"

    def buy_product(self, currency, cost, choice):
        file1 = open(self.path1, "r")
        elem = file1.readlines()
        for element in choice:
            el2 = element.split("-")
            for el in elem:
                if el.startswith(el2[0]):
                    el1 = el.split("-")
                    price = el1[1]
                    cost = round((float(cost) + float(price)), 2)
        file1.close()
        information8 = msgbox(f"You have to pay: {cost} {currency}")
        if currency == "ZLOTE":
            pass
        elif currency == "DOLLARS":
            cost = float(cost) * 4.84
        elif currency == "EUROS":
            cost = float(cost) * 4.77
        elif currency == "HRIVNAS":
            cost = float(cost) * 0.13
        file3 = open(self.path2, "r")
        self.cost = round(cost, 2)
        file3.close()
        information9 = msgbox(f"{round(cost, 2)} ZLOTE will be withdrawn")
        return self.cost

    def change_balance(self, finance, cost):                                                                            #зміна балансу на картці. Баланс завжди перераховується в початкову валюту
        if cost < finance:
            self.finance = round((finance - cost), 2)
        else:
            information5 = msgbox("There is no enough money", "No money", "OK")
        return self.finance

    def common_cost(self, cost, path2, customer_name, common):                                                                                        #підраховує та записує в окремий файл загальну суму, витрачену на закупки в даному місці
        current_cost = float(cost)
        common_list = []
        new_data = []
        x = str(customer_name)
        x = x.rstrip("\n")
        file3 = open(path2, "r")
        client = file3.readlines()
        file3.close()
        for clients in client:
            if clients.startswith(x):
                new_data.append(clients.split("-"))
            else:
                common_list.append(clients)
        former_cost = round(float(new_data[0][1]), 2)
        if former_cost > 150 and former_cost < 300:
            current_cost = round((current_cost/100 * 95), 2)
            information6 = msgbox(f"Your discount is 5%\nYou have to pay only {current_cost} ZLOTE")
        elif former_cost >= 300 and former_cost < 600:
            current_cost = round((current_cost/100 * 90), 2)
            information6 = msgbox(f"Your discount is 10%\nYou have to pay only {current_cost} ZLOTE")
        elif former_cost > 600:
            current_cost = round((current_cost/100 * 85), 2)
            information6 = msgbox(f"Your discount is 15%\nYou have to pay only {current_cost} ZLOTE")
        file3 = open(self.path2, "w")
        common = current_cost + former_cost
        common = round(float(common), 2)
        file3.write(x + "-" + str(common) + "\n")
        file3.close()
        for next_element in common_list:
            file3 = open(self.path2, "a")
            file3.write(str(next_element))
            file3.close()
        return self.common




product = Product(0, "ZLOTE", 0, 0, 0)
