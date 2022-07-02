import random

choices = ['rock', 'paper', 'scissor']
comp_choice = random.choice(choices)
print(comp_choice)
user_choice = input("Pick a move. rock, paper, or scissor?\n")

if comp_choice == user_choice:
    print('TIE')
elif comp_choice == 'rock' and user_choice == 'paper':
    print('You WIN')
elif comp_choice == 'paper' and user_choice == 'scissor':
    print('WIN')
elif comp_choice == 'scissor' and user_choice == 'rock':
    print('WIN')
else:
    print('You lose')

print('you picked ' + user_choice + ', comp picked ' + comp_choice)
