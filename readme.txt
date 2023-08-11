Explains the purpose of each main file

main:
    -the main file which is the file that is used to run the program
    -contains the main function with the programs infinite loop


SimManager:
    -contains the class for working with the simulation
    -the class contains the main functions used for working with and manipulating the simulation


DrawGrid:
    -handles the drawing of the grid for the SimManager


ActionCentre:
    -handles the tkinter window for easily working with the simulation
    -used as the interface for things like 
        -saving and loading of specific draw_grid_initial
        -play,pause,reset of the simulation


UpdateGrid:
    -contains basic loops for updating the grid and for calling the appropriate rulesets to used

Colors:
    -contains the colors for easy assignment of color to value (the number of the cell is used for the position in the list of the appropriate color)