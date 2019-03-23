import csv
import pickle
import os
from datetime import datetime
import json
import math

DATA = "crimes_data.csv"

reader = csv.DictReader(open(DATA, 'r'))
PICKLE_FILE = "dataDict.p"
TEXTFILE_FOR_DATA_TO_BE_PARSED = "apiData.json"
ZONE_RANGE = 5


def loadFile():

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


def parseDataSet():

	# Obtain the location
	


def obtainWalkingRange():

	walkingRange = list()

	#Distance in km
	latitude1, longitude1 = offsetGeoCoordinates(0.005)
	latitude2, longitude2 = offsetGeoCoordinates(-0.005)
	
	walkingRange.append((latitude1, longitude1))
	walkingRange.append((latitude2, longitude2))

	return walkingRange


def offsetGeoCoordinates(la1 ,lo1):

	'''
	# Use the user's source and destination, offset it and return the range.

	lat2 = asin(sin(lat1)*cos(d/R) + cos(lat1)*sin(d/R)*cos(θ))

	lon2 = lon1 + atan2(sin(θ)*sin(d/R)*cos(lat1), cos(d/R)−sin(lat1)*sin(lat2))
	'''
	R = 6378.1 #Radius of the Earth
	bearing = 1.57 #Bearing is 90 degrees converted to radians.
	global ZONE_RANGE
	d = ZONE_RANGE #Distance in km

	#lat2  52.20444 - the lat result I'm hoping for
	#lon2  0.36056 - the long result I'm hoping for.

	# lat1 = 52.20472 * (math.pi * 180) #Current lat point converted to radians
	# lon1 = 0.14056 * (math.pi * 180) #Current long point converted to radians

	lat1 = la1 * (math.pi * 180) #Current lat point converted to radians
	lon1 = lo1 * (math.pi * 180) #Current long point converted to radians

	lat2 = math.asin(math.sin(lat1)*math.cos(d/R) +
	             math.cos(lat1)*math.sin(d/R)*math.cos(bearing))

	lon2 = lon1 + math.atan2(math.sin(bearing)*math.sin(d/R)*math.cos(lat1),
                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

	return lat2, lon2


def parseDataFromAPI():

	global TEXTFILE_FOR_DATA_TO_BE_PARSED

	with open(TEXTFILE_FOR_DATA_TO_BE_PARSED, 'r') as f:
		text = json.load(f)
	
	points = list()
	legs_distance = list()
	legs_duration = list()

	routes = text["routes"]
	number_of_routes = len(routes)
	
	for i in range(number_of_routes):
		points.append(routes[i])
		leg = routes[i]["legs"][0]
		leg_distance = leg["distance"]
		leg_duration = leg["duration"]
		legs_distance.append(leg_distance)
		legs_duration.append(leg_duration)

	return points, legs_distance, legs_duration


if __name__ == '__main__':
	# start_time = datetime.now()
	# loadFile()
	# end_time = datetime.now()
	# print("Time taken to load the pickle: " + str(end_time - start_time))
	# parseDataFromAPI()
