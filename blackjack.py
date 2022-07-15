import random

def deck():
    my_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(my_deck)

def hit_me(hand):
    hand.append(deck())
    return True

def bust_checker(hand):
    hand_total = sum(hand)
    if hand_total > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                hand_total = hand_total + hand[i]
                return True
        return False

def win_21_checker(hand):
    hand_total = sum(hand)
    if hand_total == 21:
        return True

def dealer_over_16(hand):
    hand_total = sum(hand)
    if hand_total < 17:
        return True
    else:
        return False

def print_hand(player, hand):
    print("{}'s hand: {}".format(player, hand))

def play_again():
    while True:
        choice = input("Would you like to play again?\nPress 'y' for yes\nPress 'n' for no\n--> ").lower()
        if choice == 'y':
            main()
        elif choice == 'n':
            print("Bye")
            return False
        else:
            print("Please press 'y' or 'n'")

def win_message():
    print("YOU WIN")
def lose_message():
    print("YOU LOSE")
def draw_message():
    print("DRAW")

def main():
    print("Welcome to Blackjack!")
    player_name = input("What is your name? ").title()
    my_hand = []
    dealers_hand = []
    hit_me(my_hand)
    hit_me(my_hand)
    hit_me(dealers_hand)
    print_hand(player_name, my_hand)
    print_hand("Dealer", dealers_hand)
    while True:
        print("Would player like to Hit? or Stay? ")
        choice = input("Press 1 for Hit\nPress 2 for Stay\nYour choice: ")
        if choice == '1':
            hit_me(my_hand)
            print_hand(player_name, my_hand)
            print_hand("Dealer", dealers_hand)
            if win_21_checker(my_hand) == True:
                win_message()
                if play_again() == False:
                    return
            if bust_checker(my_hand) == False:
                lose_message()
                if play_again() == False:
                    return
        elif choice == '2':
            hit_me(dealers_hand)
            if dealer_over_16(dealers_hand):
                hit_me(dealers_hand)
            print_hand(player_name, my_hand)
            print_hand("Dealer", dealers_hand)
            if win_21_checker(dealers_hand) == True:
                lose_message()
                if play_again() == False:
                    return
            my_hand_total = sum(my_hand)
            dealers_hand_total = sum(dealers_hand)
            if bust_checker(dealers_hand) == False:
                win_message()
                if play_again() == False:
                    return
            if my_hand_total > dealers_hand_total:
                win_message()
                if play_again() == False:
                    return
            elif my_hand_total < dealers_hand_total:
                if bust_checker(dealers_hand) == True:
                    win_message()
                lose_message()
                if play_again() == False:
                    return
            else:
                draw_message()
                if play_again() == False:
                    return

if __name__ == '__main__':
    main()
