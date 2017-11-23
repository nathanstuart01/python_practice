def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'pineapple', 'extra cheese')

def make_more_pizza(size, *toppings):
	print("\nMaking a " + str(size) +
		"-inch pizze with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_more_pizza(16, 'pepperoni')
make_more_pizza(16, 'pepperoni', 'pineapple')

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)