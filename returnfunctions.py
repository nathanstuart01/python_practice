def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name+ ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name =input("Last name: ")
	if l_name == 'q':
		break


	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician_middle= get_formatted_name('evan', 'stuart', 'james')
print(musician_middle)

def build_person(first_name, last_name, age=''):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person 

musician_dict = build_person('jimi', 'hendrix', age=27)
print(musician_dict)



