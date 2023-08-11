import pygame
import DrawGrid
import numpy as np


class Main_Window():
    def __init__(self):
        self.FPS = 60
        self.COUNTER = 0
        self.MAX_COUNTER = 10

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
