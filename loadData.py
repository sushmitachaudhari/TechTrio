import csv
import pickle
import os
from datetime import datetime
import json
import math
from datetime import date
import calendar
import time
import urllib.request

DATA = "crimes_data.csv"

reader = csv.DictReader(open(DATA, 'r'))
PICKLE_FILE = "dataDict.p"
TEXTFILE_FOR_DATA_TO_BE_PARSED = "apiData.json"
ZONE_RANGE = 0.005
DEPT_DATE = date.today() # Have set it to default, needs to be updated
URL_TO_BE_SCRAPED = 'https://maps.googleapis.com/maps/api/directions/json?origin=42.361361,-71.062872&destination=42.358853,-71.067669&departure_time=1553433312&alternatives=true&mode=walking&key=AIzaSyDPVk3oxRMd1zHE8VrK0hLsJNo2_6kCTiM'


def loadFileIntoPickle():

	global reader
	global PICKLE_FILE

	dataDict = dict()

	instance_counter = 0
	for line in reader:
		instance_counter += 1
		dataDict[instance_counter] = line
	# print(len(dataDict))

	# delete only if file exists
	if os.path.exists(PICKLE_FILE):
	    os.remove(PICKLE_FILE)
	else:
	    pickle.dump(dataDict, open(PICKLE_FILE, "wb"))


def parseDataSet(source, destination, dept_time):

	'''
	Output: List[(lat1, lon1), ...)] 
	'''
	# tentative_time = timeFormat(dept_time) # check for the format matching
	# Obtain the list of locations that lie in the zone, where crimes occurred on that day of the week
	global DEPT_DATE
	tentative_dept_day = calendar.day_name[DEPT_DATE.weekday()]

	dataset = pickle.load(open(PICKLE_FILE, "rb")) # Unpickle the pickle
	TIME_RANGE = 21600
	crime_locations = list() # List of tuples of geolocation 

	xMax, xMin, yMax, yMin = obtainWalkingRange(source, destination)
	# print(xMax, xMin, yMax, yMin)
	
	for i in range(1, len(dataset)):
		location = dataset[i]['Location'].strip('(').strip(')').split(",")
		loc_x = float(location[0])
		loc_y = float(location[1])

		day = dataset[i]['DAY_WEEK']
		time_of_crime = timeFormat(dataset[i]['FROMDATE'])
		higher_time_range = dept_time + TIME_RANGE
		lower_time_range = dept_time - TIME_RANGE
		'''
		Filter crime location based on : +/- 6 hours from the tentative time of departure in the 
		crime dataset and then check if the location lies in the range of the zone range.
		'''

		if higher_time_range >= dept_time and dept_time >= lower_time_range:
			if ((loc_x <= xMax) and (xMin <= loc_x)) and ((yMin <= loc_y) and (loc_y <= yMax)):
				crime_locations.append(location)
		
	return crime_locations


def timeFormat(date_time):

	pattern = '%m/%d/%Y %I:%M:%S %p' # Update this based on user's input
	# print(out_time)
	epoch = int(time.mktime(time.strptime(date_time, pattern))) + 3000
	# print(epoch)
	return epoch


def obtainWalkingRange(source, destination):

	global ZONE_RANGE
	'''
	Use the user's source and destination, offset it and return the range.
	'''
	# print(source)
	# print(destination)
	x1 = source[0]
	x2 = destination[0]
	y1 = source[1]
	y2 = destination[1]

	xMax = max(x1, x2) + ZONE_RANGE
	xMin = min(x1, x2) - ZONE_RANGE
	yMax = max(y1, y2) + ZONE_RANGE
	yMin = min(y1, y2) - ZONE_RANGE

	return xMax, xMin, yMax, yMin


def parseDataFromAPI(URL_TO_BE_SCRAPED):

	with urllib.request.urlopen(URL_TO_BE_SCRAPED) as url:
		text = json.loads(url.read().decode())
	
	points = list()
	legs_distance = list()
	legs_duration = list()
	
	routes = text["routes"]
	number_of_routes = len(routes)
	
	for i in range(number_of_routes):
		points.append(routes[i]["overview_polyline"]["points"])
		leg = routes[i]["legs"][0]
		leg_distance = leg["distance"]
		leg_duration = leg["duration"]
		legs_distance.append(leg_distance)
		legs_duration.append(leg_duration)
	
	return points, legs_distance, legs_duration


def main():
	# start_time = datetime.now()
	# loadFileIntoPickle() # Call this method first time the application is executed.
	# end_time = datetime.now()
	# print("Time taken to load the pickle: " + str(end_time - start_time))
	parseDataSet(source=(42.34638135, -71.10379454), destination=(42.34284135, -71.09698955), dept_time=1553433312)
	points, legs_distance, legs_duration = parseDataFromAPI(URL_TO_BE_SCRAPED)


if __name__ == '__main__':
	main()
