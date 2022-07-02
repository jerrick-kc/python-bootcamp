import random

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
ascii_art = [rock, paper, scissors]
ROCK = 0
PAPER = 1
SCISSORS = 2

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


comp_choice = random.randint(0, 2)
print(f"The computer chose...")
print(ascii_art[comp_choice])

if your_choice >= 3 or your_choice <= -1:
    print("Your choice is invalid, the computer wins.")
else:
    print("Your choice was...")
    print(ascii_art[your_choice])

    if comp_choice == your_choice:
        print("Tie")
    elif comp_choice == ROCK and your_choice == SCISSORS:
        print("You lose")
    elif comp_choice == PAPER and your_choice == ROCK:
        print("You lose")
    elif comp_choice == SCISSORS and your_choice == PAPER:
        print("You lose")
    else:
        print("You win!!!!")
