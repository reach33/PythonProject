from __future__ import annotations
from typing import Optional
from game_utils import check_end_state, BoardPiece, GameState
import numpy as np
import math

class Node():

    current_root: Node = None
    player: BoardPiece = None

    def __init__(self,parent: Node,chosen_column,board: np.ndarray):
        self.parent = parent
        self.chosen_column = chosen_column
        self.board = board
        self.children: list[Node] = []
        self.win_simulations = 0
        self.total_simulations = 0
        self.value = 0
        if self.parent != None:
            self.parent.children.append(self)
            self.update_ancestors(check_end_state(self.player) == GameState.IS_WIN)
        

    def set_value(self):
        #Calculate and set the value for the node using UCT (Upper Confidence Bound).
        if self.total_simulations == 0 or self.parent == None:
            self.value = 0
            return
        self.value = (self.win_simulations/self.total_simulations)+(math.sqrt(2)*math.sqrt(math.log(self.parent.total_simulations)/self.total_simulations))

    @classmethod
    def update_root_by_board(cls, board: np.ndarray):
        if not cls.current_root == None:
            for child in cls.current_root.children:
                if np.array_equal(child.board, board):
                    cls.current_root = child
                    return
            
        #If it is the first move and root is empty
        cls.current_root = Node(None,0,board)
        
    @classmethod
    def get_leaf_by_best_value(cls) -> Node:
        return cls.current_root.choose_next_node_by_value()
        
    
    def choose_next_node_by_value(self) -> Node:
        max_value = 0
        max_child = self # for first and last run
        for child in self.children:
            if child.value >= max_value:
                max_child = child
                max_value = child.value
        if max_child.children:
            return max_child.choose_next_node_by_value()
        return max_child

    def update_ancestors(self,win: Optional[bool] = False):
        #simulations, wins, and value update
        if win:
            self.parent.total_simulations += 1
            self.parent.win_simulations += 1
            self.set_value()
            self.parent.update_ancestors(True)
            return
        
        self.parent.total_simulations += 1
        self.set_value()
        self.parent.update_ancestors()

    @classmethod
    def set_player(cls, player: BoardPiece):
        cls.player = player