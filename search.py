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

import sys
import argparse
import time
#import numpy

from agent import Agent
from maze import Maze
import math
from queue import PriorityQueue, Queue,LifoQueue


from typing import Dict, List, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')

Location = TypeVar('Location')


def search(maze, agent, searchMethod):    
    return {
        "depth": dfs,
        "breadth": bfs,
        "astar": astar
    }.get(searchMethod)(maze,agent)


def dfs(maze, agent):
    frontier = LifoQueue()
    came_from: Dict[Location, Location] = {}
    path = []
    frontier.put(maze.getStart())
    came_from[maze.getStart()] = None
    while not frontier.empty():
        current: Location = frontier.get()
        path.append(current)
        if current == maze.getGoal():
            print("Reached",current)
            break
        print('Current: ', current)
        for next in maze.getNeighbors(current[0], current[1]):
            print('   ', next)
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return path, 0


def bfs(maze, agent):
    frontier = Queue()
    came_from: Dict[Location, Location] = {}
    path = []
    frontier.put(maze.getStart())
    came_from[maze.getStart()] = None
    while not frontier.empty():
        current: Location = frontier.get()
        path.append(current)
        if current == maze.getGoal():
            print("Reached",current)
            break
        print('Current: ', current)
        for next in maze.getNeighbors(current[0],current[1]):
            print('   ', next)
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return path, 0


def astar(maze, agent):
    # TODO: Write your code here
    frontier = PriorityQueue()
    frontier.put(maze.getStart(),0)
   # functionH =  h(maze.maze)
    #functionG 

    # return path, num_states_explored
    return [], 0


def h(maze, agent):
    (x1, y1) = agent.getPosition()
    (x2, y2) = maze.getGoal()
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def getCost(maze, position):
    (x1, y1) = position
    (x2, y2) = maze.getGoal()
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='CAP Project2')
    
    parser.add_argument('filename',
                        help='path to maze file [REQUIRED]')
    parser.add_argument('-method', dest="search", type=str, default = "astar", 
                        choices = ["depth", "breadth", "astar"],
                        help='search method - default astar')

    args = parser.parse_args()

    file_name = args.filename
    method = args.search
    maze = Maze(file_name)
    agent = Agent(maze)
    path, total_cost = search(maze, agent, method)

    print(file_name)
    print(method)
    print(maze.getGoal())
    print('Number of nodes expanded: ', len(set(path)))
    print('Total Cost: ', total_cost)
    print('Path: ')
    print('-> '.join(str(node) for node in path))