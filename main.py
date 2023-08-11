import numpy as np
import pygame
import DrawGrid
import UpdateGrid
import ActionCentre as ac
import SimManager as sm



def main(main_window:sm.Main_Window, action_window:ac.Action_Window):
    #global grid, screen, CELL_SIZE, GRID_SIZE, FPS, COUNTER, MAX_COUNTER
    
    DrawGrid.draw_grid_initial(main_window.grid, main_window.screen, main_window.CELL_SIZE, main_window.GRID_SIZE)
    simulating = False
    clock = pygame.time.Clock()
    
    
    
    while True:
        keys = pygame.key.get_pressed()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                main_window.handle_mouse_event()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if simulating:
                        simulating = False
                    else:
                        simulating = True
                
                if event.key == pygame.K_e and simulating == False:
                    new_grid = UpdateGrid.update_grid(main_window.grid, main_window.GRID_SIZE)
                    DrawGrid.draw_grid(main_window.grid, new_grid, main_window.screen, main_window.CELL_SIZE, main_window.GRID_SIZE)
                    main_window.grid=new_grid
                    
                    
                if event.key == pygame.K_c:
                    simulating = False
                    main_window.reset_grid()
        
                
        #if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
        #    simulating = False
        #    reset_grid()
        
        new_grid = main_window.grid.copy()
            

        if simulating and main_window.COUNTER >= main_window.MAX_COUNTER:
            #grid = UpdateGrid.update_grid(grid, GRID_SIZE)            
            new_grid = UpdateGrid.update_grid(main_window.grid, main_window.GRID_SIZE) 
            DrawGrid.draw_grid(main_window.grid, new_grid, main_window.screen, main_window.CELL_SIZE, main_window.GRID_SIZE)
            main_window.COUNTER = 0
        else:
            main_window.COUNTER+=1
            
        #DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
        
        main_window.grid = new_grid
        action_window.root.update()
        clock.tick(main_window.FPS)


if __name__ == "__main__":
    main_window = sm.Main_Window()
    action_window = ac.Action_Window(main_window)
    main(main_window, action_window)
    
        
