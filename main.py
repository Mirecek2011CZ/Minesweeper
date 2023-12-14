import random
from datetime import datetime
from language import TEXT
from language import SELECTED_LANG

def get_lang_from_user():
    """
    Selecting language
    """
    global SELECTED_LANG
    while True:
        get_lang_from_user = (input("CHOOSE LANGUAGE (cs OR en): ").lower())
        if get_lang_from_user in ["cs", "en"]:
            SELECTED_LANG = get_lang_from_user
            return

def create_board(size, mines):
    """
    Creates a game board
    """
    board = [['.' for _ in range(size)] for _ in range(size)]
    mine_positions = random.sample(range(size * size), mines)

    for i in mine_positions:
        board[i // size][i % size] = 'X'

    return board

def display_board(board):
    """
    Displays board
    """
    for row in board:
        print(" ".join([cell if cell != 'X' else '.' for cell in row]))

def get_neighbors(x_c, y_c, size):
    """
    Surrounding mines
    """
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_x, neighbor_y = x_c + i, y_c + j
            if 0<=neighbor_x<size and 0<=neighbor_y<size and (neighbor_x, neighbor_y)!=(x_c, y_c):
                neighbors.append((neighbor_x, neighbor_y))

    return neighbors

def calculate_mines(board, size):
    """
    Mine count
    """
    mine_count = 0

    for i in range(size):
        for j in range(size):
            if board[i][j] == 'X':
                mine_count += 1

    return mine_count

def get_row_from_user():
    """
    Selection of row
    """
    while True:
        try:
            selected_x_coordinates = int(input(TEXT["enter_row"][SELECTED_LANG]))
            if selected_x_coordinates >= 1 and selected_x_coordinates <= 9:
                return selected_x_coordinates
        except ValueError:
            print(TEXT["invalid_input"][SELECTED_LANG])

def get_col_from_user():
    """
    Selection of column
    """
    while True:
        try:
            selected_y_coordinates = int(input(TEXT["enter_col"][SELECTED_LANG]))
            if selected_y_coordinates >= 1 and selected_y_coordinates <= 9:
                return selected_y_coordinates
        except ValueError:
            print(TEXT["invalid_input"][SELECTED_LANG])

def reveal_square(board, x_c, y_c, size):
    """
    Reveals selected the square
    """
    if board[x_c][y_c] == 'X':
        return 'X'
    else:
        mine_count = 0
        neighbors = get_neighbors(x_c, y_c, size)
        for n_x, n_y in neighbors:
            if board[n_x][n_y] == 'X':
                mine_count += 1
        return str(mine_count)

def game_loop(board, size):
    """
    Loop
    """
    mines = calculate_mines(board, size)
    uncovered_count = 0

    while uncovered_count < (size*size - mines):
        row = get_row_from_user()
        col = get_col_from_user()

        if board[row-1][col-1] == 'X':
            print(TEXT["game_over"][SELECTED_LANG])
            return

        board[row-1][col-1] = reveal_square(board, row-1, col-1, size)
        display_board(board)
        uncovered_count += 1

    print(TEXT["founded_all_mines"][SELECTED_LANG])

def minesweeper(size = 9, mines = 8):
    """
    Minesweeper
    """
    board = create_board(size, mines)
    display_board(board)

with open('result_file.txt','w') as file:
        file.write(TEXT["game_over"][SELECTED_LANG])

if __name__ == "__main__":
    get_lang_from_user()
    print(TEXT["welcome_text"][SELECTED_LANG])
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(TEXT["time_and_date_info"][SELECTED_LANG], current_time)
    board = create_board(9, 10)
    display_board(board)
    game_loop(board, 9)
