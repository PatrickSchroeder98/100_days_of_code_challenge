"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""
import secrets
import day_11_sources as d11


def deal(hand):
    """Functon to append a card to hand."""
    hand.append(secrets.choice(d11.cards))


def start_game(h1, h2):
    """Function that gives two cards to the player and the dealer at the begining of game."""
    deal(h1)
    deal(h1)
    deal(h2)
    deal(h2)


def display_hand(name, hand):
    """Function to show all cards in hand."""
    print(f"{name}'s cards are: ", end="")
    print(hand)

def display_one_card(hand):
    """Function to show one card in dealer's hand."""
    print("Dealer's card is: ", end="")
    print("["+str(hand[0])+"]")

def sum(hand):
    """Function to sum the values of all cards in hand."""
    sum = 0
    for card in hand:
        sum = sum + card
    return  sum

def check(hand):
    """Function to check if Ace should be considered as 11 or 1. Also to check if the player or dealer busted."""
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    if sum(hand) > 21:
        return False
    else:
        return True

def dealer_check(hand):
    """Function to check if the dealer should hit."""
    if sum(hand) < 17:
        return False
    else:
        return True

def player_hitting(username, player_hand):
    """Function that allows player to hit."""
    hit = ""
    while hit != "no":
        hit = input("Do you want to hit? [yes, no]\n").lower()
        if hit == "yes":
            deal(player_hand)
            player_not_busts = check(player_hand)
            print("Your cards are: ", end="")
            display_hand(username ,player_hand)
            if not player_not_busts:
                return player_not_busts
    return True

def dealer_hitting(dealer_hand):
    """Function that allows dealer to hit."""
    while not dealer_check(dealer_hand):
        deal(dealer_hand)
        if not check(dealer_hand):
            return False
    return True

def gameOver():
    """Function checking if the player wants to play again."""
    play_again = ""
    while play_again != "yes" and play_again != "no":
        play_again = input("Do you want to play again? [yes, no]\n").lower()
    if play_again == "no":
        return False
    else:
        return True

def main():
    """Main function of the game."""
    print(d11.blackjack)
    username = input("Choose your username: ")
    dealername = "Dealer"
    gameOn = True

    while gameOn:
        player_hand = []
        dealer_hand = []

        start_game(player_hand, dealer_hand)

        display_hand(username, player_hand)
        display_one_card(dealer_hand)

        if not player_hitting(username, player_hand):
            display_hand(username, player_hand)
            display_hand(dealername, dealer_hand)
            print("You busted! Dealer wins.")
            gameOn = gameOver()
            continue

        if not dealer_hitting(dealer_hand):
            display_hand(username, player_hand)
            display_hand(dealername, dealer_hand)
            print("Dealer busted! You win.")
            gameOn = gameOver()
            continue

        if sum(player_hand) == sum(dealer_hand):
            display_hand(username, player_hand)
            display_hand(dealername, dealer_hand)
            print("A draw! No one wins.")
        elif sum(player_hand) > sum(dealer_hand):
            display_hand(username, player_hand)
            display_hand(dealername, dealer_hand)
            print("You have won the game!")
        else:
            display_hand(username, player_hand)
            display_hand(dealername, dealer_hand)
            print("Dealer have won the game!")

        gameOn = gameOver()

main()