import numpy as np

GRID_SIZE = [5,5]
#grid = np.zeros(GRID_SIZE, dtype=int)
grid = np.arange(GRID_SIZE[0]*GRID_SIZE[1]).reshape(GRID_SIZE)
#grid[0:5, 1] = 1
#grid[0:5, 2] = 2
i = 4
j = 4
# Didnt work but possible solution lies within
#neigh = np.array(grid[ ((i-1)%GRID_SIZE[0]):((i+2)%GRID_SIZE[0]), ((j-1)%GRID_SIZE[1]):((j+2)%GRID_SIZE[1]) ])

neigh = np.array(grid[i-1:i+2, j-1:j+2])
print(grid)
print(" ")
#print(neigh)
a = grid.take(range(i-1,i+2), mode='wrap', axis=0).take(range(j-1,j+2),mode='wrap', axis=1)
b = np.roll(np.roll(grid, i, axis=0), j, axis=1)[:3, :3]

print(a)
print(" ")
print(b)
#print(-1%9)