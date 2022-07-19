import random

from highlow_art import logo
import game_data

# print logo and welcome statements
print(logo)


def generate_celeb(a_data):
    # create function called 'generate celeb' to randomly generate a username (key) so you can easily pull out the key
    # value pair
    return random.choice(a_data)


def save_info(acc):
    # create a new function and save the randomly generated info to 'A' and 'B' and print the info
    name = acc["name"]
    description = acc["description"]
    country = acc["country"]
    return f"name: {name}, {description}, {country}"


def check_answer(guess, followers_1, followers_2):
    # create another function that checks the user's guess and returns whether they answered correctly or not
    if followers_1 > followers_2:
        answer = "A"
    else:
        answer = "B"
    if answer == guess:
        return 'correct'
    else:
        return 'incorrect'


# create a score variable to keep track of score
# create a boolean that it True until the game stops
# generate the two random accounts that will be compared first


def game():
    is_game_running = True
    score = 0

    while is_game_running:
        if score == 0:
            account_a = generate_celeb(game_data.data)
        account_b = generate_celeb(game_data.data)

        while account_a == account_b:
            account_b = generate_celeb(game_data.data)

        print(f"Option A: {save_info(account_a)}, Followers: {account_a['follower_count']}M")
        print(f"Option B: {save_info(account_b)}")
        print("")

        guess = input("Who do you think has more followers? 'A' or 'B': ")
        followers_1 = account_a['follower_count']
        followers_2 = account_b['follower_count']
        answer = check_answer(guess, followers_1, followers_2)

        if answer == 'correct':
            score += 1
            print("")
            print(f"Correct! Score: {score}")
            print("")
            if guess == 'B':
                account_a = account_b
        else:
            print(f"Incorrect! Score: {score}")
            is_game_running = False

        print(f"Option B followers: {account_b['follower_count']}M")
        print("------------------------------------------------------")


game()
