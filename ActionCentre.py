import tkinter as tk
from SimManager import Main_Window
from Colors import colors

class Action_Window():
    def __init__(self, main_window:Main_Window):
        self.main_window = main_window
        self.main_window.action_window = self
        
        self.root = tk.Tk()
        self.root.geometry("300x900+200+300")
        
        # for playing and pausing game
        self.play_pause_button = tk.Button(self.root, text="Play", command=main_window.alternate_play_pause)
        self.play_pause_button.pack()
        
        # for taking a step in the simulation
        self.step_button = tk.Button(self.root, text="Step", command=main_window.step)
        self.step_button.pack()
        
        # for taking a step in the simulation
        self.reset_button = tk.Button(self.root, text="Clear Grid", command=self.main_window.reset_grid)
        self.reset_button.pack()
        
        # grid_set is related to setting what type of cell is desired to place
        self.grid_set_label = tk.Label(self.root, text="Cell Type To Place")
        self.grid_set_label.pack()
        
        self.grid_set_dropdown_options = []
        for i in range(len(colors)):
            self.grid_set_dropdown_options.append(str(i))
        
        self.grid_set_dropdown_selected = tk.StringVar()
        self.grid_set_dropdown_selected.set("1")
        
        self.grid_set_dropdown = tk.OptionMenu(self.root, 
                                               self.grid_set_dropdown_selected, 
                                               *self.grid_set_dropdown_options)
        self.grid_set_dropdown.pack()
        
        # button for the purpose of applying the change of cell to be placed
        self.grid_set_button = tk.Button(self.root, text="Apply Value", command=self.grid_set_onApply)
        self.grid_set_button.pack()
        
        
        
        
    def grid_set_onApply(self):
        self.main_window.on_click_value = int(self.grid_set_dropdown_selected.get())
        
        
        