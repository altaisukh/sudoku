import numpy as np

class Config:
    NEW_BOARD = np.zeros((9,9))
    TEST_BOARD_OLD = [[None, None, None, 4, None, 8, None, 7, None],
    [None, None, 4, None, 7, None, None, 3, None],
    [9, 8, None, None, 6, None, None, None, None],
    [None,None,2,None,None,None,None,None,1],
    [7, None,None,None,None,None,None,None,None],
    [None,6,None,8,5,None,2,None,None],
    [None,2,1,None,None,None,None,None,None],
    [None,None,None,9,None,3,None,None, None],
    [None,None,None,5,None,None,None,None,None]]
    TEST_BOARD = [[3, None, None, None, 8, None, None, None, 6],
    [None, 1, None, None, None, 6, None, 2, None],
    [None, None, 4, 7, None, None, 5, None, None],
    [None,4,None,None,1,None,9,None,None],
    [6, None,None,2,None,4,None,None,1],
    [None,None,3,None,6,None,None,5,None],
    [None,None,8,None,None,3,6,None,None],
    [None,2,None,4,None,None,None,1, None],
    [5,None,None,None,2,None,None,None,7]]
    NEW_TEST =[[3,5,None, 1, None, 4, None, None, None],
    [4, None, None, None, 2, None, 5, None, 7],
    [None, 1, None, None, 8, 7, 9, None, None],
    [None, 3, None, 9, None, None, None, None, 1],
    [None, 4, None, None, 3, None, None, 2, None],
    [6, None, None, None, None, 8, None, 7, None],
    [None, None, 4, 2, 5, None, None, 9, None],
    [5, None, 2, None, 6, None, None, None, 4],
    [None, None, None, 7, None, 1, None, 5, 8]]
    COMPLETE_ROW = list(range(1,10))

