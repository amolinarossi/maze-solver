# agent.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018



# The agent is only used when a human player is used, and is therefore not annotated much
class Agent():
    def __init__(self, maze):
        self.row = maze.getStart()[0]
        self.col = maze.getStart()[1]
        self.lastRow = None
        self.lastCol = None

        self.maze = maze


    def canMoveRight(self):
        return self.maze.isValidMove(self.row, self.col + 1)

    def canMoveLeft(self):
        return self.maze.isValidMove(self.row, self.col - 1)
        
    def canMoveUp(self):
        return self.maze.isValidMove(self.row - 1, self.col)

    def canMoveDown(self):
        return self.maze.isValidMove(self.row + 1, self.col)

    def moveRight(self):
        if self.canMoveRight():
            self.lastRow = self.row
            self.lastCol = self.col
            self.col += 1
        
    def moveLeft(self):
        if self.canMoveLeft():
            self.lastRow = self.row
            self.lastCol = self.col
            self.col -= 1

    def moveUp(self):
        if self.canMoveUp():
            self.lastRow = self.row
            self.lastCol = self.col
            self.row -= 1

    def moveDown(self):
        if self.canMoveDown():
            self.lastRow = self.row
            self.lastCol = self.col
            self.row += 1

    def getPosition(self):
        return (self.row,self.col)


