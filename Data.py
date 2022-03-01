# file: Data.py
# Purpose:   Contains Dict of Dicts storing the
#            lattitude and longitudes from each city
#            

class Data:

  def __init__(self,in_name,lat_val,long_val):
    self.name = in_name
    self.lat = lat_val
    self.long = long_val