from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start():
    """Main function of the program."""
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()

    is_on = True
    while is_on:
        choice = None
        while choice is None:
            choice = input("What would you like? " + "[" + menu.get_items() + "]")
            if choice in ["report", "off"]:
                break
            else:
                choice = menu.find_drink(choice)

        if choice == "report":
            coffee.report()
            money.report()

        elif choice == "off":
            is_on = False

        else:
            if not coffee.is_resource_sufficient(choice) or not money.make_payment(choice.cost):
                continue
            coffee.make_coffee(choice)


if __name__ == "__main__":
    start()
