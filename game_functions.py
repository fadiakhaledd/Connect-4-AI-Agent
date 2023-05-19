# Define game variables
ROWS = 6
COLUMNS = 7
WIN_LENGTH = 4

AGENT_PIECE = 1
OPP_PIECE = 2


# Drop piece in specified index
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# Check if a column is valid to drop pieces into
def is_valid_column(board, col):
    return board[ROWS - 1][col] == 0


# Find first open row in a specified column
def get_first_valid_row(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row


def game_end(board, piece):
    # Check if there are any horizontal winning positions
    for col in range(COLUMNS - 3):  # No need to check last 3 columns
        for row in range(ROWS):
            # Check if there are 4 consecutive pieces in any row
            if (board[row][col] == piece and
                    board[row][col + 1] == piece and
                    board[row][col + 2] == piece and
                    board[row][col + 3] == piece):
                return True

    # Check if there are any vertical winning positions
    for row in range(ROWS - 3):  # no need to check last 3 rows
        for col in range(COLUMNS):
            # check if there is 4 consecutive piece in any column
            if (board[row][col] == piece and
                    board[row + 1][col] == piece and
                    board[row + 2][col] == piece and
                    board[row + 3][col] == piece):
                return True

    # Check if there are any diagonal winning positions (from bottom to top)
    for col in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if (board[row][col] == piece and
                    board[row + 1][col + 1] == piece and
                    board[row + 2][col + 2] == piece and
                    board[row + 3][col + 3] == piece):
                return True

    # Check if there are any diagonal winning positions (from top to down)
    for col in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if (board[row][col] == piece and
                    board[row - 1][col + 1] == piece and
                    board[row - 2][col + 2] == piece and
                    board[row - 3][col + 3] == piece):
                return True
