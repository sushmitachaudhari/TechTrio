'''
Created on Mar 23, 2019

@author: Audrey
'''
import matplotlib.pyplot as plt
from math import sqrt

ALLOWED_DISTANCE = 0.25

# crimes_locations = [(0.1, 0.4), (0.3, 0.2), (-0.1, -0.1)]
# path = [(0,0), (0.2, 0.2), (0.4, 0.4), (0.6, 0.6), (0.8, 0.8), (1,1)]
# path2 = [(0,0), (0.1, 0.1), (0.2,0.2), (0.3,0.3), (0.5,0.5), (1,1)]

crimes_locations = []
path = []
path2 = []


def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_close_to_crime(person, crime):
    return distance(person, crime) > ALLOWED_DISTANCE

# high score = danger
def pathEvaluator(path):
    score = 0
    for point_pair in zip(path[1:], path):
        for crime in crimes_locations:
            if is_close_to_crime(point_pair[0], crime):
                score = score + 1*(distance(point_pair[0], point_pair[1]))
        
    return score


# circles = []
# for crime in crimes_locations:
#     circles.append(plt.Circle(crime, ALLOWED_DISTANCE, color = 'red', alpha = 0.5))
#  
# ax = plt.gca()
# 
# for circle in circles:
#     ax.add_artist(circle)
#   
# 
# testList2 = [(elem1, elem2) for elem1, elem2 in path]
# zip(*testList2)
# plt.scatter(*zip(*testList2))
# testList2 = [(elem1, elem2) for elem1, elem2 in path2]
# zip(*testList2)
# plt.scatter(*zip(*testList2))
# 
# 
# print(pathEvaluator(path))
# print(pathEvaluator(path2))
#   
# fig = plt.gcf()
#   
# plt.show()