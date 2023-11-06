#
#
# Project BlackJack- Console Game
#
#
import random
from art import logo

user_cards = []
dealer_cards = []


def deal_cards():
    deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck_cards)
    return card


def round1(first_user_card, dictionary):
    for chosen_player in dictionary:
        card1 = deal_cards()
        card2 = deal_cards()
        dictionary[chosen_player].append(card1)
        dictionary[chosen_player].append(card2)
        if chosen_player == "user":
            print(f"Your cards: {first_user_card}, current score {sum(first_user_card)}")
        elif chosen_player == "dealer":
            print(f"Computer's first card: {card1}")


# round2(user turn) - user chooses whether he wants another card
#          YES- give him a card, show total sum. Repeat round2. if sum greater than 21 end loop.
#          NO - skip loop
def user_turn(u_cards):
    """Let's the user choose whether to draw another card or no.
    """
    still_hit = True
    while still_hit == True:
        user_choice = input("Type 'y' to get another card, or 'n' to pass.\n")
        if user_choice == "y":
            new_card = deal_cards()
            u_cards.append(new_card)
            for x in u_cards:
                if x == 11 and sum(u_cards) > 21:
                    index = u_cards.index(x)
                    u_cards[index] = 1
            print(f"Your cards: {u_cards}, current score {sum(u_cards)}")
            if sum(u_cards) > 21:
                still_hit = False
                return sum(u_cards)
        elif user_choice == "n":
            still_hit = False
            return sum(user_cards)


# round3(dealer turn)- until he reaches sum 17 keep dealing. return sum.
def dealers_turn(d_cards):
    while sum(d_cards) < 17:
        d_cards.append(deal_cards())
    for x in d_cards:
        if x == 11 and sum(d_cards) > 21:
            index = d_cards.index(x)
            d_cards[index] = 1
    return sum(d_cards)


# round4 - check greater scores
def decider(d_user_cards, d_dealer_cards):
    if sum(d_user_cards) > sum(d_dealer_cards):
        display(d_user_cards, d_dealer_cards)
        print("You Win")
    elif sum(d_user_cards) < sum(d_dealer_cards):
        display(d_user_cards, d_dealer_cards)
        print("You lose")
    else:
        display(d_user_cards, d_dealer_cards)
        print("Draw")


# round5 - display user and dealer cards and total
def display(final_user_cards, final_dealer_cards):
    print(f"Your final cards: {final_user_cards}, final score: {sum(final_user_cards)}")
    print(f"Computer cards: {final_dealer_cards}, final score: {sum(final_dealer_cards)}")


def final():
    u_cards = []
    d_cards = []
    players = {
        "user": u_cards,
        "dealer": d_cards
    }
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n")
    if play == "y":
        round1(u_cards, players)
        total_user_sum = user_turn(u_cards)
        if total_user_sum > 21:
            display(u_cards, d_cards)
            print("You went over, You lose")
        else:
            total_dealer_sum = dealers_turn(d_cards)
            if total_dealer_sum > 21:
                display(u_cards, d_cards)
                print("Computer went over, You win")
            else:
                decider(u_cards, d_cards)
        final()
    else:
        print("Thank you for playing. Good bye")


print(logo)
final()
