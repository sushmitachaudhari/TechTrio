import csv

DATA = "crimes_data.csv"

reader = csv.DictReader(open(DATA, 'r'))

dataDict = dict()

instance_counter = 0
for line in reader:
	instance_counter += 1
	dataDict[instance_counter] = line

