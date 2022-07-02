print("Welcome to the tip calculator")

bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
number_of_people = int(input("How many people are to split the bill?\n"))

percent_tip = tip / 100
print(f"percent_tip: {percent_tip}")
total_tip = bill * percent_tip
print(f"total_tip: {total_tip}")
final_cost = bill + total_tip
print(f"final_cost: {final_cost}")
cost_per_person = final_cost / number_of_people
print(f"cost_per_person: {cost_per_person}")
cost_per_person_round = round(cost_per_person, 2)
final = "{:.2f}".format(cost_per_person_round)

print(f"Each person should pay : ${final}")
