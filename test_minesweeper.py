from datetime import datetime

import pytest

from main import create_board, get_neighbors, calculate_mines, display_board


def test_get_neighbors():
    """
    Surrounding mines test
    """
    size = 9
    neighbors = get_neighbors(4, 4, size)

    assert len(neighbors) == 8
    assert (3, 3) in neighbors
    assert (3, 4) in neighbors
    assert (3, 5) in neighbors
    assert (4, 3) in neighbors
    assert (4, 5) in neighbors
    assert (5, 3) in neighbors
    assert (5, 4) in neighbors
    assert (5, 5) in neighbors

def test_calculate_mines():
    """
    Mine count test
    """
    size = 9
    mines = 10
    board = create_board(size, mines)
 
    mine_count = calculate_mines(board, size)
    assert mine_count == mines

def test_create_board():
    """
    Selection of language
    """
    board = create_board(3, 3)
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)    

@pytest.fixture
def set_lang_and_time():
    global SELECTED_LANG
    SELECTED_LANG = "en"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    yield SELECTED_LANG, current_time
