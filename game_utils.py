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

#neu von ihm ohne integer check
class MoveStatus(Enum):
    IS_VALID = 1
    WRONG_TYPE = 'Input does not have the correct type (PlayerAction).'
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
    # Every top Stone from player
    columns_top_positions_player = []

    # Get the top stones form player in every column
    for i in range(BOARD_COLS):
        for j in range(BOARD_ROWS):
            if board[BOARD_ROWS-1-j, i] == NO_PLAYER:
                continue
            if board[BOARD_ROWS-1-j, i] == player:
                columns_top_positions_player.append((BOARD_ROWS-1-j, i))
                break
            break                             

    # Checks row and columns from the collected top stones if 4 stones from player are connected
    # Could be in the loop above (if == player) but is in an extra function for better reading/understanding
    for (row, column) in columns_top_positions_player:
        connected_stones_row = 0
        connected_stones_column = 0
        for i in range(BOARD_COLS): # row check
            if board[row,i] == player:
                connected_stones_row += 1
                continue
            if connected_stones_row  >= 4:
                return True
            connected_stones_row = 0    
        if connected_stones_row >= 4:
            return True
        if row >= 3: # column check
            for i in range(BOARD_ROWS - (BOARD_ROWS-1-row)):
                if board[row-i, column] == player:
                    connected_stones_column += 1
                    continue
                break
            if connected_stones_column >= 4:
                return True
            
        # Connections per diagonal (Northeast, SouthWest, etc.) from our top stone
        diagonal_NE = 0
        diagonal_NW = 0
        diagonal_SE = 0
        diagonal_SW = 0
        #Tells the diagonal checker which diagonal still needs to be checked
        Stopp_NE = True
        Stopp_NW = True
        Stopp_SE = True
        Stopp_SW = True


        for i in range(BOARD_COLS): # diagonal check
            if Stopp_SW and row - i >= 0 and column - i >= 0 and board[row - i, column - i] == player:
                diagonal_SW += 1
            else: Stopp_SW = False
            if Stopp_NE and row + i < BOARD_ROWS and column + i < BOARD_COLS and board[row + i, column + i] == player:
                diagonal_NE += 1
            else: Stopp_NE = False
            if Stopp_SE and row - i >= 0 and column + i < BOARD_COLS and board[row - i, column + i] == player:
                diagonal_SE += 1
            else: Stopp_SE = False
            if Stopp_NW and row + i < BOARD_ROWS and column - i >= 0 and board[row + i, column - i] == player:
                diagonal_NW += 1
            else: Stopp_NW = False
        if diagonal_SW + diagonal_NE - 1 >= 4 or diagonal_SE + diagonal_NW - 1 >= 4:
            return True
    return False


def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still on-going (GameState.STILL_PLAYING)?
    """
    if connected_four(board, player):
        return GameState.IS_WIN
    if np.any(board[BOARD_ROWS-1] == NO_PLAYER):
        return GameState.STILL_PLAYING
    return GameState.IS_DRAW


def check_move_status(board: np.ndarray, column: Any) -> MoveStatus:
    #seine neue implementierung
    """
    Returns a MoveStatus indicating whether a move is accepted as a valid move 
    or not, and if not, why.
    The provided column must be of the correct type (PlayerAction).
    Furthermore, the column must be within the bounds of the board and the
    column must not be full.
    """
        
    #Is column typ Playeraction?
    if not isinstance(column, PlayerAction):
        return MoveStatus.WRONG_TYPE
    
    #Is column in Bounds?
    if not (int(column) >= 0 and int(column) < BOARD_COLS):
        return MoveStatus.OUT_OF_BOUNDS
    
    #Is given column full?
    if not board[BOARD_ROWS-1, int(column)] == NO_PLAYER:
        return MoveStatus.FULL_COLUMN
    
    return MoveStatus.IS_VALID
