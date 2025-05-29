from art import logo
from random import randint

def play_number_guessing_game():
    guess_allocations = {
        "E": 10,
        "M": 7,
        "H": 5
    }

    print(logo)
    print("Welcome to the Number Guessing Game!\nCan you guess a number between 0 - 100?")
    level_choice = input("Which difficulty would you like to play? Easy (E), Medium (M), Hard (H)").upper()
    guesses = guess_allocations[level_choice]

    # Generate Number
    number = randint(0, 100)
    print("I have my Number!")
    while guesses > 0:
        guess = int(input("What is your guess?"))

        if guess > number * 1.5:
            print("Way Too High!")
        elif guess > number:
            print("Too High!")

        if guess * 1.5 < number:
            print("Way Too Low!")
        elif guess < number:
            print("Too Low!")

        if guess == number:
            print(f"You got it!!\nThe number is {number}")

        guesses -= 1
        if guesses == 0:
            print(f"You lose! The number was {number}")
        else:
            print(f"Guesses Remaining: {guesses}")

play_number_guessing_game()

