import random
import sys

def print_gallows(strikes):
    """
    this function prints the gallows stage based on the amount of strikes
    """
    if strikes == 0:
        print("  _______\n" \
        " |/      |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes == 1:
        print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes == 2:
        print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |       |\n" \
        " |       |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes == 3:
         print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |      \|\n" \
        " |       |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes == 4:
        print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |      \|/\n" \
        " |       |\n" \
        " |\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes == 5:
        print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |      \|/\n" \
        " |       |\n" \
        " |      /\n" \
        " |\n" \
        " |\n" \
        "_|___\n")
    elif strikes >= 6:
        print("  _______\n" \
        " |/      |\n" \
        " |      (_)\n" \
        " |      \|/\n" \
        " |       |\n" \
        " |      / \ \n" \
        " |\n" \
        " |\n" \
        "_|___\n")

def game_setup():
    """
    this function sets up some of the main variables
    """
    strikes = 0
    with open("letter combinations.txt") as file:
        letter_combinations = [w.strip() for w in file.readlines()]
    random_letter_combination_that_is_totally_random_and_not_real_words = random.choice(letter_combinations)
    incorrect_guesses = []
    word_thing = ["_ "] * len(random_letter_combination_that_is_totally_random_and_not_real_words)
    return strikes, random_letter_combination_that_is_totally_random_and_not_real_words, incorrect_guesses, word_thing
    
def main_game(strikes, word, incorrect_guesses, word_thing):
    """
    this is the main game loop where the gallows get updated and it displays the incorrect guesses and word and lets you guess
    """
    word_list = []
    guesses = 0
    for letter in word:
        word_list.append(letter.lower())
    while True:
        yea = False
        print_gallows(strikes)
        print("Incorrect guesses: ", end="")
        for idx, letter in enumerate(incorrect_guesses):
            if idx != len(incorrect_guesses)-1:
                print(f"{letter}, ", end="")
            else:
                print(letter)
        print()
        print("Word: ", end="")
        for letter in word_thing:
            print(f"{letter}", end = "")
        print("\n")
        for letter in word_thing:
            if letter == "_ ":
                break
        else:
            print(f"You win! You guessed the word in {guesses} guesses!")
            return
        if strikes == 6:
            print(f"You lost! The word was {word.upper()}.")
            return
        check = 0
        while True:
            guess = input("Guess a letter: ").lower()
            for thing in incorrect_guesses:
                if guess == thing:
                    check = 1
                else:
                    continue
            if len(guess) > 1:
                print("Please enter a valid input")
            elif guess == "":
                print("Please enter a valid input")
            elif check == 1:
                print("please enter a letter you haven't guessed yet")
                check = 0
            else:
                try:
                    int(guess)
                except ValueError:
                    break
        guesses += 1
        for idx, letter in enumerate(word_list):
            if word_list[idx] == guess:
                yea = True
                word_list[idx] = "_"
                word_thing[idx] = guess + " "
        if yea == False:
            incorrect_guesses.append(guess)
            strikes += 1
            yea = False

def main():
    """
    runs the functions to setup the game and start the game loop
    also checks if the user wants to play/play again
    """
    while True:
        play = input("do you wanna play my awesome game: ")
        if play.lower().strip() == "y" or play.lower().strip() == "yes" or play.lower().strip() == "n" or play.lower().strip() == "no":
            if play.lower().strip() == "y" or play.lower().strip() == "yes":
                playy = "yes"
                break
            else:
                print("ok bye")
                sys.exit()
        else:
            pass
    if playy == "yes":
        while True:
            strikes, word, incorrect_guesses, word_thing = game_setup()
            main_game(strikes, word, incorrect_guesses, word_thing)
            while True:
                play = input("do you wanna play my awesome game again: ")
                if play.lower().strip() == "y" or play.lower().strip() == "yes" or play.lower().strip() == "n" or play.lower().strip() == "no":
                    if play.lower().strip() == "y" or play.lower().strip() == "yes":
                        break
                    else:
                        print("ok bye")
                        sys.exit()
                else:
                    pass

if __name__ == "__main__":
    main()