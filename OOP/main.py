from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True


money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while is_on:
    order = menu.get_items()
    choice = input((f"What would you like to order({order})"))

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)




