from project import (
    validate_input,
    possible,
    correct,
    solved,
    find_next_empty
)

# -------------------------
# Tests for validate_input()
# -------------------------
def test_validate_input_coords_valid():
    assert validate_input("1", "coord") == True
    assert validate_input("9", "coord") == True

def test_validate_input_coords_invalid():
    assert validate_input("0", "coord") == False
    assert validate_input("10", "coord") == False
    assert validate_input("-3", "coord") == False
    assert validate_input("abc", "coord") == False

def test_validate_input_value_valid():
    assert validate_input("5", "value") == True
    assert validate_input("9", "value") == True

def test_validate_input_value_invalid():
    assert validate_input("0", "value") == False
    assert validate_input("15", "value") == False

def test_validate_input_invalid_type():
    assert validate_input("5", "unknown") == False


# ---------------------
# Tests for possible()
# ---------------------
def test_possible_valid_move():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert possible(0, 2, 4, board) == True

def test_possible_invalid_row():
    board = [[1]*9 for _ in range(9)]
    assert possible(0, 0, 1, board) == False

def test_possible_invalid_column():
    board = [[0]*9 for _ in range(9)]
    for i in range(9):
        board[i][0] = 2
    assert possible(5, 0, 2, board) == False

def test_possible_invalid_box():
    board = [[0]*9 for _ in range(9)]
    board[1][1] = 3
    assert possible(2, 2, 3, board) == False


# ---------------------
# Tests for correct()
# ---------------------
def test_correct_true():
    complete = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9],
    ]
    assert correct(complete) == True

def test_correct_false_duplicate_row():
    grid = [
        [5,5,4,6,7,8,9,1,2],  # duplicate 5
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9],
    ]
    assert correct(grid) == False

def test_correct_false_duplicate_col():
    grid = [
        [5,3,4,6,7,8,9,1,2],
        [5,7,2,1,9,5,3,4,8],  # duplicate 5 in column 0
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9],
    ]
    assert correct(grid) == False

def test_correct_false_duplicate_box():
    grid = [
        [5,3,4,6,7,8,9,1,2],
        [6,5,2,1,9,5,3,4,8],  # duplicate 5 in top-left 3x3 box
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9],
    ]
    assert correct(grid) == False


# ---------------------
# Tests for solved()
# ---------------------
def test_solved_true():
    grid = [[1]*9 for _ in range(9)]  # no zeros
    assert solved(grid) == True

def test_solved_false():
    grid = [[1]*9 for _ in range(9)]
    grid[4][4] = 0
    assert solved(grid) == False


# ---------------------
# Test for find_next_empty()
# ---------------------
def test_find_next_empty_found():
    grid = [[1]*9 for _ in range(9)]
    grid[0][3] = 0
    assert find_next_empty(grid) == (0, 3)

def test_find_next_empty_none():
    grid = [[1]*9 for _ in range(9)]
    assert find_next_empty(grid) == (None, None)