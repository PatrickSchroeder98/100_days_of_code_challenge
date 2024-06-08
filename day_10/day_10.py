import os
import day_10_sources as d10


def acceptNumber(message):
    """Function to accept the numbers provided by user."""
    error = True
    number = 0
    while error:
        try:
            number = float(input(message))
        except:
            print("Error! This is not a number.")
        else:
            error = False
    return number


def acceptChoice(message):
    """Function to accept the character used in the operation choice."""
    error = True
    choice = ""
    while error:
        choice = input("Choose the operation: + , - , * , / .")
        if choice not in ["+", "-", "*", "/"]:
            print("Error! This is not a valid character.")
        else:
            error = False
    return choice


def calculate(n1, n2, char):
    """Function checking which operation the user wants to perform, returns the result."""
    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }
    return operations[char](n1, n2)


def add(n1, n2):
    """Function performing adding operation, returns the result number."""
    return n1 + n2


def substract(n1, n2):
    """Function performing substracting operation, returns the result number."""
    return n1 - n2


def multiply(n1, n2):
    """Function performing multiplying operation, returns the result number."""
    return n1 * n2


def divide(n1, n2):
    """Function performing divisioning operation, returns the result number or None if it's division by zero."""
    try:
        return n1 / n2
    except:
        print("Error! Division by zero!")
        return None


def app():
    """Main function of the calculator app."""
    print(d10.calculator)
    proceed = True
    appOn = True
    n1 = acceptNumber("What is the first number?\n")

    while appOn:
        if not proceed or n1 is None:
            print("Restarting...")
            os.system("PAUSE")
            os.system('cls')
            n1 = acceptNumber("What is the first number?\n")
        n2 = acceptNumber("What is the second number?\n")
        choice = acceptChoice("Choose the operation: + , - , * , / \n")
        n1 = calculate(n1, n2, choice)
        print("Result is: " + str(n1))
        m1 = "Type 'yes' if you want to continue with current result, 'exit' to end, any character to reset. \n"
        choice = input(m1).lower() if n1 is not None else print()

        proceed = True if choice == "yes" else False
        appOn = False if choice == "exit" else True

app()