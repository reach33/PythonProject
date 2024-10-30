from typing import Callable, Optional, Any
from enum import Enum
import numpy as np

BOARD_COLS = 7
BOARD_ROWS = 6
BOARD_SHAPE = (6, 7)
INDEX_HIGHEST_ROW = BOARD_ROWS - 1
INDEX_LOWEST_ROW = 0

BoardPiece = np.int8  # The data type (dtype) of the board pieces
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 (player to move first) has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 (player to move second) has a piece

BoardPiecePrint = str  # dtype for string representation of BoardPiece
NO_PLAYER_PRINT = BoardPiecePrint(' ')
PLAYER1_PRINT = BoardPiecePrint('X')
PLAYER2_PRINT = BoardPiecePrint('O')

PlayerAction = np.int8  # The column to be played

class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0

class MoveStatus(Enum):
    IS_VALID = 1
    WRONG_TYPE = 'Input is not a number.'
    NOT_INTEGER = ('Input is not an integer, or isn\'t equal to an integer in '
                   'value.')
    OUT_OF_BOUNDS = 'Input is out of bounds.'
    FULL_COLUMN = 'Selected column is full.'

class SavedState:
    pass

GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]


def initialize_game_state() -> np.ndarray:
    """
    Returns an ndarray, shape BOARD_SHAPE and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).
    """
    return np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece)

def pretty_print_board(board: np.ndarray) -> str:
    """
    Should return `board` converted to a human readable string representation,
    to be used when playing or printing diagnostics to the console (stdout). The piece in
    board[0, 0] of the array should appear in the lower-left in the printed string representation. Here's an example output, note that we use
    PLAYER1_Print to represent PLAYER1 and PLAYER2_Print to represent PLAYER2):
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """

    wall = "|"
    columns = "0 1 2 3 4 5 6"
    dividers = "============="
    ndarray_print = np.full(BOARD_SHAPE,NO_PLAYER_PRINT, BoardPiecePrint) # ndarray with the right datatyp (str), easier to converte `board` to a human readable string later

    ndarray_print_string =  wall + dividers + wall + "\n" # String we return at the end

    # Iterates through each array inside 'board' array and changes 'ndarray_print' to look identical
    for array in board:
        for element in array:
            if element == PLAYER1:
                ndarray_print[np.where(board == element)] = PLAYER1_PRINT
            if element == PLAYER2:
                ndarray_print[np.where(board == element)] = PLAYER2_PRINT       

    # Iterates through 'board' array, flips the inner arrays and the 'board' array itself so when printed everything is at the right place and appends the flipped arrays to ndarray_print_string
    for array in np.flip(ndarray_print):
        ndarray_print_string = ndarray_print_string + wall + " ".join(map(str, np.flip(array))) + wall + "\n"

    return ndarray_print_string + wall + dividers + wall + "\n" + wall + columns + wall


def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.
    This is quite useful for debugging, when the agent crashed and you have the last
    board state as a string.
    """

    ndarray_as_array = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # ndarray which we return at the end
    
    ndarray_as_list = pp_board.splitlines() # pp_board made into a list for easier manipulation
    
    # removes dividers and column number row
    ndarray_as_list.pop(0)
    ndarray_as_list.pop()
    ndarray_as_list.pop()
    
    for i in range (len(ndarray_as_list)):
        ndarray_as_list[i] = ndarray_as_list[i][1:-1] # removes walls from board arrays
        ndarray_as_list[i] = ndarray_as_list[i][::2] #creating the pp_board as asked, we had to put a ' ' between the values (" ".join(...) in def pretty_print_board). Here we remove them.
    
    for string in ndarray_as_list:
        for char in string:
            if char == "X":
                ndarray_as_array[5 - ndarray_as_list.index(string),string.index(char)] = PLAYER1
            if char == "O":
                ndarray_as_array[5 - ndarray_as_list.index(string),string.index(char)] = PLAYER2
    
    
    return ndarray_as_array

    


def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece):
    """
    Sets board[i, action] = player, where i is the lowest open row. The input 
    board should be modified in place, such that it's not necessary to return 
    something.
    """

    # Goes from board[0,action] to, board[1,action] and the moment he finds a free space, he changes the position to player and breaks
    for array in board:
        if array[action] == NO_PLAYER:
            array[action] = player
            break


def connected_four(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.
    """
    #main
            


def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still on-going (GameState.STILL_PLAYING)?
    """

    # führe vorherige funktion aus um win zu schauen
    # schau ob es noch NO_Player felder gibt, sonst ist draw. Wenn noch freie felde on going game
    raise NotImplementedError


def check_move_status(board: np.ndarray, column: Any) -> MoveStatus:
    """
    Returns a MoveStatus indicating whether a move is legal or illegal, and why 
    the move is illegal.
    Any column type is accepted if it is convertible to a number (e.g., '3' but 
    not 'a') and if the conversion results in a whole number (e.g., '3.0' would
    be okay, but not '3.1').
    Furthermore, the column must be within the bounds of the board and the
    column must not be full.
    """
    raise NotImplementedError