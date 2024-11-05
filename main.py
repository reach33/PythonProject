"""

import numpy as np
from game_utils import *

"""

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

# Aufgabe 5

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

"""

# Aufgabe 6 und Aufgabe 7

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
board[1,1] = PLAYER1
board[2,2] = PLAYER2
board[0,6] = PLAYER1
board[3,2] = PLAYER1

board.fill(PLAYER2)
board[5,4] = NO_PLAYER
print(pretty_print_board(board))

print(check_end_state(board, player))
print(check_move_status(board, "42"))

test github

"""
from typing import Callable
import time
from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT, GameState, MoveStatus, GenMove
from game_utils import initialize_game_state, pretty_print_board, apply_player_action, check_end_state, check_move_status
from agents import user_move, generate_move




def human_vs_agent(
    generate_move_1: GenMove,
    generate_move_2: GenMove = user_move,   #   Switch between 'user_move' and 'generate_move' to play Human/Random-Agent
    player_1: str = "Player 1",
    player_2: str = "Player 2",
    args_1: tuple = (),
    args_2: tuple = (),
    init_1: Callable = lambda board, player: None,
    init_2: Callable = lambda board, player: None,
):

    players = (PLAYER1, PLAYER2)
    for play_first in (1, -1):
        for init, player in zip((init_1, init_2)[::play_first], players):
            init(initialize_game_state(), player)

        saved_state = {PLAYER1: None, PLAYER2: None}
        board = initialize_game_state()
        gen_moves = (generate_move_1, generate_move_2)[::play_first]
        player_names = (player_1, player_2)[::play_first]
        gen_args = (args_1, args_2)[::play_first]

        playing = True
        while playing:
            for player, player_name, gen_move, args in zip(
                players, player_names, gen_moves, gen_args,
            ):
                t0 = time.time()
                print(pretty_print_board(board))
                print(
                    f'{player_name} you are playing with {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                )
                action, saved_state[player] = gen_move(
                    board.copy(),  # copy board to be safe, even though agents shouldn't modify it
                    player, saved_state[player], *args
                )
                print(f'Move time: {time.time() - t0:.3f}s')

                move_status = check_move_status(board, action)
                if move_status != MoveStatus.IS_VALID:
                    print(f'Move {action} is invalid: {move_status.value}')
                    print(f'{player_name} lost by making an illegal move.')
                    playing = False
                    break

                apply_player_action(board, action, player)
                end_state = check_end_state(board, player)

                if end_state != GameState.STILL_PLAYING:
                    print(pretty_print_board(board))
                    if end_state == GameState.IS_DRAW:
                        print('Game ended in draw')
                    else:
                        print(
                            f'{player_name} won playing {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                        )
                    playing = False
                    break


if __name__ == "__main__":
    human_vs_agent(user_move)