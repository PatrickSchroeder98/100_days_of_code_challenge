import day_15_sources as d15


def generate_report(money):
    """Function to print the report of ingredients and money."""
    print(
        f"Water: {d15.resources['water']}ml\nMilk: {d15.resources['milk']}ml\n" +
        f"Coffee: {d15.resources['coffee']}g\nMoney: ${money}"
    )


def check_resources(choice, update):
    """Function to check if there are enough ingredients to make the coffee chosen by user or update the resources."""
    for item in d15.resources:
        try:
            if update:
                d15.resources[item] = d15.resources[item] - d15.MENU[choice]["ingredients"][item]
                continue

            if d15.resources[item] < d15.MENU[choice]["ingredients"][item]:
                print(f'Sorry there is not enough {item}.')
                return False
        except:
            # This exception is created for bypass the espresso not having 0 milk in ingredients.
            pass
    return True


def pay(choice):
    """Function to take amount of coins from user, it checks if it's sufficient amount."""
    print("Please insert coins.")
    quarters = dimes = nickles = pennies = 0
    error = True
    while error:
        try:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickles = int(input("How many nickles? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
        except:
            print("Please insert a number.")
        else:
            error = False
    total = quarters + dimes + nickles + pennies

    if total < d15.MENU[choice]['cost']:
        print(f"Sorry, the amount of money is not sufficient. Here are your ${total} back.")
        return False
    elif total > d15.MENU[choice]['cost']:
        print(f"Here is ${round(total - d15.MENU[choice]['cost'], 2)} in change.")
        return True
    else:
        return True


def start():
    """Main function of the program."""
    options = ["espresso", "latte", "cappuccino", "report", "off"]
    money = 0

    is_on = True
    while is_on:
        choice = ""
        while choice not in options:
            choice = input("What would you like? [espresso, latte, cappuccino] ")

        if choice == "report":
            generate_report(money)

        elif choice == "off":
            is_on = False

        else:
            if not check_resources(choice, False) or not pay(choice):
                continue
            money = money + d15.MENU[choice]['cost']
            check_resources(choice, True)
            print(f"Here is your {choice} ☕ Enjoy!")


if __name__ == "__main__":
    start()
