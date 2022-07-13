import random


def check_guess(guess, answer, lives):
    if guess > answer:
        print("You guessed too high")
        return lives - 1
    elif answer > guess:
        print("You guessed too low")
        return lives - 1
    else:
        print(f"You guessed correctly! The answer was {guess}")


def start_game():
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 100)
    print(f"Answer: {answer}")

    difficulty = input("What difficulty would you like to play on? Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5

    guess = 0
    while guess != answer:
        print(f"You have {lives} lives left!")

        guess = int(input("Make a guess: "))
        lives = check_guess(guess, answer, lives)

        if lives == 0:
            print(f"You ran out of lives! The number was {answer}")
            return
        elif answer != guess:
            print("Try again")


start_game()
