import numpy as np
import random
from typing import Optional, Tuple
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_random(
board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]
) -> Tuple[PlayerAction, Optional[SavedState]]:
    # Choose a valid, non-full column randomly and return it as `action`

    action = random.randint(0,BOARD_COLS-1)
    while(not check_move_status(board, action) == MoveStatus.IS_VALID):
        action = random.randint(0,BOARD_COLS-1)
    return [action, saved_state]