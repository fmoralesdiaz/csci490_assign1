# File:       Node.py

# Purpose:   Contains the Node class

class Node:

    def __init__(self, in_name, in_parent=None, in_g=0, in_h=0, in_depth=0):
        self.name = in_name
        self.parent = in_parent
        self.g = in_g
        self.h = in_h
        self.f = in_g + in_h
        self.depth = in_depth

    def __eq__(self, other):
        x = self.name == other.name
        return x
    
