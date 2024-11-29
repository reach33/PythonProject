from __future__ import annotations
from typing import Optional
from game_utils import check_end_state, BoardPiece, GameState, BOARD_COLS, apply_player_action, PLAYER1, PLAYER2, check_move_status, PlayerAction, MoveStatus
import numpy as np
import math
import random

class Node:
    """A class representing a node in the Monte Carlo Tree Search for Connect Four.

    Attributes:
        current_root (Node): The current root of the search tree.
        player (BoardPiece): The player whose move is being evaluated.
        parent (Node): The parent node of this node.
        chosen_column (int): The column chosen to reach this node.
        board (np.ndarray): The board state at this node.
        children (list[Node]): List of child nodes.
        win_simulations (int): Number of winning simulations from this node.
        total_simulations (int): Total number of simulations from this node.
        value (float): The value of the node based on simulations.
        weight (int): The weight of the node used for choosing moves.
        move_made_by (BoardPiece): The player who made the move to reach this node.
    """

    current_root: Node = None
    player: BoardPiece = None

    def __init__(self, parent: Node, chosen_column: int, board: np.ndarray):
        """Initializes a new node.

        Args:
            parent (Node): The parent node.
            chosen_column (int): The column chosen to reach this node.
            board (np.ndarray): The board state at this node.
        """
        self.parent = parent
        self.chosen_column = chosen_column
        self.board = board
        self.children: list[Node] = []
        self.win_simulations = 0
        self.total_simulations = 0
        self.value = 0
        self.weight = 0

        if self.parent is not None:
            self.move_made_by = PLAYER1 if self.parent.move_made_by == PLAYER2 else PLAYER2
            self.parent.children.append(self)
            apply_player_action(self.board, self.chosen_column, self.move_made_by)
            self.update_ancestors(check_end_state(self.board, self.player) == GameState.IS_WIN)
        else:
            self.move_made_by = PLAYER1 if self.player == PLAYER2 else PLAYER2

    def set_value(self):
        """Calculates and sets the value for the node using the Upper Confidence Bound (UCB) formula."""
        if self.total_simulations == 0 or check_end_state(self.board,self.player) == GameState.IS_WIN or check_end_state(self.board,PLAYER2 if self.player == PLAYER1 else PLAYER1) == GameState.IS_WIN:
            self.value = 0
            return
        self.value = (self.win_simulations / self.total_simulations) + \
                     (math.sqrt(2) * math.sqrt(math.log(self.parent.total_simulations) / self.total_simulations))

    @classmethod
    def update_root_by_board(cls, board: np.ndarray):
        """Updates the current root based on the board state.

        Args:
            board (np.ndarray): The current board state.
        """
        if cls.current_root is not None:
            for child in cls.current_root.children:
                if np.array_equal(child.board, board):
                    cls.current_root = child
                    return
        
        cls.current_root = Node(None, 0, board.copy())

    @classmethod
    def get_leaf_by_best_value(cls) -> Node:
        """Finds the leaf node with the best value.

        Returns:
            Node: The leaf node with the highest value.
        """
        return cls.current_root.choose_next_node_by_value()

    def choose_next_node_by_value(self) -> Node:
        """Selects the next node based on the highest value.

        Returns:
            Node: The node with the highest value among the children.
        """
        max_value = 0
        max_child = self
        for child in self.children:
            if child.value >= max_value:
                max_child = child
                max_value = child.value
        return max_child.choose_next_node_by_value() if max_child.children else max_child

    def update_ancestors(self, win: Optional[bool] = False):
        """Updates the ancestors of this node based on the simulation result.

        Args:
            win (Optional[bool]): Whether the simulation resulted in a win.
        """
        if win:
            if self.parent is not None:
                self.parent.total_simulations += 1
                self.parent.win_simulations += 1
                self.set_weight(True)
                self.parent.update_ancestors(True)
                self.set_value()
            return

        if self.parent is not None:
            self.parent.total_simulations += 1
            self.set_weight()
            self.parent.update_ancestors()
            self.set_value()

    @classmethod
    def set_player(cls, player: BoardPiece):
        """Sets the current player for the game.

        Args:
            player (BoardPiece): The player piece (PLAYER1 or PLAYER2).
        """
        cls.player = player

    def create_children(self, simulation_depth: int):
        """Creates child nodes by simulating moves up to a given depth.

        Args:
            simulation_depth (int): The depth of simulation for creating children.
        """
        opponent = PLAYER1 if self.player == PLAYER2 else PLAYER2
        if simulation_depth > 0:
            for i in range(BOARD_COLS):
                if check_end_state(self.board,self.player) == GameState.STILL_PLAYING  and check_end_state(self.board,opponent) == GameState.STILL_PLAYING and check_move_status(self.board, PlayerAction(i)) == MoveStatus.IS_VALID:# hier die check if ende eingetragen sollte jett keine kinder bei endgames mehr generieren
                    Node(self, i, self.board.copy()).create_children(simulation_depth - 1)

    def choose_child_as_move_by_weight(self) -> Node:
        """Selects the best move based on node weights.

        Returns:
            Node: The child node with the highest weight.
        """
        current_child = random.choice(self.children)
        for child in self.children:
            if child.weight > current_child.weight:
                current_child = child
        return current_child

    def set_weight(self, win: bool = False):
        """Calculates and sets the weight for the current node.

        Args:
            win (bool): Whether the simulation resulted in a win.
        """
        opponent = PLAYER1 if self.player == PLAYER2 else PLAYER2
        win_player = check_end_state(self.board, self.player) == GameState.IS_WIN# jedesmal checken kostet zeit besser direkt in update ancestors mitgeben als bool nicht spart zeit
        win_opponent = check_end_state(self.board, opponent) == GameState.IS_WIN

        self.weight -= 1

        if win:
            self.weight += 10000
        if win_player:
            self.weight += 3000000
        if win_opponent:
            self.weight -= 3000000

        if self.move_made_by == self.player:
            if self.weight <= -1000000:
                count_no_losses = sum(1 for child in self.parent.children if child.weight > -1000000)
                if count_no_losses < 1:
                    self.parent.weight = min(self.weight, self.parent.weight)
                    return
            self.parent.weight = max(self.weight, self.parent.weight)

        if self.move_made_by == opponent:
            self.parent.weight = min(self.weight, self.parent.weight)