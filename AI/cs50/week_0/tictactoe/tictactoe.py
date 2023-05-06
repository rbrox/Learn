"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count = 0
    
    for row in range(3):
        for col in range(3):
            
            ele = board[row][col]
            if (ele == EMPTY):
                count += 1
    
    if count % 2 == 1: 
        return X
    else:
        return O

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions = []
    
    for row in range(3):
        for col in range(3):
            
            ele = board[row][col]
            if (ele == EMPTY):
                actions.append(row, col)            
    
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    ele = actions(board)
    
    board[action[0]][action[1]] = ele
    
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 8 possible winning states
    
      
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
