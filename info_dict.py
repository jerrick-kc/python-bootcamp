information = {
    "name": "Jerrick Kamaraj",
    "age": "14",
    "city": "Dallas"
}

for i, info in information.items():
    print(i, ':', info)

menus = {
    'breakfast': [
        {
            'name': 'Idly',
            'price': 1.00
        },
        {
            'name': 'Poori',
            'price': 2.50
        }
    ],
    'lunch': [
        {
            'name' : 'Rice',
            'price' : 1.50

        },
        {
            'name' : 'Curry',
            'price' : '2.00'
        }
    ]
}

print('For breakfast we have:')
for i in menus['breakfast']:
    print(i['name'], ' costs $', i['price'], sep='')

print('For lunch we have:')
for i in menus['lunch']:
    print(i['name'], ' costs $', i['price'], sep='')