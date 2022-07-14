import random

def hangman():
    print("Welcome to Hangman!")
    print("What kind of game would you like to play? ")
    while True:
        game_choice = int(input("Press 1 for foodies\nPress 2 for animal lovers\n"))
        if game_choice == 1:
            word_bank = ['hamburger', 'apple', 'adobo', 'broccoli', 'cookie','danish',
                         'escargot','fries','grapefruit','horchata','icecream',
                         'jello','kiwi','lemon','mayonnaise','nectarine','omelette',
                         'peanutbutter','quiche','rasberry','strawberry','taco',
                         'ube','venison','watermelon','xiaolongbao','yogurt','zapps']
            print("You have chosen Hangman - Food Edition!")
            break
        elif game_choice == 2:
            word_bank = ['axolotl','bear', 'cat', 'dog', 'elephant', 'falcon','giraffe',
                        'honeybadger', 'iguana', 'jackal','kangaroo', 'lemur',
                        'monkey','narwhal','octopus','parrot','quail','rabbit',
                        'shark','tarantula','unicorn','vulture','whale','xoloitzcuintle',
                        'yak','zebra']
            print("You have chosen Hangman - Animal Edition!")
            break
        else:
            print("Unrecognized response. Please input 1 or 2")
    chosen_word = random.choice(word_bank)
    display = []
    # print("Chosen word: {}".format(chosen_word))
    for i in chosen_word:
        display.append("_")
    print("Your word has {} letters".format(len(chosen_word)))
    print(' '.join(display))
    guessed_letters = []
    lives = 6
    while True:
        guess = input("Choose a letter: ").lower()
        for i in range(len(guessed_letters)):
            if guess == guessed_letters[i]:
                print("You already guessed that letter.")
                break
        guessed_letters.append(guess)
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess not in chosen_word:
            lives = lives - 1
            if lives == 5:
                print(hangman_character()[5])
            if lives == 4:
                print(hangman_character()[4])
            if lives == 3:
                print(hangman_character()[3])
            if lives == 2:
                print(hangman_character()[2])
            if lives == 1:
                print(hangman_character()[1])
            print("Current life: {}".format(lives))
            if lives == 0:
                print(hangman_character()[0])
                print("You have run out of lives...")
                print("The secret word is '{}'".format(chosen_word))
                print("You lose")
                try_again()
                return
        for i in range(len(chosen_word)):
            if "_" not in display:
                print(' '.join(display))
                print("The secret word is '{}'".format(''.join(display)))
                print("You win")
                try_again()
                return
        print(' '.join(display))

def try_again():
    while True:
        answer = input("Would you like to play again? ").lower()
        if answer == 'yes' or answer == 'y':
            hangman()
        elif answer == 'no' or answer == 'n':
            print("Thank you for playing!")
            return
        else:
            print("Unrecognized response. Please input yes or no")

def hangman_character():
    lives_5 = '''Huh... how did I get here??
     +---+
     |   |
     O   |
         |
         |
         |
  ==========
              '''

    lives_4 = '''Ummm... is that supposed to be my body...?
     +---+
     |   |
     O   |
     |   |
         |
         |
  ==========
              '''
    lives_3 = '''How could you... my arm!!
     +---+
     |   |
     O   |
    /|   |
         |
         |
  ==========
              '''
    lives_2 = '''MY OTHER ARM..!!
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    ==========
              '''
    lives_1 = '''Aite you better not get the next one wrong!
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
  ==========
              '''
    lives_0 = '''Bruh.
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
  ==========
              '''
    return lives_0, lives_1, lives_2, lives_3, lives_4, lives_5

def main():
    hangman()

if __name__ == '__main__':
    main()
