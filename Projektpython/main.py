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

#Aufgabe 5

board = np.full(BOARD_SHAPE,NO_PLAYER, BoardPiece) # kriegen wir als parameter eigentlich
player = PLAYER1 # Player der reinwirft


board[0,5] = PLAYER1
board[3,4] = PLAYER1
board[1,2] = PLAYER1
board[0,1] = PLAYER1
board[0,2] = PLAYER1
board[0,3] = PLAYER1
board[1,1] = PLAYER1
board[3,3] = PLAYER2
board[2,3] = PLAYER1
board[2,4] = PLAYER2
board[5,4] = PLAYER1
board[5,5] = PLAYER1
board[0,0] = PLAYER1


print(board)
print(pretty_print_board(board))


rows, columns = np.where(board == player)
for i in range(BOARD_COLS):
    pass



"""b = (board == player)
zeilen, spalten = b.shape
for i in range(0, zeilen, 1):
  for j in range(0, spalten, 1):
    # Hier fehlt evtl. ein Check, ob du überhaupt so ne große Submatrix hast
    s = b[i:i+4, j:j+4]
    if np.any(s.sum(0) == 4) or np.any(s.sum(1) == 4) or np.diag(s).sum() == 4 or np.diag(s[::-1, ::-1]).sum() == 4:
      print(True)"""