def secret_auction():
    empty_dict = {}
    while True:
        try:
            name = input("What is your name? ").title()
            bid = int(input("What is your bid? $"))
            empty_dict[name] = bid
            while True:
                choice = input("Is there another person bidding? ").lower()
                if choice == 'yes' or choice == 'y':
                    break
                elif choice == 'no' or choice == 'n':
                    greatest_bid = []
                    greatest_bid2 = []
                    for key in empty_dict:
                        greatest_bid.append(key)
                        greatest_bid.append(empty_dict[key])
                    for i in range(1, len(greatest_bid), 2):
                        greatest_bid2.append(greatest_bid[i])
                    # print(greatest_bid2)
                    # print(greatest_bid)
                    winner_number = max(greatest_bid2)
                    winner = ''
                    for i in range(1, len(greatest_bid)):
                        if greatest_bid[i] == winner_number:
                            winner = greatest_bid[i-1]
                    print("The winner is {} who bid ${}".format(winner, winner_number))
                    return
                else:
                    print("Unrecognized response. Try again")
                    print("Please input 'yes' or 'no'")
        except:
            print("Invalid bid. Try again")
            print("Please input a number when prompted.")

def main():
    secret_auction()

if __name__ == '__main__':
    main()
