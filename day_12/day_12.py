import random as r
import day_12_sources as d12


def generate():
    return r.randint(1, 100)


def guess(number, rand):
    if number > rand:
        print("Too high!")
        return False
    elif number < rand:
        print("Too low!")
        return False
    else:
        print("You guessed it!")
        return True


def difficulty_level():
    while True:
        choice = input("Choose the difficulty level [easy, hard]: ")
        if choice == "easy":
            return 10
        elif choice == "hard":
            return 5
        else:
            print("Unrecognized command.")


def game():
    print(
        d12.ascii_art
        + "\n\nWelcome to  number guessing game.\nI'm thinking about a number between 1 and 100."
    )
    rand = generate()

    chances = difficulty_level()

    guessed = False
    while not guessed:
        print(f"You have {chances} chances left.")
        try:
            number = int(input("Make your guess: "))
        except:
            print("Error! Provide a number.")
            continue
        else:
            guessed = guess(number, rand)
            if not guessed:
                chances = chances - 1
                if chances == 0:
                    print("You lose!")
                    break


if __name__ == "__main__":
    game()
