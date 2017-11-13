motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(2, 'ducati')

print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

second_ownded = motorcycles.pop(1)

print(second_ownded)
print(motorcycles)


too_expensive = 'ducati'
motorcycles.insert(0,'ducati')

motorcycles.remove(too_expensive)
print(motorcycles)
print("\n A" + too_expensive.title() + " is too expensive for me.")

guests = []

guests.append('nathan')
guests.append('lewis')

print(guests)

guests.insert(2, 'evan')
print(guests)

late_guest = guests.pop(2)
print(late_guest.title() + "\nHe cannot make it.")

guests.sort()
print(guests)

guests.append('jess')
print(guests)

guest = guests


print("Original list: \n")
print(guests)
print("Here is the sorted list\n")
print(sorted(guests, reverse = True))

print(guests)
guests.reverse()
print(guests)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

locations = ['norway', 'china', 'vietnam', 'chile', 'argentina']
print(locations)

print(sorted(locations))
print(sorted(locations, reverse = True))

print(locations.sort()) 

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(magician.title() + ", that was a great trick!") 
	print(magician.title() + ", fantastic!" + magician.title() + " .\n")
	print("Thank you, everyone. That was a great magic show!") 

pizzas = ['Pepperoni and Pineapple', 'Sausage and green peppers', 'pepperoni']

for pizza in pizzas:
	print("I like " + pizza)

print("I really like all pizza so much, it's hard to choose just one!\nBut if I had to choose, Pepperoni Pineapple is my favorite")

numbers = [1,2,3,4,5]
for value in range(1,6):
	print(value)