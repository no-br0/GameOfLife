import numpy as np
import pygame
import time
import threading

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set the dimensions of the screen
WINDOW_SIZE = [1000, 700]

# Set the dimensions of the grid
GRID_SIZE = [50, 50]

# Set the size of each cell in the grid
CELL_SIZE = [WINDOW_SIZE[0] // GRID_SIZE[0], WINDOW_SIZE[1] // GRID_SIZE[1]]

# Initialize the Pygame library
pygame.init()

# Set the title of the game window
pygame.display.set_caption("Conway's Game of Life")

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Create the grid
grid = np.zeros(GRID_SIZE, dtype=int)

# Define the starting pattern for the grid
grid[25, 24:26] = 1
grid[26, 25] = 1
grid[27, 25] = 1

# Define the function to update the grid
def update_grid_part(grid_part, new_grid_part, i_start, i_end):
    # Loop over each cell in the grid part
    for i in range(i_start, i_end):
        for j in range(GRID_SIZE[1]):
            # Count the number of live neighbors
            num_neighbors = np.sum(grid_part[max(i-1, 0):min(i+2, GRID_SIZE[0]), max(j-1, 0):min(j+2, GRID_SIZE[1])]) - grid_part[i, j]

            # Apply the rules of the game
            if grid_part[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_grid_part[i, j] = 0
            elif grid_part[i, j] == 0 and num_neighbors == 3:
                new_grid_part[i, j] = 1

def update_grid(grid):
    # Create a copy of the grid
    new_grid = grid.copy()

    # Define the number of threads to use
    num_threads = 4

    # Divide the grid into equal parts for each thread to process
    parts = np.array_split(grid, num_threads, axis=0)
    new_parts = np.array_split(new_grid, num_threads, axis=0)

    # Create a list of threads to update each part of the grid
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=update_grid_part, args=(parts[i], new_parts[i], parts[i].shape[0] // 2, parts[i].shape[0]))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return new_grid

# Define the function to draw the grid
def draw_grid(grid):
    # Clear the screen
    screen.fill(WHITE)

    # Loop over each cell in the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            # Draw a rectangle for each cell
            rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
            if grid[i, j] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect, 1)

    # Update the screen
    #pygame.display.flip()


# Define the function to handle mouse events
def handle_mouse_event():
    # Get the position of the mouse cursor
    pos = pygame.mouse.get_pos()

    # Convert the position to grid coordinates
    i = pos[0] // CELL_SIZE[0]
    j = pos[1] // CELL_SIZE[1]

    # Toggle the state of the cell
    if grid[i, j] == 0:
        grid[i, j] = 1
    else:
        grid[i, j] = 0


def reset_grid():
    global grid
    grid = np.zeros(GRID_SIZE, dtype=int)


# Define the main function
def main():
    global grid
    # Set the clock object
    clock = pygame.time.Clock()
    simulating = False

    # Run the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_event()
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    if simulating:
                        simulating = False
                    else:
                        simulating = True
                
                if event.key == pygame.K_c:
                    simulating = False
                    reset_grid()

            

        if simulating:
            # Update the grid
            grid = update_grid(grid)

        # Draw the grid
        draw_grid(grid)

        pygame.display.update()
        # Wait for a short time to limit the frame rate
        clock.tick(6)

# Call the main function
if __name__ == '__main__':
    main()

