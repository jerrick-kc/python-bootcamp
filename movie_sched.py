movies = {
    'Doctor Strange' : '1:00 P.M',
    'Spiderman' : '3:00 P.M',
    'Home Alone' : '5:00 P.M',
    'Scream' : '9:00 P.M'
}

print('The following movies will be played today:')

for i in movies:
    print(i)

selected_movie = input('What movie would you like to see the showtime for?\n')
showtime = movies.get(i)

print(i, 'will play at ', showtime)
