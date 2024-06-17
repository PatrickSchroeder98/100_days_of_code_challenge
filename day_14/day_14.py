import os
import secrets as s
import day_14_sources as d14


def choose(indexes):
    """Function chooses the account from data, it checks if it was already chosen in this game to not repeat it."""
    index = -1
    account = ""
    drawing = True
    while drawing:
        account = s.choice(d14.data)
        index = d14.data.index(account)
        if index not in indexes:
            drawing = False
    indexes.append(index)
    return account


def view(account, position):
    """Function prints a string with information about account."""
    print(
        f"{position}: {account['name']}, a {account['description']}, from {account['country']}."
    )


def check_answer(answer, first_account, second_account):
    """Function to check if answer provided by user is correct."""
    correct_answer = "A" if first_account["follower_count"] > second_account["follower_count"] else "B"
    if answer == correct_answer:
        return True
    else:
        return False


def game():
    """Main function of the game."""
    indexes = []
    score = -1
    first_account = choose(indexes)
    gameOn = True

    while gameOn:
        os.system("cls")
        score += 1
        print(d14.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        view(first_account, "Compare A")
        print(d14.vs)
        second_account = choose(indexes)
        view(second_account, "Against B")
        answer = ""
        while answer != "A" and answer != "B":
            answer = input("Who has more followers? Type 'A' or 'B': ")
        gameOn = check_answer(answer, first_account, second_account)
        first_account = second_account
        if len(indexes) == len(d14.data):
            indexes = []

    os.system("cls")
    print(d14.logo)
    print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    game()
