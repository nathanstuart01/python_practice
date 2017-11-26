from car import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_bettle = Car('volkswagen', 'bettle', 2015)
print(my_bettle.get_descriptive_name())

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

