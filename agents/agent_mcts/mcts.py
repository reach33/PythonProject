import numpy as np
from .node import Node
from typing import Optional, Tuple
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_mcts(board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]) -> Tuple[PlayerAction, Optional[SavedState]]:
    
    Node.set_player(player)
    Node.update_root_by_board(board)
    simulate(4)
    move = PlayerAction(make_move())
    return [move,saved_state]

def simulate(simulation_depth: int):

    leaf = Node.get_leaf_by_best_value()
    leaf.create_children(simulation_depth)

def make_move() -> int:

    return Node.current_root.choose_child_as_move_by_weight().chosen_column

