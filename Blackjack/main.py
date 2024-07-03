import random
options = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
draw = False
comp_win = False
user_win = False
def card_dealer():
    global options
    cards = []
    for i in range(2):
        cards.append(random.choice(options))
    return cards
def draw_cards(cards):
    cards.append(random.choice(options))
    return cards
def total_sum(cards):
    return sum(cards)
def check_for_blackjack(cards):
    if len(cards) == 2:
        if 11 in cards and 10 in cards:
            return True
    return False
def check_if_over_21(cards, sum):
    if sum > 21:
        for index in (0, len(cards) - 1):
            if cards[index] == 11:
                cards[index] = 1
                sum = total_sum(cards)
                if sum > 21:
                    return True
        return True
    return False
def keep_running():
    ans = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no: ")
    if ans == 'y':
        keep_going = True
    else:
        keep_going = False
    return keep_going

keep_going = keep_running()
while keep_going:
    print("\n"*100)

    user_cards = card_dealer()
    comp_cards = card_dealer()
    comp_sum = total_sum(comp_cards)
    user_sum = total_sum(user_cards)

    user_has_blackjack = check_for_blackjack(user_cards)
    comp_has_blackjack = check_for_blackjack(comp_cards)

    if user_has_blackjack and comp_has_blackjack:
        draw = True
    elif user_has_blackjack:
        user_win = True
    elif comp_has_blackjack:
        comp_win = True
    else:
        print(f"Here are your cards: {user_cards}. Here is your current score: {user_sum}")
        print(f"Here is the computer's first card: {comp_cards[0]}")

        more_cards = True

        while more_cards:
            ans = input("Do you want another card? Type 'y' for yes and 'n' for no: ")

            if ans == 'y':
                user_cards = draw_cards(user_cards)
                user_sum = total_sum(user_cards)
                print(f"Here are your cards: {user_cards}. Here is your current score: {user_sum}")
                print(f"Here is the computer's first card: {comp_cards[0]}")
            else:
                more_cards = False

            if user_sum >= 21 or comp_sum >= 21:
                more_cards = False

        while comp_sum < 17:
            draw_cards(comp_cards)
            comp_sum = total_sum(comp_cards)

        over_21_user = check_if_over_21(user_cards, user_sum)
        over_21_comp = check_if_over_21(comp_cards, comp_sum)

        if over_21_user:
            comp_win = True
            user_win = False
        elif over_21_comp:
            comp_win = False
            user_win = True
        elif user_sum > comp_sum:
            user_win = True
            comp_win = False
        elif comp_sum > user_sum:
            comp_win = True
            user_win = False
        else:
            draw = True
            user_win = False
            comp_win = False

    print(f"Here are your final cards: {user_cards}. Here is your final score: {user_sum}")
    print(f"Here are the computer's final cards: {comp_cards}. Here is the computer's final score: {comp_sum}")

    if user_win:
        print("You win!")
    elif comp_win:
        print("You lose.")
    else:
        print("Draw.")

    keep_going = keep_running()

