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

from typing import Dict, List, Iterator, Tuple, TypeVar, Optional
from agent import Agent
from maze import Maze
import math
from queue import PriorityQueue




def search(maze, agent, searchMethod):    
    return {
        "depth": dfs,
        "breadth": bfs,
        "astar": astar
    }.get(searchMethod)(maze,agent)
   
def dfs(maze, agent):
    frontier = PriorityQueue()
    frontier.put(maze.getStart(),0)
    came_from: Dict[(int,int), Optional[(int,int)]] = {}
    cost_so_far: Dict[(int,int), float] = {}
    came_from[maze.getStart()] = None
    cost_so_far[maze.getStart()] = 0
    total_cost = 0

    while not frontier.empty():
        
        current = frontier.get()
        agent.move(current)
        total_cost+= cost_so_far[current]
        print(agent.getPosition())
        if current == maze.getGoal():
            break
        
        for potentialNext in maze.getNeighbors(current[0], current[1]):
            new_cost = cost_so_far[current] + getCost(maze,potentialNext)
            if potentialNext not in cost_so_far or new_cost < cost_so_far[current]:
                next = potentialNext
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)

                print('-',next)
                came_from[next] = current



    return came_from, total_cost



def bfs(maze, agent):

    
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0


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

    fileName = args.filename
    searchType = args.search
    thisMaze = Maze(fileName)
    thisAgent = Agent(thisMaze)
    came_from, total_cost = search(thisMaze, thisAgent, searchType)

    print(fileName)
    print(searchType)
    print(thisMaze.getGoal())
    print('Number of nodes expanded: ', len(set(came_from)))
    print('Total Cost: ', total_cost)
    print('Path: ')
    print('-> '.join(str (key) for key in came_from))