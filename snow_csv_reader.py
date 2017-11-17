import csv

raw_snow_file = 'altasnow70s.csv'

with open(raw_snow_file, 'rb') as f:
	area_snow = []
	reader = csv.reader(f)
	for row in reader:
		area_snow.extend(row)
		print(area_snow)

