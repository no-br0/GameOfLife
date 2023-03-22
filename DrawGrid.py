import pygame
from Colors import DEAD, MUSHROOM

def draw_grid(grid, screen, CELL_SIZE, GRID_SIZE):
    # Clear the screen
    screen.fill(DEAD)

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Draw a rectangle for each cell
            rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
            if grid[i, j] == 1:
                pygame.draw.rect(screen, MUSHROOM, rect)
            else:
                pygame.draw.rect(screen, DEAD, rect, 1)

    # Update the screen
    pygame.display.update()