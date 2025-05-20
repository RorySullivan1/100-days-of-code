# Internal Import
import random

# External Import
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo



game_on = True
lives = len(stages) - 1
cur_stage = stages[lives]
guesses = []
missed_guesses = []

print(logo)
print("Lets play hangman!")
rand_word = random.choice(word_list)
word_status = "_" * len(rand_word)
print("I have my word! " + word_status)

while game_on:
    user_guess = input("Guess a Letter!").lower()
    if user_guess in guesses:
        print("You Guessed That!")
    else:
        guesses.append(user_guess)
        count_of_instance = rand_word.count(user_guess)
        if count_of_instance > 0:
            print("\nYes!")
            pos = 0
            for val in range(0, count_of_instance):
                pos = rand_word.find(user_guess, pos)
                word_status = word_status[:pos] + user_guess + word_status[pos + 1:]
                pos += 1
        else:
            print("\nNo!")
            missed_guesses.append(user_guess)
            lives = lives - 1
            cur_stage = stages[lives]


    print(word_status)
    if word_status == rand_word:
        print("You have Won!")
        game_on = False
    elif len(missed_guesses) == len(stages) - 1:
        print(cur_stage)
        print("You have lost!")
        game_on = False
    else:
        print(cur_stage)
        print("\nIncorrect Guesses: {}".format(missed_guesses))