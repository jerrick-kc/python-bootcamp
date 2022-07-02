# Write your code below this line 👇


def prime_checker(number):
    # factors = 0
    is_prime_number = True
    for i in range(2, number):
        if number % i == 0:
            # print(f"{i} is a factor of {number}")
            is_prime_number = False
    #         factors += 1
    # print(f"{number} has {factors} factors.")

    # if factors > 0:
    #     print(f"{number} isn't a prime number")
    # else:
    #     print(f"{number} is a prime number")

    if is_prime_number:
        print(f"{number} is a prime number")
    else:
        print(f"{number} isn't a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
