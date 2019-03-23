import csv
import pickle
import os
from datetime import datetime

DATA = "crimes_data.csv"

reader = csv.DictReader(open(DATA, 'r'))
PICKLE_FILE = "dataDict.p"


def loadFile():
	dataDict = dict()

	instance_counter = 0
	for line in reader:
		instance_counter += 1
		dataDict[instance_counter] = line

	# delete only if file exists
	if os.path.exists(PICKLE_FILE):
	    os.remove(PICKLE_FILE)
	else:
	    pickle.dump(dataDict, open(PICKLE_FILE, "wb"))


if __name__ == '__main__':
	start_time = datetime.now()
	loadFile()
	end_time = datetime.now()
	print("Time taken to load the pickle: " + str(end_time - start_time))
