import numpy as np
from random import randint

def square_neigh(grid, i, j, reach=1):
    neigh = grid.take(range(i-reach, i+reach+1), mode='wrap', axis=0).take(range(j-reach, j+reach+1), mode='wrap', axis=1)
    neigh[reach,reach] = [0,0]
    return neigh

def square_neigh_count(grid, i, j, reach=1):
    neigh = square_neigh(grid,i,j,reach)
    output = 0
    for i in neigh:
        for j in i:
            state = randint(0,1)
            output += j[state]
    
    return output
