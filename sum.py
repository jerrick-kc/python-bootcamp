expenses = []
total = 0

for i in range(5):
    expenses.append(float(input('Enter an expense!')))
total = sum(expenses)

loop_total = 0

for x in expenses:
    loop_total = loop_total + x

print('Your total expenses was $', total, sep='' )

if loop_total == total:
    print('Both methods resulted in the same answer')
else:
    print('Both methods gave different answers')
