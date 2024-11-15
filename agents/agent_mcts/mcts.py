import numpy as np
from node import Node
from typing import Optional, Tuple
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_mcts(board: np.ndarray, saved_state: Optional[SavedState]) -> Tuple[PlayerAction, Optional[SavedState]]:
    pass