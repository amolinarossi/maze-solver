# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

# search method implementations inspired from: https://www.redblobgames.com/pathfinding/a-star/implementation.py

# Modified by Angelo Molina-Rossi and Rahul Mittal

import sys
import argparse

from maze import Maze
import math
from queue import PriorityQueue, Queue, LifoQueue


from typing import Dict, TypeVar, Optional
T = TypeVar('T')

Location = TypeVar('Location')


def search(maze, searchMethod):    
    return {
        "depth": dfs,
        "breadth": bfs,
        "astar": astar
    }.get(searchMethod)(maze)


def dfs(maze):
    cost_so_far: Dict[Location, float] = {}
    cost_so_far[maze.getStart()] = 0
    frontier = LifoQueue()
    came_from: Dict[Location, Location] = {}
    path = []
    frontier.put(maze.getStart())
    came_from[maze.getStart()] = None
    total_cost = 0
    while not frontier.empty():
        current: Location = frontier.get()
        path.append(current)
        if current == maze.getGoal():
            total_cost = cost_so_far[current]
            print("Reached",current)
            break
        print('Current: ', current)
        for next in maze.getNeighbors(current[0], current[1]):
            print('   ', next)
            if next not in came_from:
                new_cost = cost_so_far[current] + getCost(current, next)
                cost_so_far[next] = new_cost
                frontier.put(next)
                came_from[next] = current
    return path, total_cost


def bfs(maze):
    cost_so_far: Dict[Location, float] = {}
    cost_so_far[maze.getStart()] = 0
    frontier = Queue()
    came_from: Dict[Location, Location] = {}
    path = []
    frontier.put(maze.getStart())
    came_from[maze.getStart()] = None
    total_cost = 0
    while not frontier.empty():
        current: Location = frontier.get()
        path.append(current)
        if current == maze.getGoal():
            total_cost = cost_so_far[current]
            print("Reached",current)
            break
        print('Current: ', current)
        for next in maze.getNeighbors(current[0],current[1]):
            print('   ', next)
            if next not in came_from:
                new_cost = cost_so_far[current] + getCost(current, next)
                cost_so_far[next] = new_cost
                frontier.put(next)
                came_from[next] = current
    return path, total_cost


def astar(maze):
    frontier = PriorityQueue()
    frontier.put(maze.getStart(), 0)
    came_from: Dict[Location, Optional[Location]] = {}
    cost_so_far: Dict[Location, float] = {}
    came_from[maze.getStart()] = None
    cost_so_far[maze.getStart()] = 0
    path = []
    total_cost = 0
    while not frontier.empty():
        current: Location = frontier.get()
        path.append(current)
        if current == maze.getGoal():
            print("Reached",current)
            total_cost = cost_so_far[current]
            break
        print('Current: ', current)
        for next in maze.getNeighbors(current[0], current[1]):
            new_cost = cost_so_far[current] + getCost(current, next)
            print('   ', next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(maze, next)
                frontier.put(next, priority)
                came_from[next] = current
        
    return path, total_cost


def heuristic(maze, current):
    (x1, y1) = current
    (x2, y2) = maze.getGoal()
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def getCost(current, next):
    (x1, y1) = current
    (x2, y2) = next
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
    path, total_cost = search(maze, method)

    print(file_name)
    print(method)
    print(maze.getGoal())
    print('Number of nodes expanded: ', len(set(path)))
    print('Total Cost: ', total_cost)
    print('Path: ')
    print('-> '.join(str(node) for node in path))