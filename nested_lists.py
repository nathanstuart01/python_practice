alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_1, alien_2, alien_3]

for alien in aliens:
	print(alien)

aliens_army = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens_army.append(new_alien)

for alien in aliens_army[:25]:
	print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens_army)))

for alien in aliens_army[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens_army[:30]:
	if alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
	print(alien)

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print("\n" + name.title() + "'s favorite languages are:")
	else:
		print("\n" + name.title() + "'s favorite language is:")
	for language in languages:
		print("\t" + language.title())

users = {
	'nstuart': {
		'first': 'nathan',
		'last': 'stuart',
		'location': 'slc'
	},
	'lstuart': {
		'first': 'lewis',
		'last': 'stuart',
		'location': 'slc',
	},
}

for username, user_info in users.items():
	print("\nUsername:" + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

message = input("Tell me something: ")
print(message)

