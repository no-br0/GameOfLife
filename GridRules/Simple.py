from GridRules import Tools as t


def horizontal(grid, i, j, size=1, stay_alive:list=[1], become_alive=[1]):
    num_neigh = t.horizontal_neigh_count(grid,i,j, size)
    
    
    
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
    
    
    
def vertical(grid, i, j, size=1, stay_alive:list=[1], become_alive:list=[1]):
    num_neigh = t.vertical_neigh_count(grid, i,j, size)
    
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
    
    

def horivertical(grid, i, j, size=1, stay_alive:list=[2,3], become_alive:list=[2]):
    num_neigh = t.horizontal_neigh_count(grid,i,j, size) + t.vertical_neigh_count(grid,i,j, size)
    
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
def horivertical_average(grid, i, j, size=1):
    vert = vertical(grid,i,j,size)
    hori = horizontal(grid,i,j,size)
    
        
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
    
        
        
        