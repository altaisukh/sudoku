import numpy as np
from config import Config

class BoardController(object):
    def __init__(self):
        """
        :params numpy_array board_array: A 9 x 9 numpy array. 
        """
    
    def get_square_range(self, row_column, nine=True):
        """
        :params int row_column:
        :params bool nine: Enter true if for a row of nine digits. Enter False if 3 x 3
        :return tuple: The low and high values of a square. 
        """
        if nine:
            return (int(np.floor(row_column/3)*3), int(np.floor(row_column/3 +1) * 3))
        return (row_column * 3 , (row_column + 1) * 3)
    
    def update_taken_values(self,taken_values, board):
        """
        :params numpy.array taken_values: An array of lists with the values that are taken by a combination of the row/column/square.
        :params numpy.array board_array: A representation of the board. A 9X9 matrix with None for unknowns and a number for filled in values.
        :return taken_values:
        Iterate through the board. If a value is in a row/column/square, update the taken values matrix with the 1s for all rows/columns/squares
        """ 
        updated_taken_values = taken_values
        for index, val in np.ndenumerate(board):
            if val:
                # update space as taken on all boards
                updated_taken_values[:,index[0], index[1]] = 1

                # update rows as taken
                updated_taken_values[val - 1, index[0], :] = 1

                # update columns as taken
                updated_taken_values[val - 1, :, index[1]] = 1

                # update square as taken
                x_low, x_high = self.get_square_range(index[0]) 
                y_low, y_high = self.get_square_range(index[1])

                updated_taken_values[val - 1, x_low:x_high, y_low:y_high] = 1
        return updated_taken_values

    def get_index_zero_value(self, taken_array):
        """
        :params np_array taken_array: (9,) shape np array with 1s and 0s. 
        :return int or None: return int of index if there is only one space left, else return None
        """
        batch_sum = taken_array.sum()
        if batch_sum == 8:
            return np.where(taken_array == 0)[0][0]
        return None
      
    def update_only_options(self, taken_values, board):
        """
        :params numpy.array taken_values: An array of lists with the values that are taken by a combination of the row/column/square.
        :params numpy.array board_array: A representation of the board. A 9X9 matrix with None for unknowns and a number for filled in values.
        :return updated_board:  
        In Sudoku, a number can be filled in when all other values in a row/column/square are impossible for a given value. 

        For instance, if 1 is considered unplayable in all areas of a row/column/square but one remaining location, 1 can be played.
        """
        for i in range(9):
            value = i + 1
            for j in range(9):
                y = self.get_index_zero_value(taken_values[i,j,:])
                if y:
                    board[j, y] = value
                x = self.get_index_zero_value(taken_values[i,:,j])
                if x:
                    board[x, j] = value
            for x in range(3):
                for y in range(3):
                    x_low, x_high = self.get_square_range(x, nine=False)
                    y_low, y_high = self.get_square_range(y, nine=False)
                    taken_array = taken_values[i,x_low : x_high, y_low : y_high]
                    square_sum = taken_array.sum()
                    if square_sum == 8:
                        x_delta, y_delta = np.where(taken_array == 0)
                        x_val = x_low + x_delta[0]
                        y_val = y_low + y_delta[0]
                        board[x_val, y_val] = value
        return board



        