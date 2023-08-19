from GridRules import Tools as t
from random import randint

def horizontal(grid, i, j, reach=1, stay_alive:list=[1], become_alive:list=[1]):
    num_neigh = t.horizontal_neigh_count(grid, i, j, reach)
    
    
    
    if grid[i,j] == 0:
        if num_neigh in become_alive:
            return 1
        else:
            return 0
    else:
        if num_neigh in stay_alive:
            return 1
        else:
            return 0
    
    '''
    if grid[i,j] == 0:
        if num_neigh == 1:
            return 1
        else:
            return 0
    else:
        return 1
    '''
    
    
    
def vertical(grid, i, j, reach=1, stay_alive:list=[1], become_alive:list=[1]):
    num_neigh = t.vertical_neigh_count(grid, i, j, reach)
    
    if grid[i,j] == 0:
        if num_neigh in become_alive:
            return 1
        else:
            return 0
    else:
        if num_neigh in stay_alive:
            return 1
        else:
            return 0
    
    

def horivertical(grid, i, j, reach=1, stay_alive:list=[2,3], become_alive:list=[2]):
    num_neigh = t.horizontal_neigh_count(grid, i, j, reach) + t.vertical_neigh_count(grid,i,j, reach)
    
    if grid[i,j] == 1:
        if num_neigh in stay_alive:
            return 1
        else:
            return 0
    else:
        if num_neigh in become_alive:
            return 1
        else:
            return 0



# Still to be worked on
def horivertical_average(grid, i, j, reach=1):
    vert = vertical(grid, i, j, reach)
    hori = horizontal(grid, i, j, reach)
    
        
    if (vert == 1 and hori == 0) or (vert == 0 and hori == 1):
        return 1
    else:
        return 0

    '''
    if vert == 1 and hori == 1:
        return 1
    else:
        return 0
    '''
    
    
def doughnut(grid,i,j, inner_reach = 1, outer_reach = 2, stay_alive=[2,3], become_alive=[3]):
    num_neigh = t.square_neigh_count(grid,i,j,outer_reach) - t.square_neigh_count(grid,i,j,inner_reach)
    
    
    if grid[i,j] == 1:
        if num_neigh in stay_alive:
            return 1
        else:
            return 0
    else:
        if num_neigh in become_alive:
            return 1
        else:
            return 0
        
        

