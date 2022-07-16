import random
import math
import time

def dictionary_of_topics():
    my_dict = {
                "4 + 7": 4+7,
                "44 - 42": 44-42,
                "e": math.e,
                "2 * 3": 2*3,
                "34^0": 34**0,
                "55/11": 55/11,
                "π": math.pi,
                "9 * 0": 9 * 0,
                "(1/2) + (1/4)": (1/2)+(1/4),
                "0 / 21": 0/21
              }
    return my_dict

def grab_random_key_value(my_dict):
    return random.choice(list(my_dict.items()))

def right_or_wrong(player_choice, random1, random2):
    if random1[1] > random2[1]:
        if player_choice == 'a':
            return True
    elif random1[1] < random2[1]:
        if player_choice == 'b':
            return True
    else:
        if player_choice == 'a' or player_choice == 'b':
            print("Same value\nSo I will say you are...")
            return True

def main():
    t0 = time.time()
    d = dictionary_of_topics()
    score = 0
    while True:
        get_random1 = grab_random_key_value(d)
        get_random2 = grab_random_key_value(d)

        # Ensures random values are never the same
        while True:
            if get_random1 == get_random2:
                get_random2 = grab_random_key_value(d)
            else:
                break
        print("What is the greater value?\na.) {}\nb.) {}".format(get_random1[0], get_random2[0]))
        while True:
            choice = input("Answer: ")
            if choice == 'a' or choice == 'b':
                break
            print("Please press 'a' or 'b'")

        if right_or_wrong(choice, get_random1, get_random2) == True:
            score += 1
            print("Correct!\nScore: {}\n".format(score))
        else:
            print("\nIncorrect\nGAME OVER\nScore: {}".format(score))
            t1 = time.time()
            total = t1 - t0
            rounded_time = round(total, 2)
            print("Total time: {}".format(rounded_time))
            return

if __name__ == '__main__':
    main()
