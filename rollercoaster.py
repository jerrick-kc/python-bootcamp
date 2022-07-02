print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
        bill = 5
    elif age <= 18:
        print('Please pay $7.')
        bill = 7
    elif age >= 45 and age <= 55:
        print("You get a free ride!")
    else:
        print("Please pay $12")
        bill = 12

    pic_taken = input("Would you like to purchase pictures? Reply with Y or N: ")
    if pic_taken == "Y":
        bill += 3

    print(f"Your final bill comes down to ${bill}")
else:
    print("You can't ride the rollercoaster")
