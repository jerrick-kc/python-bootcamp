import random

computer_roll = random.randint(1, 6)
guess = int(input("What do you think the computer rolled?\n"))

if computer_roll == guess:
    print("You were right! The computer rolled " + str(computer_roll))
else:
    print("You were incorrect! The computer rolled " + str(computer_roll))
