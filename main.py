import math
import numpy

maze = [[0,0,0,0,0],
        [0,0,0,0,3],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [2,0,0,0,0]]

class Distance:
    def __init__(self, distance):
        self.distance = distance

class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.dataTypes = {
            0: "free",
            1: "wall",
            2: "start",
            3: "end",
            4: "path"
        }
    
    def coord(self, location: tuple):
        return self.maze[location[1]][location[0]]
    
    def adjacents(self, location):
        above = None
        below = None
        left = None
        right = None
        
        # checking if outside matrix boundary

        if location[0] - 1 >= 0:
            left = (location[0]-1, location[1])
        if location[0] + 1 <= len(self.maze[0])-1:
            right = (location[0]+1, location[1])
        if location[1] - 1 >= 0:
            above = (location[0], location[1]-1)
        if location[1] + 1 <= len(self.maze)-1:
            below = (location[0], location[1]+1)

        return [above, below, left, right]

    def findPath(self):
        self.path = []

test_object = AStar(maze)
print(f"this is the maze: ")
print(maze)
print(f"here is the adjacents of location (0,0): {test_object.adjacents((0,0))}")
