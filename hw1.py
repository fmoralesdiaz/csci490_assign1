#!/usr/bin/python3

# Purpose:   A*

# Execution: ./hw1.py From_city To_city


from os import system
import sys
import re
from Node import Node
from Hfns import H_zero, H_east_west

def plain_city_string(city_list):
    base_city_string = " ".join([city for city in city_list])
    full_city_string = "(" + base_city_string + ")"
    return full_city_string    

    
def city_string(node_list):
    base_city_string = " ".join([node.name for node in node_list])
    full_city_string = "(" + base_city_string + ")"
    return full_city_string    

def city_f_string(node_list):
    base_city_string = " ".join(["(" + node.name + " " + str(node.f) + ")" for node in node_list])
    full_city_string = "(" + base_city_string + ")"
    return full_city_string    


# Function: astar(from_city, to_city, franceroads, france_long, h)
#
# Inputs:  from_city:    departure city
#          to_city:      destination city
#          france_roads: road list
#          france_long:  city longititude
#          h:            h function used in search
#
# Outputs:  None           
#
# Notes:    Look for shortest path between two cities using A* search.

def astar(from_city, to_city, france_roads, france_long, h):
    found_path = False
    open_list = [from_city]
    closed_list = []
    nodes_expanded = 0
    path_length = 0

    # set inital cities f, g and h values
    from_city.h = h.h(france_long[to_city.name], france_long[from_city.name])
    from_city.f = from_city.h + from_city.g

    print("A* with ", h.name(), ":\n\n", sep='')

    # while open list is not empty
    while len(open_list) != 0:

        # pop front of openlist and set current node
        current_node = open_list.pop(0)

        print("Expanding ", current_node.name, " f=", current_node.f, ",",
              " g=", current_node.g, ",", " h=", current_node.h, sep='')        

        # if current node is destination, set path length and break
        if current_node.name == to_city.name:
            path_length = current_node.f
            found_path = True
            break

        nodes_expanded += 1
        
        # get current node's children and calculate their f, g and h values
        # sort by name and print
        
        children = [Node(name, current_node.name,
                          int(france_roads[current_node.name][name]) + current_node.g,
                          h.h(france_long[to_city.name],
                              france_long[name])) for name in france_roads[current_node.name].keys()]
        children = sorted(children, key=lambda x: x.name)
        print("Children are " + city_string(children))

        # for every child
        for child in children:
            if child not in closed_list:
                if child not in open_list:
                    # add to open list
                    open_list.append(child)

                # else if child has smaller value then openlist, replace openlist city with child
                elif child.f < open_list[open_list.index(child)].f:
                    print("***Revaluing open node", child.name, "from",
                          open_list[open_list.index(child)].f, "to", child.f)
                    open_list[open_list.index(child)] = child

            # else if child has smaller value then closed_list,
            # remove from closed_list and add child back onto open_list
            elif child.f < closed_list[closed_list.index(child)].f:
                print("***Revaluing closed node", child.name, "from",
                      closed_list[closed_list.index(child)].f, "to", child.f)
                open_list.append(child)
                closed_list.remove(child)

        # sort openlist by name and by f value and print
        open_list = sorted(open_list, key=lambda x: x.name)
        open_list = sorted(open_list, key=lambda x: x.f)
        print("Open list is", city_f_string(open_list))

        # add current node to closed list and print
        closed_list.append(current_node)
        print("Closed list is", city_f_string(closed_list))
        print()
        
    # if solution found
    #  backtrack through the closed list using parent references to
    #  construct the full path

    if found_path:
        solution_path = []
        while current_node != from_city:
            solution_path.insert(0, current_node.name)
            current_node = closed_list[closed_list.index(Node(current_node.parent))]
        solution_path.insert(0, from_city.name)
        print("\n\nA* solution with ", h.name(), ": ", plain_city_string(solution_path), sep='')
        print("Path length:", path_length)
    else:
        print("\n\nA* has no solution")
        
    print(nodes_expanded, "nodes expanded\n\n")


france_roads = {}
france_long = {}

france_roads_file = open("france-roads1.txt")

for input_line in france_roads_file:
    input_line = input_line.strip()

    if input_line != "" and input_line[0] != "#":

        # ':' indicates new city, make new inner dict
        if ":" in input_line:
            cur_city = input_line.replace(":", "").lower().capitalize()
            france_roads[cur_city] = {}
        else:
            city_distance = input_line.split()
            france_roads[cur_city][city_distance[0]] = city_distance[1]

# close file
france_roads_file.close()


#  Attempting to make dict of dicts
#   Need to opena and read file france-latlong.txt
#
#
#

lat_long_dict = {}
lat_long_DB={}

lat_file = open("france-latlong.txt")

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

# open france long file
france_long_file = open("france-long1.txt")

for input_line in france_long_file:
    input_line = input_line.strip()

    if input_line != "" and input_line[0] != "#":
        city_long = input_line.split()
        france_long[city_long[0]] = city_long[1]

france_long_file.close()

arg_count = len(sys.argv)

if arg_count == 3:
    from_city  = Node(sys.argv[1])
    to_city    = Node(sys.argv[2])
else:
    print("Two arguments required: from city and to city")
    sys.exit()

if from_city.name not in france_long:
    print("From city not valid: ", from_city.name)
    sys.exit()

if to_city.name not in france_long:
    print("To city not valid: ", to_city.name)
    sys.exit()

astar(from_city, to_city, france_roads, france_long, H_zero())

astar(from_city, to_city, france_roads, france_long, H_east_west())


print("\n\nPrinting the values of the data base: ")
print (lat_long_DB)

