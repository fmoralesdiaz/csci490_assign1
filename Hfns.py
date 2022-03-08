#File:       Hfns.py

#Purpose:    Contains function objects for the A* search method.
#            h_zero returns a zero as a h function
#            h_east_west estimates a distance based on longitude

import math

class H_zero:
    def name(self):
        return "h=0"

    def h(self, long1, long2,lat1,lat2):
        return 0

class H_east_west:
    def name(self):
        return "h=east-west distance"

    def h(self, long1, long2,lat1,lat2):
        return 7.8*abs(float(long1) - float(long2))
    
class H_north_south:
    def name(self):
        return "h=north-south distance"
    
    def h(self,lat1,lat2,long1,long2):
        return 7.8*abs(float(lat1)-float(lat2))
class H_straight_line:
    def name(self):
        return "h= straight line distance"
    def h (self, lat1,lat2,long1,long2):
        dLat = (lat1-lat2)*math.pi
        dLong = (long1 - long2)* math.pi

        lat1 = (lat1) * math.pi
        lat2 = (lat1) * math.pi

        a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLong / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

