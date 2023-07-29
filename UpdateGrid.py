import numpy as np
from Values import Dead, Mushroom, Grass, Water

def update_grid(grid, GRID_SIZE):
    
    return update_grid_modular(grid, GRID_SIZE)



def update_grid_modular(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    
    # Test Function: Works as intended
    #def rule_0():
    #    print("Hello World  (" + str(i) + "," + str(j) + ")")
    def default():
        neigh = np.array(grid[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])])
        neigh[1,1] = 0
        num_neigh = neigh[neigh>0].size
        
        if grid[i,j] == 1 and (num_neigh < 2 or num_neigh > 3):
            return 0
        elif grid[i,j] == 0 and num_neigh == 3:
            return 1
        else:
            return grid[i,j]
        
        
        
    
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            #rule_0()
            new_grid[i,j] = default()
            
            
        
    return new_grid










# Here For Reference
def update_grid_default(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Count the number of live neighbors
            neigh = np.array(grid[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])])
            neigh[1,1] = 0
            num_neigh = neigh[neigh > 0].size
            sum_neigh = np.sum(neigh)
            
            if grid[i, j] == 1 and (num_neigh < 2 or num_neigh > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and (num_neigh == 3):
                new_grid[i, j] = 1
    
    return new_grid


# Here For Reference
def update_grid_average(grid, GRID_SIZE):
    
    new_grid = grid.copy()
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            neigh = np.array(grid[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])])
            avg_neigh = np.sum(neigh)/9
            
            
            if grid[i,j] == 0: 
                if (avg_neigh * 3) == 1:
                    new_grid[i,j] = 1
                    
            elif grid[i,j] == 1: 
                if (avg_neigh * 3) <= 1 and (avg_neigh * 3) > 3:
                    new_grid[i,j] = 0
                elif avg_neigh == 1:
                    new_grid[i,j] = 2
            
            elif grid[i,j] == 2:
                if (avg_neigh * 3) < 1:        
                    new_grid[i,j] = 0
                if (avg_neigh * 3) > 1.5:
                    new_grid[i,j] = 1
            
    return new_grid




