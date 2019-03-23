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


def url_creator_from_strings(orig, dest, dep_time):
    result = "https://maps.googleapis.com/maps/api/directions/json?origin=" + orig + "&destination=" + dest + "&departure_time=" + str(
        dep_time) + "&alternatives=true&mode=walking&key=" + SECRET_KEY
    return result

# orig = (1.3, 4)
# dest = (-3.4, 2)
# 
# orig2 = "Agganis Arena, Boston, MA"
# dest2 = "Boston University, MA"
# 
# print(url_creator_from_strings(orig2, dest2, 1553468425))