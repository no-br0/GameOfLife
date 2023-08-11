import numpy as np
import pygame
import DrawGrid
import UpdateGrid
from ActionCentre import Action_Window
from SimManager import Main_Window



def main(main_window:Main_Window, action_window:Action_Window):
    
    DrawGrid.draw_grid_initial(main_window.grid, main_window.screen, main_window.CELL_SIZE, main_window.GRID_SIZE)
    clock = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                main_window.handle_mouse_event()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_window.alternate_play_pause()
                
                if event.key == pygame.K_e and main_window.simulating == False:
                    main_window.step()
                    
                    
                if event.key == pygame.K_c:
                    main_window.reset_grid()
        
                
        if main_window.simulating:
            if main_window.COUNTER >= main_window.MAX_COUNTER:
                main_window.step()
                main_window.COUNTER = 0
            else:
                main_window.COUNTER+=1
            
        
        
        
        action_window.root.update()
        
        clock.tick(main_window.FPS)



#if __name__ == "__main__":
main_window = Main_Window()
action_window = Action_Window(main_window)
main(main_window, action_window)
    
        
