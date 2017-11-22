def greet_user():
	"""display a simple greeting."""
	print("Hello!")

greet_user()

def greet_user_with_name(username):
	print("Hello, " + username.title() + "!")

greet_user_with_name("Evan")
greet_user_with_name("Nathan")

def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'lewis')
describe_pet(pet_name ='harry', animal_type= 'hamster')
describe_pet('harry','hamster')

def describe_pets(pet_name, animal_type='dog'):
	print("\nI have a " + animal_type)
	print("my " + animal_type + "'s name is " + pet_name.title())

describe_pets(pet_name ='willie')
describe_pets('willie')
describe_pets(pet_name= 'lewis', animal_type='cat')
