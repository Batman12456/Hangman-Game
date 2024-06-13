import random
# from guess import suggest_next_letter, play_move
from your_solution import suggest_next_letter_sol

"""
This file is the Hangman game. 
Please do not edit this file in any case or you might not be able to test you code.
You need to implement your logic in guess.py in suggest_next_letter function.
However you should go through this code too for better understanding of the mechanics of the game.
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sample",type=bool)
parser.add_argument("--play",type=bool)



def choose_word(filename):
    """choosing random word samples
    """
    with open(filename, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

def display_word(word, guessed_letters):
    """
    word display for terminal

    """
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman(filename, guess_func):
    """
    actual logic of the game.
    """
    word = choose_word(filename)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word by guessing a letter at a time. You have 6 attempts.")
    print(display_word(word, guessed_letters))

    while attempts_left > 0:
        guess = guess_func(display_word(word, guessed_letters), guessed_letters)
        print(f"You guessed the letter: {guess}")
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            attempts_left -= 1
            print("Attempts left:", attempts_left)
            print(' '*45)
            continue

        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts_left -= 1

        print(display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word.")
            return 1

        print("Attempts left:", attempts_left)
        print(' '*45)

    print("Out of attempts! The word was:", word)
    return 0

if __name__ == "__main__":
    args = parser.parse_args()
    
    # if args.play:
    # hangman("C:\\Users\\Rohan Sharma\\Desktop\\Mosaic-24-main\\Mosaic PS2\\training.txt", play_move)
    # elif args.sample:
    # hangman("training.txt", suggest_next_letter)  
    # correct = 0
    # a = 1001
    # for a in range(0 ,a):
    #     i = hangman("C:\\Users\\Rohan Sharma\\Desktop\\Mosaic-24-main\\Mosaic PS2\\training.txt", suggest_next_letter_sol)
    #     if i==1:
    #         correct = correct+1
    # accuracy = correct/(a-1)
    # print(accuracy)

    hangman("C:\\Users\\Rohan Sharma\\Desktop\\Mosaic-24-main\\Mosaic PS2\\training.txt", suggest_next_letter_sol)