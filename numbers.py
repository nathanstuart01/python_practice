numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = [value**2 for value in range(1,11)]
print(squares)
for value in range(1,11):
	square = value **2
	squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))

five_adder = [value + 5 for value in range(5,50)]
print(five_adder)

million = list(range(1,100000))




for value in range(3,30):
	value * 5
	print(value)

threes = list(range(3,33,3))
stus = ['nathan', 'jess', 'lewis', 'evan']
print(stus[-2:])

print("Here are the members of my family:")
for stu in stus[:4]:
	print(stu.title())

my_foods = ['pizza', 'burgers', 'burritos']

friend_foods = my_foods[:]

my_foods.append('soup')
friend_foods.append('tacos')
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("my most favorite food is:\n")
print(my_foods[:1])

for food in my_foods:
	print(food)

# values that cannot change are immutable 
# an immutable list is a tuple

dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)

dimensions =(400,50)
print(dimensions[0])

buffet_foods = ('pizza', 'burgers', 'tacos')

for food in buffet_foods:
	print(food)

