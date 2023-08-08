import numpy as np


GRID_SIZE = [10, 10]

def secondary(grid):
    grid[0,0] = 1

def main():
    grid = np.zeros([3,3], dtype=int)
    secondary(grid)
    print(grid)
    #first = [0,GRID_SIZE[0]//2]
    #second = [GRID_SIZE[0]//2, GRID_SIZE[0]]
    #for i in range(first[0], first[1]):
    #    print(i)
        
    #print("---Break---")
    #for i in range(second[0], second[1]):
    #    print(i)
    

    
main()