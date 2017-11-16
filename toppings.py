requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("adding mushrooms")
elif 'pepperoni' in requested_toppings:
	print("adding pepperoni")
elif 'extra cheese' in requested_toppings:
	print("adding extra cheese")

print("\nFinished making your pizza!")

alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
	points = 10
	print("You are a green monsters, " + str(points))
elif 'yellow' in alien_color:
	points = 5
	print("You are just a yellow ol alien" + points)
else:
	points = 0
	print("You are every thing else")
	
available_topping = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_topping = ['mushrooms', 'french fries', 'extra cheese']

for requested_top in requested_topping:
	if requested_top in available_topping:
		print("Adding " + requested_top + ".")
	else:
		print("sorry, we don't have " + requested_top + ".")

print("\nFinished making your pizza!")

usernames = ['admin', 'lewis', 'evan', 'jess']

new_usernames =['lewis', 'sturat']

for new_users in new_usernames:
	if new_users in usernames:
		print("Sorry you will need to find another username, that one is already taken")
	else:
		print("Creating your username:" + new_users)







