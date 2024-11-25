import sys
sys.path.append(r"C:\Users\amirm\Desktop\PythonProject")
sys.path.append(r"C:\Users\Amir\Desktop\PythonProject")
from game_utils import initialize_game_state
import pytest

@pytest.fixture
def board():
    return initialize_game_state()