from __future__ import annotations
from typing import Optional
from game_utils import check_end_state, BoardPiece, GameState, BOARD_COLS, apply_player_action, PLAYER1, PLAYER2, check_move_status, PlayerAction, MoveStatus
import numpy as np
import math
import random

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
        self.weight = 0

        if self.parent != None:
            self.move_made_by = PLAYER1 if self.parent.move_made_by == PLAYER2 else PLAYER2
            self.parent.children.append(self)
            apply_player_action(self.board,self.chosen_column,self.move_made_by)
            self.update_ancestors(check_end_state(self.board,self.player) == GameState.IS_WIN)# mit if kann hier ein check vermieden werden wenn der gegner das macht du idiot
        else:
            self.move_made_by = PLAYER1 if self.player == PLAYER2 else PLAYER2
        

    def set_value(self):
        #Calculate and set the value for the node using UCT (Upper Confidence Bound).
        if self.total_simulations == 0:
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
        cls.current_root = Node(None,0,board.copy())
        
    @classmethod
    def get_leaf_by_best_value(cls) -> Node:
        return cls.current_root.choose_next_node_by_value()
        
    
    def choose_next_node_by_value(self) -> Node:
        max_value = 0
        max_child = self # importend for first and last run
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
            if self.parent != None:
                self.parent.total_simulations += 1
                self.parent.win_simulations += 1
                self.set_weight(True)
                self.parent.update_ancestors(True)
                self.set_value()
            return
        
        if self.parent != None:
            self.parent.total_simulations += 1
            self.set_weight()
            self.parent.update_ancestors()
            self.set_value()

    @classmethod
    def set_player(cls, player: BoardPiece):
        cls.player = player
    
    def create_children(self, simulation_depth: int):
        if simulation_depth > 0:
            for i in range (BOARD_COLS):
                if check_move_status(self.board,PlayerAction(i)) == MoveStatus.IS_VALID:
                    Node(self,i,self.board.copy()).create_children(simulation_depth - 1)

    def choose_child_as_move_by_weight(self) -> Node:
        if self.children:
            current_child = self.children[random.randint(0,len(self.children)-1)]
            for child in self.children:
                if child.weight > current_child.weight:
                    current_child = child
            return current_child
        return self



    def set_weight(self,win: bool = False):

        self.weight -= 1
        if win:
            self.weight += 100

        if not self.children:
            if check_end_state(self.board,self.player) == GameState.IS_WIN:
                self.weight = 1000000
            opponent = PLAYER1 if self.player == PLAYER2 else PLAYER2
            if check_end_state(self.board,opponent) == GameState.IS_WIN:
                self.weight = -1000000
        
        if self.move_made_by == self.player:
            if self.weight <= -1000000:
                count_losses = 1
                for child in self.parent.children:
                    if child.weight <= -1000000:
                        count_losses += 1
                if count_losses > 1:
                    self.parent.weight = min(self.weight, self.parent.weight)
                    return
            self.parent.weight = max(self.weight, self.parent.weight)
        else:
            self.parent.weight = min(self.weight, self.parent.weight)


"""
leaf = -1000000, move by player 1
davor = -1000000, move by player 2
davor = -9, move by player1




"""

