rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint

choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}
# Rock < Paper < Scissors < Rock

call_for_choice = input("Choose a move! 'Rock', 'Paper', or 'Scissors'!")
user_choice = choices[call_for_choice.lower()]
cpu_choice = list(choices.keys())[randint(0, len(choices) - 1)]
cpu_choice = choices[cpu_choice]

print(cpu_choice)
print(user_choice)

if user_choice == cpu_choice:
    print("Tie!")
elif user_choice == choices["rock"]:
    if cpu_choice == choices["paper"]:
        print("You Lose!")
    elif cpu_choice == choices["scissors"]:
        print("You Win!")
elif user_choice == choices["paper"]:
    if cpu_choice == choices["scissors"]:
        print("You Lose!")
    elif cpu_choice == choices["rock"]:
        print("You Win!")
elif user_choice == choices["scissors"]:
    if cpu_choice == choices["rock"]:
        print("You Lose!")
    elif cpu_choice == choices["paper"]:
        print("You Win!")


