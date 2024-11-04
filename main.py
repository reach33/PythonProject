import numpy as np

from game_utils import BOARD_COLS, BOARD_ROWS, BOARD_SHAPE, NO_PLAYER, PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT, BoardPiece, NO_PLAYER_PRINT, BoardPiecePrint, PlayerAction, pretty_print_board, INDEX_HIGHEST_ROW
    
"""

# Aufgabe 1

ndarray = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece)

print(ndarray)

"""
"""

# Aufgabe 2

board = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # kriegen wir als parameter eigentlich

board[2,1] = PLAYER1 # Beispiel Element
board[0,4] = PLAYER2 # Beispiel Element

wall = "|"
columns = "0 1 2 3 4 5 6"
dividers = "============="
ndarray_print = np.full(BOARD_SHAPE,NO_PLAYER_PRINT, BoardPiecePrint)


ndarray_print_string =  wall + dividers + wall + "\n"

for array in board:
    for element in array:
        if element == PLAYER1:
            ndarray_print[np.where(board == element)] = PLAYER1_PRINT
        if element == PLAYER2:
            ndarray_print[np.where(board == element)] = PLAYER2_PRINT       

for array in np.flip(ndarray_print):
    ndarray_print_string = ndarray_print_string + wall + " ".join(map(str, np.flip(array))) + wall + "\n"

print(ndarray_print_string + wall + dividers + wall + "\n" + wall + columns + wall)

"""
"""

# Aufgabe 3

pp_board = ndarray_print_string + wall + dividers + wall + "\n" + wall + columns + wall # Parameter normalerweise
ndarray_as_array = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # Das ndarray, welches am ende returned wird

ndarray_as_list = ndarray_print_string.splitlines()

ndarray_as_list.pop(0)
ndarray_as_list.pop()
ndarray_as_list.pop()

for i in range(len(ndarray_as_list)):
    ndarray_as_list[i] = ndarray_as_list[i][1:-1]
    ndarray_as_list[i] = ndarray_as_list[i][::2]

for string in ndarray_as_list:
    for char in string:
        if char == "X":
            ndarray_as_array[5 - ndarray_as_list.index(string),string.index(char)] = PLAYER1
        if char == "O":
            ndarray_as_array[5 - ndarray_as_list.index(string),string.index(char)] = PLAYER2

print(ndarray_as_list)
print(ndarray_as_array)

"""

"""
# Aufgabe 4

board = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # kriegen wir als parameter eigentlich
action = 3 # Column wo reingespielt wird
Player = PLAYER1 # Player der reinwirft

print(pretty_print_board(board))

board[0,0] = PLAYER2
board[0,3] = PLAYER2

for array in board:
    if array[action] == NO_PLAYER:
        array[action] = Player
        break

print(pretty_print_board(board))

"""

"""
#Aufgabe 5

board = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # kriegen wir als parameter eigentlich
player = PLAYER1 # Player der reinwirft

# kriegen wir eigentlich mit fertigem board
board[0,5] = PLAYER1
board[0,4] = PLAYER2
board[1,2] = PLAYER1
board[0,2] = PLAYER1
board[0,3] = PLAYER1
board[0,1] = PLAYER1
board[1,3] = PLAYER2
board[2,3] = PLAYER1
board[1,4] = PLAYER1
board[1,1] = PLAYER1
board[2,2] = PLAYER2
board[0,6] = PLAYER1
board[3,2] = PLAYER1

print(pretty_print_board(board))            #printer

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

win = False# helper delet later (to change with game state or something like that)

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
            win = True
            break
        connected_stones_row = 0    
    if connected_stones_row >= 4:
        win = True
        break
    if row >= 3: # column check
        for i in range(BOARD_ROWS - (BOARD_ROWS-1-row)):
            if board[row-i, column] == player:
                connected_stones_column += 1
                continue
            break
        if connected_stones_column >= 4:
            win = True
            break
    
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
        win = True
        break
print(win)# helper print delete later

"""
