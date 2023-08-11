import numpy as np
import pygame
import DrawGrid
import UpdateGrid




class Main_Window():
    def __init__(self):
        self.FPS = 60
        self.COUNTER = 0
        self.MAX_COUNTER = 0

        self.WINDOW_SIZE = [1200, 1200]
        self.GRID_SIZE = [150,150]

        self.CELL_SIZE = [self.WINDOW_SIZE[0]// self.GRID_SIZE[0], self.WINDOW_SIZE[1]//self.GRID_SIZE[1]]

        pygame.init()

        pygame.display.set_caption("Basic Game Of Life")

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        self.grid = np.zeros(self.GRID_SIZE, dtype=int)


    def handle_mouse_event(self):
        #global grid
        # Get the position of the mouse cursor
        pos = pygame.mouse.get_pos()
        new_grid = self.grid.copy()

        # Convert the position to grid coordinates
        i = pos[0] // self.CELL_SIZE[0]
        j = pos[1] // self.CELL_SIZE[1]

        # Toggle the state of the cell
        if self.grid[i, j] == 0:
            new_grid[i, j] = 1
        else:
            new_grid[i, j] = 0
            
        DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
        self.grid = new_grid
            


    def reset_grid(self):
        #global grid
        self.grid = np.zeros(self.GRID_SIZE, dtype=int)
        DrawGrid.draw_grid_initial(self.grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)



    def main(self):
        #global grid, screen, CELL_SIZE, GRID_SIZE, FPS, COUNTER, MAX_COUNTER
        
        DrawGrid.draw_grid_initial(self.grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
        simulating = False
        clock = pygame.time.Clock()
        
        
        
        while True:
            keys = pygame.key.get_pressed()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_event()
                    
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if simulating:
                            simulating = False
                        else:
                            simulating = True
                    
                    if event.key == pygame.K_e and simulating == False:
                        new_grid = UpdateGrid.update_grid(self.grid, self.GRID_SIZE)
                        DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
                        self.grid=new_grid
                        
                        
                    if event.key == pygame.K_c:
                        simulating = False
                        self.reset_grid()
            
                    
            #if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
            #    simulating = False
            #    reset_grid()
            
            new_grid = self.grid.copy()
                

            if simulating and self.COUNTER >= self.MAX_COUNTER:
                #grid = UpdateGrid.update_grid(grid, GRID_SIZE)            
                new_grid = UpdateGrid.update_grid(self.grid, self.GRID_SIZE) 
                DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
                self.COUNTER = 0
            else:
                self.COUNTER+=1
                
            #DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
            
            self.grid = new_grid
            
            clock.tick(self.FPS)


if __name__ == "__main__":
    simulation_window = Main_Window()
    simulation_window.main()
        
