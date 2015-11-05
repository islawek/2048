"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    return_line = []
    for temp in range(0, len(line)):
        return_line.append(0)
    
    #slide all of the numbers to the left, leave zeros at the end
    last_index = 0
    for temp in range(0, len(line)):
        if line[temp] != 0:
            return_line[last_index] = line[temp]
            last_index += 1
    
    #merge if two numbers in a row are the same
    for temp in range(0, len(line) - 1):
        if return_line[temp] == return_line[temp+1]:
            return_line[temp] *= 2
            return_line[temp+1] = 0
    
    #slide numbers to the left
    for temp in range(0, len(line)-1):
        if return_line[temp] == 0:
            for temp_2 in range(temp+1, len(line)):
                if return_line[temp_2] != 0:
                    return_line[temp] = return_line[temp_2]
                    return_line[temp_2] = 0
                    break                 
       
    return return_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
               

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_string = ""
        for row in range(self._grid_height):
            grid_string = grid_string + str(self._grid[row]) + "\n"
        return grid_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == LEFT:
            for row in range(self._grid_height):
                self._grid[row] = merge(self._grid[row])
        elif direction == RIGHT:
            for row in range(self._grid_height):
                temp_list = self._grid[row]
                temp_list.reverse()
                temp_list = merge(temp_list)
                temp_list.reverse()
                self._grid[row] = temp_list
        elif direction == UP:
            for col in range(0, self._grid_width):
                temp_list = []
                for row in range(0, self._grid_height):
                    temp_list.append(self._grid[row][col])
                temp_list = merge(temp_list)
                for row in range(0, self._grid_height):
                    self._grid[row][col] = temp_list.pop(0)
        elif direction == DOWN:
            for col in range(0, self._grid_width):
                temp_list = []
                for row in range(0, self._grid_height):
                    temp_list.append(self._grid[row][col])
                temp_list.reverse()
                temp_list = merge(temp_list)
                temp_list.reverse()
                for row in range(0, self._grid_height):
                    self._grid[row][col] = temp_list.pop(0)        
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        choice = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        is_zero = False
        for row in range(0, self._grid_height):
            for col in range(0, self._grid_width):
                if self._grid[row][col] == 0: 
                    is_zero = True
                    break
                
        while(is_zero):	
            col = random.randrange(0, self._grid_width)
            row = random.randrange(0, self._grid_height)
            if(self._grid[row][col] == 0):
                self._grid[row][col] = random.choice(choice)
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#some code for debugging 

#new_game = TwentyFortyEight(4,6)
#print new_game
#new_game.set_tile(2, 1, 3)
#new_game.set_tile(1, 1, 3)
#new_game.move(DOWN)
#print new_game
