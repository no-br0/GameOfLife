import numpy as np

grid = np.zeros([3,3], dtype=int)
grid[1,1] = 2
grid[0,0] = 1
grid[2,2] = 1
#print(grid[grid > 0])
#print(len(grid[grid > 0]))
print(grid)