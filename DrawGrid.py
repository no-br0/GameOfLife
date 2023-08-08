import pygame
from Colors import colors
from Values import *


def draw_grid(grid, screen, CELL_SIZE, GRID_SIZE):
    # Clear the screen
    screen.fill(colors[0])

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Draw a rectangle for each cell
            if grid[i,j] != 0:
                rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
                pygame.draw.rect(screen,colors[grid[i,j]], rect)
            '''
            if grid[i,j] == Dead:
                pygame.draw.rect(screen, DEAD, rect)
            elif grid[i,j] == Mushroom:
                pygame.draw.rect(screen, MUSHROOM, rect)
            elif grid[i,j] == Grass:
                pygame.draw.rect(screen, GRASS, rect)
            elif grid[i,j] == Water:
                pygame.draw.rect(screen, WATER, rect)
            '''
    # Update the screen
    pygame.display.update()