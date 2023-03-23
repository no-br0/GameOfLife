import numpy as np

def update_grid(grid, GRID_SIZE):
    # Copy the grid
    new_grid = grid.copy()

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Count the number of live neighbors
            neigh = grid[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])]
            sum_neigh = np.sum(neigh) - grid[i, j]
            temp_neigh = np.array(neigh)
            temp_neigh[1,1] = 0
            num_neigh = len(temp_neigh[temp_neigh > 0])



            #if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 4):
            #    new_grid[i, j] = 0
            #elif grid[i, j] == 0 and (num_neighbors == 3 or num_neighbors == 2):
            #    new_grid[i, j] = 1

            # Apply the rules of the game
            #if grid[i, j] == 1 and (num_neighbors < 3 or num_neighbors > 4):
            #    new_grid[i, j] = 0
            #elif grid[i, j] == 0 and (num_neighbors == 4 or num_neighbors == 3):
            #    new_grid[i, j] = 1

            #if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 4):
            #    new_grid[i, j] = 0
            #elif grid[i, j] == 0 and (num_neighbors == 3):
            #    new_grid[i, j] = 1

            # Apply the rules of the game
            #if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
            #    new_grid[i, j] = 0
            #elif grid[i, j] == 0 and (num_neighbors == 3 or num_neighbors == 4):
            #    new_grid[i, j] = 1

            #if grid[i,j] == 1 and num_neighbors > 2:
            #    new_grid[i,j] = 0
            #elif grid[i,j] == 0 and num_neighbors == 3:
            #    new_grid[i,j] = 1

            #if grid[i,j] == 1 and (num_neighbors != 4 and num_neighbors != 6 and num_neighbors != 6):
            #    new_grid[i,j] = 0
            #elif grid[i,j] == 0 and (num_neighbors == 3 or num_neighbors == 4 or num_neighbors == 6):
            #    new_grid[i,j] = 1

            #Creates amazing symmetry
            #if grid[i,j] == 1 and (num_neighbors != 3 and num_neighbors != 4 and num_neighbors != 7):
            #    new_grid[i,j] = 0
            #elif grid[i,j] == 0 and (num_neighbors == 3 or num_neighbors == 4 or num_neighbors == 7):
            #    new_grid[i,j] = 1

            # can generate 4 leaf clovers
            #if grid[i,j] == 0 and (num_neigh == 3):
            #    new_grid[i,j] = 1
            #elif grid[i,j] == 1 and (num_neigh == 4):
            #    new_grid[i,j] = 2
            #elif grid[i,j] == 1 and (num_neigh != 2 and num_neigh != 3):
            #    new_grid[i,j] = 0
            

            # creates beautiful mandalas
            #if grid[i,j] == 0:
            #    if num_neigh == 3:
            #        new_grid[i,j] = 1

            #elif grid[i,j] == 1:
            #    if sum_neigh == 5:
            #        new_grid[i,j] = 2
            #    elif num_neigh != 2 and num_neigh != 3:
            #        new_grid[i,j] = 0

            #elif grid[i,j] == 2:
            #    if sum_neigh == 4 or num_neigh == 4:
            #        new_grid[i,j] = 1
            #    elif sum_neigh == 5:
            #        pass
            #    elif num_neigh != 2 and num_neigh != 3:
            #        new_grid[i,j] = 0



            #if grid[i,j] == 0:
            #    if num_neigh == 3:
            #        new_grid[i,j] = 1

            #elif grid[i,j] == 1:
            #    if sum_neigh == 5:
            #        new_grid[i,j] = 2
            #    elif num_neigh != 2 and num_neigh != 3:
            #        new_grid[i,j] = 0

            #elif grid[i,j] == 2:
            #    if sum_neigh == 6 or num_neigh == 4:
            #        new_grid[i,j] = 1
            #    elif num_neigh != 3 and num_neigh != 3 and num_neigh != 5:
            #        new_grid[i,j] = 0

            if grid[i,j] == 0:
                if sum_neigh == 3:
                    new_grid[i,j] = 1
            elif grid[i,j] == 1:
                if sum_neigh == 5:
                    new_grid[i,j] = 2
                elif sum_neigh != 2 and sum_neigh != 3:
                    new_grid[i,j] = 0
            elif grid[i,j] == 2:
                if sum_neigh == 1 or sum_neigh == 4:
                    new_grid[i,j] = 1
                elif sum_neigh != 3 and sum_neigh != 5:
                    new_grid[i,j] = 0

    return new_grid