def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models =[]

while unprinted_designs:
	current_design =unprinted_designs.pop()

	print("printing model: " + current_design)
	completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)


def print_models(unprinted_designs1, completed_models1):
	while unprinted_designs1:
		current_design1 = unprinted_designs1.pop()

		print("Printing model: " + current_design1)
		completed_models1.append(current_design1)

def show_completed_models(completed_models1):
	print("\nThe following models have been printed:")
	for completed_models in completed_models1:
		print(completed_model)

unprinted_designs1 =['iphone', 'galaxy', 'nokie']
completed_models1 = []

print(unprinted_designs1, completed_models1)
show_completed_models(completed_models1)