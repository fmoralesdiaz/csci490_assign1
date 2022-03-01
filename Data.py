# file: Data.py
# Purpose:   Contains Dict of Dicts storing the
#            lattitude and longitudes from each city
#            
import re
class Data:


 def name(self):
  return "lat_longDB"



 def getLatLong(): 
  lat_file = open("france-latlong.txt")

  lat_long_DB={}
  lat_long_dict={}

  for input_line in lat_file:
    input_line = input_line.strip()
    
    #using regex to group ouput and use matcher object 
    regex_pattern = re.compile("(^.+\w),.+,\s.+\s(\d+\.\d+)\s(\d+\.\d+)")
    matchedOutput = regex_pattern.match(input_line)

    #if there is a line that doesnt match the pattern print an error message
    if not matchedOutput:
        #print("incorrect input")
        continue
        
    city_name = matchedOutput.group(1)
    city_lat = matchedOutput.group(2)
    city_long = matchedOutput.group(3)

    lat_long_dict['lat']=city_lat
    lat_long_dict['long']=city_long

    lat_long_DB[city_name]=lat_long_dict
  lat_file.close()
  # print("\n\nPrinting the values of the data base: ")
  # print (lat_long_DB)

  return lat_long_dict