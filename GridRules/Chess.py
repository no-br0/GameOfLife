from GridRules import Tools as t

def knight(grid, i, j, stay_alive:list=[2,3], become_alive:list=[2]):
    num_neigh = t.knight_neigh_count(grid, i, j)
    
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