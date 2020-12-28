import pprint
import numpy as np
import time
import sys

SnakePos = [5, 10]
row, col = 30, 30

def Main_Menu():
    choice = 0
    print('Welcome to the game of Snake\n\n1.Start the game\n\n2.Settings\n\n3.Exit\n')
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())
        if choice == 1:
            Start_Game(row, col, 0)
        if choice == 2:
            Setting_Menu()
        if choice == 3:
            sys.exit()
        
def Start_Game(row, col, speed):
    grid = GenMap()
    PrintMap(grid)
    return True

def Gen_border():
    
    pass

def GenMap():
    grid  = np.array([['X' for i in range(row)] for f in range(col)], np.unicode)
#    grid = np.array([[row]col], np.unicode)
    for i in range(row - 1):
        for f in range(col - 1):
            grid[i][f] = ' '
    return grid

def PrintMap(grid):
    for x in range(row):
        for y in range(col):
            print(grid[y][x], end='')
        print()
"""
Main_Menu()
grid = GenMap(25, 25)
PrintMap(grid)
"""

Main_Menu()
