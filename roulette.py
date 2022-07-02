import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)

number_of_people = len(names)
rand_choice = random.randint(0, number_of_people - 1)
person_chosen = names[rand_choice]
print(f"{person_chosen} is going to buy the meal today! ")
