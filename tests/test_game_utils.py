import sys
sys.path.append(r"C:\Users\amirm\Desktop\PythonProject")
sys.path.append(r"C:\Users\Amir\Desktop\PythonProject")
import numpy as np

from game_utils import *

def test_initialize_game_state():
    board = initialize_game_state()
    assert board.shape == (BOARD_ROWS, BOARD_COLS)
    assert np.all(board == NO_PLAYER)

def test_apply_player_action():
    board = initialize_game_state()
    apply_player_action(board, PlayerAction(0), PLAYER1)
    assert board[0, 0] == PLAYER1
    apply_player_action(board, PlayerAction(0), PLAYER2)
    assert board[1, 0] == PLAYER2

def test_connected_four_horizontal():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    board[5, 1] = PLAYER1
    board[5, 2] = PLAYER1
    board[5, 3] = PLAYER1
    assert connected_four(board, PLAYER1)

def test_connected_four_vertical():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    board[4, 0] = PLAYER1
    board[3, 0] = PLAYER1
    board[2, 0] = PLAYER1
    assert connected_four(board, PLAYER1)

def test_connected_four_diagonal():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    board[4, 1] = PLAYER1
    board[3, 2] = PLAYER1
    board[2, 3] = PLAYER1
    assert connected_four(board, PLAYER1)

def test_no_connected_four():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    board[4, 1] = PLAYER1
    board[3, 2] = PLAYER1
    assert not connected_four(board, PLAYER1)

def test_check_end_state_win():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    board[5, 1] = PLAYER1
    board[5, 2] = PLAYER1
    board[5, 3] = PLAYER1
    assert check_end_state(board, PLAYER1) == GameState.IS_WIN

def test_check_end_state_still_playing():
    board = initialize_game_state()
    board[5, 0] = PLAYER1
    assert check_end_state(board, PLAYER1) == GameState.STILL_PLAYING

def test_check_move_status_valid_move():
    board = initialize_game_state()
    move_status = check_move_status(board, PlayerAction(0))
    assert move_status == MoveStatus.IS_VALID

def test_check_move_status_wrong_type():
    board = initialize_game_state()
    move_status = check_move_status(board, "not an int")
    assert move_status == MoveStatus.WRONG_TYPE

def test_check_move_status_out_of_bounds():
    board = initialize_game_state()
    move_status = check_move_status(board, PlayerAction(7))
    assert move_status == MoveStatus.OUT_OF_BOUNDS

def test_check_move_status_full_column():
    board = initialize_game_state()
    for row in range(BOARD_ROWS):
        board[row, 0] = PLAYER1
    move_status = check_move_status(board, PlayerAction(0))
    assert move_status == MoveStatus.FULL_COLUMN
