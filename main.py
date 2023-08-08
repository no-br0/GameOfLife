import numpy as np
import pygame
import DrawGrid
import UpdateGrid

FPS = 60
COUNTER = 0
MAX_COUNTER = 20

WINDOW_SIZE = [1200, 1200]
GRID_SIZE = [150,150]

CELL_SIZE = [WINDOW_SIZE[0]// GRID_SIZE[0], WINDOW_SIZE[1]//GRID_SIZE[1]]

pygame.init()

pygame.display.set_caption("Basic Game Of Life")

screen = pygame.display.set_mode(WINDOW_SIZE)

grid = np.zeros(GRID_SIZE, dtype=int)


def handle_mouse_event():
    global grid
    # Get the position of the mouse cursor
    pos = pygame.mouse.get_pos()
    new_grid = grid.copy()

    # Convert the position to grid coordinates
    i = pos[0] // CELL_SIZE[0]
    j = pos[1] // CELL_SIZE[1]

    # Toggle the state of the cell
    if grid[i, j] == 0:
        new_grid[i, j] = 1
    else:
        new_grid[i, j] = 0
        
    DrawGrid.draw_grid(grid, new_grid, screen, CELL_SIZE, GRID_SIZE)
    grid = new_grid
        


def reset_grid():
    global grid
    grid = np.zeros(GRID_SIZE, dtype=int)
    DrawGrid.draw_grid_initial(grid, screen, CELL_SIZE, GRID_SIZE)




if __name__ == "__main__":
    DrawGrid.draw_grid_initial(grid, screen,CELL_SIZE,GRID_SIZE)
    simulating = False
    clock = pygame.time.Clock()
    
    
    
    while True:
        keys = pygame.key.get_pressed()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_event()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if simulating:
                        simulating = False
                    else:
                        simulating = True
                
                if event.key == pygame.K_e and simulating == False:
                    new_grid = UpdateGrid.update_grid(grid, GRID_SIZE)
                    DrawGrid.draw_grid(grid, new_grid, screen, CELL_SIZE, GRID_SIZE)
                    grid=new_grid
                    
                    
                if event.key == pygame.K_c:
                    simulating = False
                    reset_grid()
        
                
        #if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
        #    simulating = False
        #    reset_grid()
        
        new_grid = grid.copy()
            

        if simulating and COUNTER >= MAX_COUNTER:
            #grid = UpdateGrid.update_grid(grid, GRID_SIZE)            
            new_grid = UpdateGrid.update_grid(grid, GRID_SIZE) 
            
            COUNTER = 0
        else:
            COUNTER+=1
            
        DrawGrid.draw_grid(grid, new_grid, screen, CELL_SIZE, GRID_SIZE)
        
        grid = new_grid
        
        clock.tick(FPS)
        
