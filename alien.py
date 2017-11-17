alien_o = {'color': 'green', 'points': 5}

print(alien_o['color'])
print(alien_o['points'])

new_points = alien_o['points']

print("You just earner " + str(new_points) + " points!")

alien_o['x_post'] = 0
alien_o['y_post'] = 25
print(alien_o)

alien_n = {}
alien_n['name'] = 'Marvin'
print(alien_n)

alien_n['name'] = 'Bennie'
print(alien_n)

alien_n['x_post'] = 0
alien_n['y_post'] = 25
alien_n['speed'] = 'fast'
print("Original x-position: " + str(alien_n['x_post']))

if alien_n['speed'] == 'slow':
	x_increment = 1
elif alien_n['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_n['x_post'] = alien_n['x_post'] + x_increment

print("New x-position: " + str(alien_n['x_post']))

del alien_n['name']
print(alien_n)

favorite_languages = {
	'nathan': 'python',
	'jess': 'ruby',
	'lewis': 'javascript',
	'scott': 'php'
}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")

print("Lewis's favorite language is " + favorite_languages['lewis'].title() + ".")

user_o = {
	'username': 'nathanstuart01',
	'first': 'nathan',
	'last': 'stuart'
}

for key, value in user_o.items():
	print("\nKey: " + key)
	print("Value: " + value)

for name in favorite_languages:
	print(name.title())

friends = ['jules', 'scott']

for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite langague is " 
			+ favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please tell us what language you love!")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")

print("The following are languages loved: ")
for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()):
	print(language.title())



