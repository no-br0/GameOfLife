import GridRules as gr

#works for making the grid loop around edges
def default(grid, i, j, size=1, stay_alive:list=[2,3], become_alive:list=[3]):
    num_neigh = gr.Tools.square_neigh_count(grid,i,j)
    
    
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