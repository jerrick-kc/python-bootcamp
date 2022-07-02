student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
num_student = 0

for height in student_heights:
    total_height += height
    num_student += 1

print(f"The total height is {total_height}")
print(f"The number of students is {num_student}")

avg_height = (total_height / num_student)
rounded_avg = round(avg_height)

print(f"The average height is {rounded_avg}")
