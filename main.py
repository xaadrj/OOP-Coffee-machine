from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
machine_money = MoneyMachine()
coffee_type = menu.get_items()

machine_on = True

while machine_on:
    choice = input(f"what drink do you want to order {coffee_type}? ")
    if choice == "report":
        coffee_maker.report()
        machine_money.report()
    elif choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and machine_money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
