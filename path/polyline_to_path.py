'''
Created on Mar 23, 2019

@author: Audrey
'''

def decode(encoded):
    # array that holds the points
    points = []
    index = 0
    length = len(encoded)
    lat = 0
    lng = 0
    while index < length:
        #var b
        shift = 0
        result = 0
        while True:
            b = ord(encoded[index]) - 63 #//finds ascii   
            index = index + 1#           //and substract it by 63
            result |= (b & 0x1f) << shift
            shift = shift + 5
            if b < 0x20:
                break
        if (result & 1) != 0:
            dlat =  ~(result >> 1)
        else:
            dlat = (result >> 1)
        lat = lat + dlat
        shift = 0
        result = 0
        while True:
            b = ord(encoded[index]) - 63
            index = index + 1
            result |= (b & 0x1f) << shift
            shift = shift + 5
            if b < 0x20:
                break
        if (result & 1) != 0:
            dlng =  ~(result >> 1)
        else:
            dlng = (result >> 1)
        lng = lng + dlng
        points.append((( lat / 1E5),( lng / 1E5)))  
    return points

# poly = "mupaGzmvpLBjC?FN?T??^BlCDpB?JLAhBGnAC?P@`BN?CeA?[l@C~@CP?~ADD@?P?|BArE?pC"
# print(decode(poly))
