from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True


def take_order():
    global is_on
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)


while is_on:
    take_order()
