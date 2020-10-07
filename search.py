# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (depth,breadth,astar)

import maze
import math
import PriorityQueue

def search(maze, searchMethod):    
    return {
        "depth": dfs,
        "breadth": bfs,
        "astar": astar,
    }.get(searchMethod)(maze)
   
def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0


def bfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0


def astar(maze):
    # TODO: Write your code here
    frontier = PriorityQueue()
    frontier.put(maze.getStart(),0)

    # return path, num_states_explored
    return [], 0


def h(curr,maze):
    (x1, y1) = curr
    (x2, y2) = maze.getGoal(maze)
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)