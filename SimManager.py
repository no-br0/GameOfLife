import pygame
import DrawGrid
import UpdateGrid
import numpy as np
import tkinter as tk
import LateUpdate as lu
from random import randint

class Main_Window():
    def __init__(self):
        self.FPS = 60
        self.COUNTER = 0
        self.MAX_COUNTER = 10
        self.action_window = None
        self.WINDOW_SIZE = [1200, 1200]
        self.GRID_SIZE = [50,50,2]
        self.on_click_value = 1

        self.CELL_SIZE = [self.WINDOW_SIZE[0]// self.GRID_SIZE[0], self.WINDOW_SIZE[1]//self.GRID_SIZE[1]]
        
        self.simulating = False

        pygame.init()

        pygame.display.set_caption("Game Of Cells")

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
        state_to_change = randint(0,1)
        # Toggle the state of the cell
        if self.grid[i, j, state_to_change] == 0:
            new_grid[i, j, state_to_change] = self.on_click_value
        else:
            new_grid[i, j, state_to_change] = 0
            
        DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
        self.grid = new_grid
            
    
            


    def step(self):
        new_grid = UpdateGrid.update_grid(self.grid, self.GRID_SIZE)
        #new_grid = lu.late_update(new_grid, self.GRID_SIZE)
        DrawGrid.draw_grid(self.grid, new_grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
        self.grid=new_grid
        
    
    def alternate_play_pause(self):
        if self.simulating:
            if self.action_window != None:
                self.action_window.play_pause_button.configure(text="Play")
            self.simulating = False
        else:
            if self.action_window != None:
                self.action_window.play_pause_button.configure(text="Pause")
            self.simulating = True
    

    def reset_grid(self):
        self.simulating = False
        self.grid = np.zeros(self.GRID_SIZE, dtype=int)
        DrawGrid.draw_grid_initial(self.grid, self.screen, self.CELL_SIZE, self.GRID_SIZE)
