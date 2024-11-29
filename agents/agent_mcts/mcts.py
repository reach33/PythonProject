import numpy as np
from .node import Node
from typing import Optional, Tuple
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_mcts(board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]) -> Tuple[PlayerAction, Optional[SavedState]]:
    """
    Generates the next move for a player using the Monte Carlo Tree Search (MCTS) algorithm.

    Args:
        board (np.ndarray): The current state of the game board.
        player (BoardPiece): The current player making the move (PLAYER1 or PLAYER2).
        saved_state (Optional[SavedState]): An optional saved state for the game (not utilized here).

    Returns:
        Tuple[PlayerAction, Optional[SavedState]]: The column index where the player will place their piece 
        and the (unchanged) saved state.
    """
    Node.set_player(player)
    Node.update_root_by_board(board)
    simulate(4)#should repeatedly chose by ubs (oder so) until time ends (if max 5 sec then stop by 4,5?) not just simulate depth
    simulate(4)
    simulate(4)
    simulate(4)
    simulate(4)
    simulate(4)
    move = PlayerAction(make_move())
    return [move, saved_state]


def simulate(simulation_depth: int):
    """
    Simulates potential future moves to a specified depth by expanding the tree from the best leaf node.

    Args:
        simulation_depth (int): The depth to which the game tree should be expanded.
    """
    leaf = Node.get_leaf_by_best_value()
    leaf.create_children(simulation_depth)


def make_move() -> int:
    """
    Selects the next move based on the highest-weighted child node.

    Returns:
        int: The column index corresponding to the best move chosen by the MCTS algorithm.
    """
    return Node.current_root.choose_child_as_move_by_weight().chosen_column
