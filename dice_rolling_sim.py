import random

def roll():
    # Rolls a random number between specified parameters
    random_roll = random.randint(1, 6)
    return random_roll

def the_game(number):
    # Function that initiates game
    list_of_players = []
    for i in range(number):
        list_of_players.append([])

    num_of_dice = int(input("How many dice do you want to play with? "))
    for i in range(len(list_of_players)):
        for j in range(num_of_dice):
            list_of_players[i].append(roll())

    list_of_totals = []

    for i in range(number):
        print("Player {}: {} = {}".format(i+1, list_of_players[i], sum(list_of_players[i])))
        list_of_totals.append(sum(list_of_players[i]))
    winning_score = max(list_of_totals)

    for i in range(len(list_of_totals)):
        if list_of_totals[i] == winning_score:
            print("Player {} wins".format(i+1))

def main():
    # Main function that handles number of players, and calls game function
    num_of_players = int(input("How many players? "))
    the_game(num_of_players)




if __name__ == '__main__':
    main()
