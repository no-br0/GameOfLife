import pygame
from Colors import colors
from random import randint

def draw_grid_initial(grid, screen, CELL_SIZE, GRID_SIZE):
    # Clear the screen
    screen.fill(colors[0])

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            state_to_draw = randint(0,1)
            # Draw a rectangle for each cell
            if grid[i,j, state_to_draw] != 0:
                rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
                pygame.draw.rect(screen,colors[grid[i,j, state_to_draw]], rect)

    # Update the screen
    pygame.display.update()



def draw_grid(grid, new_grid, screen, CELL_SIZE, GRID_SIZE):

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            state_to_draw = randint(0,1)
            # Draw a rectangle for each cell that has changed between grid and new_grid
            rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
            pygame.draw.rect(screen,colors[new_grid[i,j, state_to_draw]], rect)
                
    # Update the screen
    pygame.display.update()