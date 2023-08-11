import numpy as np

def square_neigh(grid, i, j, reach=1):
    neigh = grid.take(range(i-reach, i+reach+1), mode='wrap', axis=0).take(range(j-reach, j+reach+1), mode='wrap', axis=1)
    neigh[reach,reach] = 0
    return neigh

def square_neigh_count(grid, i, j, reach=1):
    neigh = square_neigh(grid,i,j,reach)
    return neigh[neigh>0].size

def horizontal_neigh(grid, i, j, reach=1):
    neigh = grid.take(range(i-reach, i+reach+1), mode='wrap', axis=0).take(range(j, j+1), mode='wrap', axis=1)
    neigh[reach,0] = 0
    return neigh

def horizontal_neigh_count(grid, i, j, reach=1):
    neigh = horizontal_neigh(grid,i,j, reach)
    return neigh[neigh>0].size
    
def vertical_neigh(grid, i, j, reach=1):
    neigh = grid.take(range(i,i+1), mode='wrap', axis=0).take(range(j-reach, j+reach+1), mode='wrap', axis=1)
    neigh[0,reach] = 0
    return neigh

def vertical_neigh_count(grid, i,j, reach=1):
    neigh = vertical_neigh(grid, i, j, reach)
    return neigh[neigh>0].size


def knight_neigh(grid, i,j):
    neigh = []
    
    neigh.append(grid[(i+1)%grid[0].size, (j+2)%grid[0].size])
    neigh.append(grid[(i+1)%grid[0].size, (j-2)%grid[0].size]) 
    
    neigh.append(grid[(i-1)%grid[0].size, (j+2)%grid[0].size])
    neigh.append(grid[(i-1)%grid[0].size, (j-2)%grid[0].size])
    
    neigh.append(grid[(i+2)%grid[0].size, (j+1)%grid[0].size])
    neigh.append(grid[(i-2)%grid[0].size, (j+1)%grid[0].size]) 
    
    neigh.append(grid[(i+2)%grid[0].size, (j-1)%grid[0].size])
    neigh.append(grid[(i-2)%grid[0].size, (j-1)%grid[0].size])
    
    return neigh

#May Require some changes when cells greater than 1 are implemented
def knight_neigh_count(grid, i, j):
    neigh = knight_neigh(grid, i, j)        
    return sum(neigh)