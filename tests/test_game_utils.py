import sys
sys.path.append(r"C:\Users\amirm\Desktop\PythonProject")
sys.path.append(r"C:\Users\Amir\Desktop\PythonProject")
import numpy as np

from game_utils import BOARD_SHAPE, BoardPiece, NO_PLAYER

def test_initialize_game_state():
    ndarray = np.ndarray(BOARD_SHAPE, BoardPiece ,NO_PLAYER)
    print(ndarray)