print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = (name1 + name2).lower()

t_count = both_names.count('t')
r_count = both_names.count('r')
u_count = both_names.count('u')
e_count = both_names.count('e')

l_count = both_names.count('l')
o_count = both_names.count('o')
v_count = both_names.count('v')

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count
love_score = str(true_count) + str(love_count)
new_score = int(love_score)

if new_score < 10 or new_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos!")
elif 40 <= new_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
