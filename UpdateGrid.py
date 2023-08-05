import numpy as np
from Values import Dead, Mushroom, Grass, Water
import GridRules as gr

def update_grid(grid, GRID_SIZE):
    
    return update_grid_modular(grid, GRID_SIZE)



def update_grid_modular(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    
    # Test Function: Works as intended
    #def rule_0():
    #    print("Hello World  (" + str(i) + "," + str(j) + ")")
    
        
        



    

            
    
    
    #has potential with some other rules added with it (Also will require simplifying)
    def chess_knight():
        for i in range(GRID_SIZE[0]):
            for j in range(GRID_SIZE[1]):
                if grid[i,j] == 1:
                    if new_grid[i+2, j+1] == 0:
                        new_grid[i+2, j+1] = 1
                    
                    if new_grid[i+2, j-1] == 0:
                        new_grid[i+2, j-1] = 1
                    
                    if new_grid[i-2, j+1] == 0:
                        new_grid[i-2, j+1] = 1
                    
                    if new_grid[i-2, j-1] == 0:
                        new_grid[i-2, j-1] = 1
                        
                        
                    if new_grid[i+1, j+2] == 0:
                        new_grid[i+1, j+2] = 1
                    
                    if new_grid[i-1, j+2] == 0:
                        new_grid[i-1, j+2] = 1
                    
                    if new_grid[i+1, j-2] == 0:
                        new_grid[i+1, j-2] = 1
                    
                    if new_grid[i-1, j-2] == 0:
                        new_grid[i-1, j-2] = 1
                        
                    
                        
                        
        
    
    
    # DO NOT REMOVE IS NEEDED FOR EVERYTHING EXCEPT FOR THE chess_knight() function
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            #new_grid[i,j] = default_test(range = 2, min_life = 3, max_life = 5, create_life = 4)
            #new_grid[i,j] = gr.Simple.horivertical(grid,i,j, 2)
            #new_grid[i,j] = gr.Simple.horivertical(grid,i,j, 3)
            #new_grid[i,j] = gr.Simple.horivertical(grid,i,j, 1)
            #new_grid[i,j] = gr.Chess.knight(grid,i,j, stay_alive=[1])
            new_grid[i,j] = gr.Default.default(grid,i,j)

    
    #chess_knight()        

        
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




