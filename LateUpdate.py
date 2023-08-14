import numpy as np


#new (format is list[int,tuple[int,int]]) or [int,(int,int)]
late_update_values = []

#basic version not tested yet, will need improving for further functionality
def late_update(new_grid:np.array, GRID_SIZE):
    global late_update_values
    #print(late_update_values)
    if len(late_update_values) > 0:
        for i in late_update_values:
            pos:tuple[int,int] = i[1]
            value:int = i[0]
            new_grid[pos[0]%GRID_SIZE[0], pos[1]%GRID_SIZE[1]] = value
        late_update_values.clear()
    return new_grid