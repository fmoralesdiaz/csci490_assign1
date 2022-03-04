#File:       Hfns.py

#Purpose:    Contains function objects for the A* search method.
#            h_zero returns a zero as a h function
#            h_east_west estimates a distance based on longitude

class H_zero:
    def name(self):
        return "h=0"

    def h(self, long1, long2):
        return 0

class H_east_west:
    def name(self):
        return "h=east-west distance"

    def h(self, long1, long2):
        return 8 * abs(int(long1) - int(long2))
    
class H_north_south:
    def name(self):
        return "h=north-south distance"
    
    def h(self,lat1,lat2):
 
        return 8*abs(float(lat1)-float(lat2))