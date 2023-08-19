from random import randint
import LateUpdate as lu
from GridRules import Tools as t

def move_down(grid,i,j):
    if grid[i,j] == 1:
        #lu.late_update_values.append((1, (i, j+random.randint(0,5))))
        #lu.late_update_values.append((1, (i,j+1)))
        lu.add_late_value(1, i, j+1)
    return 0
        

def default_move_down(grid, i, j, stay_alive:list = [2,3], become_alive:list = [3]):
    num_neigh = t.square_neigh_count(grid,i,j)
    
    if grid[i,j] == 0:
        if num_neigh in become_alive:
            return 1
        else:
            return 0
    elif grid[i,j] == 1:
        if num_neigh in stay_alive:
            if num_neigh in become_alive:
                #lu.late_update_values.append((1, (i,j+1))) 
                lu.add_late_value(1, i, j+1)
            return 1
        else:
            return 0
    else:
        return grid[i,j]
        
        
def move_random(grid,i,j):
    if grid[i,j] == 1:
        x = i + randint(-1,1)
        y = j + randint(-1,1)
        #lu.late_update_values.append((1,(x,y)))
        lu.add_late_value(1,x,y)
    return 0

def move_random1(grid,i,j):
    if grid[i,j] == 1:
        x = i + randint(-1,1)
        y = j + randint(-1,1)
        #lu.late_update_values.append((1,(x,y)))
        lu.add_late_value(1,x,y)
    return grid[i,j]

def move_random2(grid,i,j):
    if grid[i,j] == 1:
        x = i + randint(-1,1)
        y = j + randint(-1,1)
        #lu.late_update_values.append((1,(x,y)))
        lu.add_late_value(1,x,y)
    if randint(0,1) == 0:
        return 0
    else:
        return grid[i,j]
    
    
def move_random3(grid,i,j):
    if grid[i,j] == 1:
        x = i + randint(-1,1)
        y = j + randint(-1,1)
        #lu.late_update_values.append((1,(x,y)))
        lu.add_late_value(1,x,y)
    if randint(0,15) != 0:
        return 0
    else:
        return grid[i,j]