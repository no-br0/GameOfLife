from GridRules import Tools as t
from GridRules.DataTypes import transition, neigh_transition


#works for making the grid loop around edges
def default(grid, i, j, reach=1, stay_alive:list=[2,3], become_alive:list=[3]):
    num_neigh = t.square_neigh_count(grid, i, j, reach)
    
    
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
    if grid[i,j] == 1 and (num_neigh < 2 or num_neigh > 3):
        
        return 0
    elif grid[i,j] == 0 and num_neigh == 3:
        return 1
    else:
        return grid[i,j]
    '''


def expanded_default(grid, i, j, reach:int=1, condition:list[transition] = [transition(0,1,(3,)), transition(1,1,(2,3))]):
    num_neigh = t.square_neigh_count(grid, i, j, reach)
    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0

def expanded_default2(grid, i, j, reach:int=1, condition:list[transition] = [transition(0,1,(3,)), transition(1,1,(2,3))]):
    if grid[i,j] == 0:
        num_neigh = t.square_neigh_count(grid, i, j, reach)
    else:
        num_neigh = t.square_neigh_count_num(grid,i,j,grid[i,j], reach)

    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0
    
    
    
def universal_rule(grid,i,j, rule:int, condition:list[transition]= [transition(0,1,(3,)), transition(1,1,(2,3))]):
    num_neigh = rule
    
    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0


def conditional_rule(grid,i,j, condition:list[neigh_transition]):
    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if condition[x].num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0
    