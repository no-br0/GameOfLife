import tkinter as tk
from SimManager import Main_Window

class Action_Window():
    def __init__(self, main_window:Main_Window):
        self.main_window = main_window
        self.main_window.action_window = self
        
        self.root = tk.Tk()
        self.root.geometry("300x900+200+300")
        #self.root.mainloop()
        self.reset_button = tk.Button(self.root, text="Clear Grid", command=self.main_window.reset_grid)
        self.reset_button.pack()
        
        self.step_button = tk.Button(self.root, text="Step", command=main_window.step)
        self.step_button.pack()
        
        self.play_pause_button = tk.Button(self.root, text="Play", command=main_window.alternate_play_pause)
        self.play_pause_button.pack()
        
        