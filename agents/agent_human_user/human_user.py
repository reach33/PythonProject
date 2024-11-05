import numpy as np

from game_utils import BoardPiece, PlayerAction, SavedState, MoveStatus, check_move_status
from typing import Optional, Callable, Any


def query_user(prompt_function: Callable) -> Any:
    usr_input = prompt_function("Column? ")
    return usr_input


def user_move(board: np.ndarray,
              _player: BoardPiece,
              saved_state: SavedState | None) -> tuple[PlayerAction, SavedState | None]:
    move_status = None
    while move_status != MoveStatus.IS_VALID:
        if move_status is not None:
            print('Invalid move: ', move_status.value)
            print('Please try again.')
        input_move_string = query_user(input)
        move_status = check_move_status(board, input_move_string)

    input_move_integer = PlayerAction(float(input_move_string))
    return input_move_integer, saved_state