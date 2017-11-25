class Dog():

	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed

	def sit(self):
		print(self.name.title() + " is now sitting.")
		print(self.name.title() + " is sitting because he is a " + self.breed + "!")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6, 'labrador retriever')

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


your_dog =Dog('Millie', 2, 'Mixed')

print("My dog's name is " + your_dog.name + " and she is a " + your_dog.breed + " breed.")
your_dog.sit()

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.modle = model
		self.year = year

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
