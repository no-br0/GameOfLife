import numpy as np
import GridRules as gr
import threading 
from GridRules.DataTypes import transition, neigh_transition
from GridRules import Tools as t



def update_grid(grid, GRID_SIZE):
    
    return update_grid_normal(grid, GRID_SIZE)



def update_multi_rule(grid, i,j, alive, dead):
    if grid[i,j] == 0:
        return dead
    elif grid[i,j] == 1:
        return alive
    else:
        print("Error: Cell Exceeds Maximum Value.")
        return None



# To Be Completed
def update_grid_modular(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    

        
    return new_grid





def universal_rule(grid,i,j, rule:int, condition:list[transition]= [transition(0,1,(3,)), transition(1,1,(2,3))]):
    num_neigh = rule
    
    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0


def conditional_rule(grid,i,j, condition:list[neigh_transition]):
    for x in range(len(condition)):
        if grid[i,j] == condition[x].curstate:
            if condition[x].num_neigh in condition[x].condition:
                return condition[x].nextstate
    return 0




def update_grid_normal(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            #new_grid[i,j] = gr.Simple.move_down(grid,i,j)
            #new_grid[i,j] = gr.Simple.default_move_down(grid,i,j)
            #new_grid[i,j] = gr.TestMove.move_random3(grid,i,j)
            #new_grid[i,j] = gr.Default.default(grid,i,j)
            '''
            new_grid[i,j] = gr.Default.expanded_default(grid,i,j, 
                                                        condition=
                                                        [transition(0,1,(1,2)), 
                                                         transition(1,1,(2,3)),
                                                         transition(1,2,(4,))])
            '''
            '''
            new_grid[i,j] = gr.Default.expanded_default(grid,i,j,
                                                        condition=
                                                        [transition(0,1,(2,6)),
                                                         transition(1,1,(2,)),
                                                         transition(1,2,(3,)),
                                                         transition(2,2,(1,3)),
                                                         transition(2,1,(2,))])
            '''
            '''
            new_grid[i,j] = gr.Default.expanded_default2(grid,i,j,
                                                         condition=[
                                                          transition(0,1,(2,3)),
                                                          transition(0,2,(4,5)),
                                                          transition(1,1,(2,)),
                                                          transition(1,2,(3,)),
                                                          transition(2,2,(0,1))
                                                          ])
            '''
            '''
            new_grid[i,j] = universal_rule(grid,i,j,
                                                      rule=t.square_neigh_count(grid,i,j),
                                                      condition=[transition(0,1,(3,)),
                                                                 transition(1,1,(2,3))])
            '''
            new_grid[i,j] = conditional_rule(grid,i,j,
                                                        condition=[neigh_transition(0,1,(2,4), t.square_neigh_count(grid,i,j)),
                                                                   neigh_transition(1,1,(2,3), t.horivertical_neigh_count(grid,i,j))]
                                                        )
    return new_grid


    










def update_grid_segement(grid, new_grid, range_i:list=[0,0], range_j:list=[0,0]):
    for i in range(range_i[0], range_i[1]):
        for j in range(range_j[0], range_j[1]):
            #new_grid[i,j] = gr.Chess.knight(grid,i,j, stay_alive=[1], become_alive=[2,3])
            #new_grid[i,j] = gr.Chess.knight(grid,i,j, stay_alive=[1])
            #new_grid[i,j] = gr.Simple.horivertical(grid,i,j,2)
            #new_grid[i,j] = gr.Default.default(grid, i, j, 2,stay_alive=[3,5], become_alive=[2,4])
            #new_grid[i,j] = gr.Default.default(grid, i, j, 2,stay_alive=[3,4], become_alive=[3,4])
            #new_grid[i,j] = gr.Default.default(grid, i, j, 3,stay_alive=[3,4], become_alive=[3,4])
            #new_grid[i,j] = gr.Default.default(grid, i, j, 3,stay_alive=[2,3], become_alive=[3])
            #new_grid[i,j] = gr.Simple.horivertical(grid, i, j, 3, stay_alive=[2,3], become_alive=[2,4])
            #new_grid[i,j] = update_multi_rule(grid,i,j, alive=gr.Simple.horivertical(grid,i,j,1), dead=gr.Default.default(grid,i,j, become_alive=[2]))
            #new_grid[i,j] = update_multi_rule(grid,i,j, alive=gr.Chess.knight(grid,i,j,stay_alive=[1]), dead=gr.Default.default(grid,i,j, become_alive=[2]))
            #new_grid[i,j] = update_multi_rule(grid,i,j, alive=gr.Default.default(grid,i,j), dead=gr.Chess.knight(grid,i,j, become_alive=[1]))
            #new_grid[i,j] = update_multi_rule(grid,i,j, alive=gr.Default.default(grid,i,j, stay_alive=[2]), dead=gr.Chess.knight(grid,i,j, become_alive=[2]))
            #new_grid[i,j] = update_multi_rule(grid,i,j, dead=gr.Simple.horivertical(grid,i,j, become_alive=[1,2]), alive=gr.Default.default(grid,i,j, become_alive=[2]))
            #new_grid[i,j] = update_multi_rule(grid,i,j, dead=gr.Chess.knight(grid,i,j, become_alive=[1]),  alive=gr.Simple.horivertical(grid,i,j,1,stay_alive=[2]))
            new_grid[i,j] = update_multi_rule(grid,i,j, alive=gr.Chess.knight(grid,i,j, become_alive=[1], stay_alive=[1,2]),  dead=gr.Simple.horivertical(grid,i,j,1,stay_alive=[2], become_alive=[1]))
            


def update_grid_threading(grid, GRID_SIZE):
    new_grid = grid.copy()
    
    #'''
    t1 = threading.Thread(target=update_grid_segement, args=(grid, new_grid, [0,GRID_SIZE[0]//2], [0,GRID_SIZE[1]//2]))
    t2 = threading.Thread(target=update_grid_segement, args=(grid, new_grid, [0,GRID_SIZE[0]//2], [GRID_SIZE[1]//2,GRID_SIZE[1]]))
    t3 = threading.Thread(target=update_grid_segement, args=(grid, new_grid, [GRID_SIZE[0]//2,GRID_SIZE[0]], [0,GRID_SIZE[1]//2]))
    t4 = threading.Thread(target=update_grid_segement, args=(grid, new_grid, [GRID_SIZE[0]//2, GRID_SIZE[0]], [GRID_SIZE[1]//2, GRID_SIZE[1]]))
    
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    #'''
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




