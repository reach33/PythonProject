import numpy as np
from .node import Node
from typing import Optional, Tuple
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_mcts(board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]) -> Tuple[PlayerAction, Optional[SavedState]]:
    
    Node.set_player(player)
    Node.update_root_by_board(board)
    simulate(4)
    pass

def simulate(simulation_depth: int):
    leaf = Node.get_leaf_by_best_value
    if simulation_depth > 0:
        pass #(7->7->7->7 / die nodes müssen erstellt, die parents upgedated, die leafs upgedated) -> eventuell extra methode die board.column neue nodes erstellt und auf diese wieder die simulation anwendet mit depth - 1 und du musst schauen wer überhaupt dran ist damit du sagen kannst aus welcher perspektive welcher move am besten ist (beziehungsweiße mit dem negativ ding  rechnest um nichts an der logik ändern zu müssen)
    pass


