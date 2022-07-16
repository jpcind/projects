import random

RANDOM_NUMBER = random.randint(1,100)

def the_game(chances):
    print("Chances: {}".format(chances))
    while True:
        if chances == 0:
            print("You lose")
            print("The number was: {}".format(RANDOM_NUMBER))
            return
        guess = int(input("What is your guess? "))
        if guess < RANDOM_NUMBER:
            print("\n--Guess is too low--\n")
            chances -= 1
            print("Chances: {}".format(chances))
        elif guess > RANDOM_NUMBER:
            print("\n--Guess is too high--\n")
            chances -= 1
            print("Chances: {}".format(chances))
        else:
            print("\nWINNER WINNER CHICKEN DINNER!!!!")
            return

def main():
    print("Welcome to the guessing game!")
    print("Objective: Guess the number between 1 and 100")
    print("Easy mode - 10 chances\nHard mode - 5 chances\n")
    print("Easy or hard mode? ")
    while True:
        difficulty_level = input("Press 'e' for EASY\nPress 'h' for HARD\nYour selection: ").lower()
        if difficulty_level == 'e':
            lives = 10
            print("You have chosen baby uwu difficulty")
            break
        elif difficulty_level == 'h':
            print("Hardcore af")
            lives = 5
            break
        else:
            print("Invalid entry!")
    print()
    the_game(lives)



if __name__ == '__main__':
    main()
