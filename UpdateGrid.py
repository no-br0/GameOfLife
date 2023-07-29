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
        
    def default_test(range = 1, min_life = 2, max_life = 3, create_life = 3):
        neigh = np.array(grid[max(i-range, 0):min(i+range+1,GRID_SIZE[0]), max(j-range, 0):min(j+range+1, GRID_SIZE[1])])
        neigh[1,1] = 0
        num_neigh = neigh[neigh>0].size
        
        if grid[i,j] == 1 and (num_neigh < min_life or num_neigh > max_life):
            return 0
        elif grid[i,j] == 0 and num_neigh == create_life:
            return 1
        else:
            return grid[i,j]
        
    #works for making the grid loop around edges
    def default_wrap():
        neigh = grid.take(range(i-1, i+2), mode='wrap', axis=0).take(range(j-1, j+2), mode='wrap', axis=1)
        neigh[1,1] = 0
        num_neigh = neigh[neigh > 0].size
        
        if grid[i,j] == 1 and (num_neigh < 2 or num_neigh > 3):
            return 0
        elif grid[i,j] == 0 and num_neigh == 3:
            return 1
        else:
            return grid[i,j]
        
        
    
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            #new_grid[i,j] = default_test(range = 2, min_life = 3, max_life = 5, create_life = 4)
            new_grid[i,j] = default_wrap()
            
            
        
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




