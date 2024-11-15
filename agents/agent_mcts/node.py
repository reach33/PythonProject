import numpy as np
import math
from __future__ import annotations

class Node():

    current_root: Node
    max_height: int
    leafs: list

    def __init__(self,parent: Node,children: list[Node],height,chosen_column,win_simulations,total_simulations,board: np.ndarray,value):
        self.parent = parent
        self.children = children
        self.height = height
        self.chosen_column = chosen_column
        self.win_simulations = win_simulations
        self.total_simulations = total_simulations
        self.board = board
        self.value = value

    def set_value(self):
        self.value = (self.win_simulations/self.total_simulations)+(math.sqrt(2)*math.sqrt(math.log(self.parent.total_simulations)/self.total_simulations))