import numpy as np

def update_grid(grid, GRID_SIZE):
    # Copy the grid
    new_grid = grid.copy()

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Count the number of live neighbors
            num_neighbors = np.sum(grid[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])]) - grid[i, j]



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

            if grid[i,j] == 1 and (num_neighbors != 3 and num_neighbors != 4 and num_neighbors != 7):
                new_grid[i,j] = 0
            elif grid[i,j] == 0 and (num_neighbors == 3 or num_neighbors == 5 or num_neighbors == 7):
                new_grid[i,j] = 1

    return new_grid