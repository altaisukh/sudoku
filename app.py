import numpy as np
from sudoku import BoardController
from config import Config

"""
Architecture:
Model
1. board
2. updated board
3. taken_values

Controller
1. board - handles the logic of 
"""

def main():
    board = np.array(Config.TEST_BOARD)

    board_controller = BoardController()
    taken_values = np.zeros((9,9,9))
    count = 0

    while np.count_nonzero(board) < 81: 
        print("Board before running")
        print(board)
        print("Total Values {}".format(np.count_nonzero(board)))
        count += 1
        taken_values = board_controller.update_taken_values(taken_values, board)
        board = board_controller.update_only_options(taken_values, board)
        print("")
        print("Iteration {}".format(count))
        print(board)
        print("Total Values {}".format(np.count_nonzero(board)))

if __name__ == "__main__":
    main()