'''
Created on Mar 23, 2019

@author: Audrey
'''

SECRET_KEY = "INSERT_YOUR_API_KEY_HERE"

def url_creator(orig, dest, dep_time):
    x1, y1 = orig
    x2, y2 = dest
    result = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(
        x1) + "," + str(y1) + "&destination=" + str(
        x2) + "," + str(y2) + "&departure_time=" + str(
        dep_time) + "&alternatives=true&mode=walking&key=" + SECRET_KEY
    return result
