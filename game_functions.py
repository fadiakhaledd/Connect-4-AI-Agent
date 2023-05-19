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


def score_mechanism(window, piece):
    score = 0

    # Determine the piece of the opponent
    opponent = OPP_PIECE
    if piece == OPP_PIECE:
        opponent = AGENT_PIECE

    # Count the number of occurrences of the current player's piece and empty spaces
    piece_count = window.count(piece)  # count occurrence
    empty_count = window.count(0)

    # Assign scores based on the number of occurrences of the current player's piece and empty spaces
    if piece_count == 4:
        score += 1000  # highest score we can get
    elif (piece_count == 3) and empty_count == 1:
        score += 10
    elif (piece_count == 2) and empty_count == 2:
        score += 5

    # Check for the opponent's pieces and assign a negative score if they have three in a row with an empty space
    opp_count = window.count(opponent)
    if opp_count == 3 and empty_count == 1:
        score -= 70

    return score


# assign the score to a board
def calculate_score(board, piece):
    score = 0  # initial score is zero

    # score center column
    center_array = [int(row[COLUMNS // 2])
                    for row in board]  # get the center column
    center_count = center_array.count(piece)
    score += center_count * 6

    # Score for horizontal sequences of pieces
    for row in range(ROWS):
        row_array = [int(i) for i in board[row]]
        for col in range(COLUMNS - 3):
            # Get a window of 4 pieces in the row
            window = row_array[col:col + WIN_LENGTH]
            score += score_mechanism(window, piece)

    # Score for vertical sequences of pieces
    for col in range(COLUMNS):
        col_array = [int(i) for i in [board[r][col] for r in range(ROWS)]]
        for row in range(ROWS - 3):
            # Get a window of 4 pieces in the column
            window = col_array[row:row + WIN_LENGTH]
            score += score_mechanism(window, piece)

    # Score for diagonal sequences of pieces (from bottom to top)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            # Get a diagonal window of 4 pieces
            window = [board[row + i][col + i] for i in range(WIN_LENGTH)]
            score += score_mechanism(window, piece)

    # Score for diagonal sequences of pieces (from top to bottom)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            # Get a diagonal window of 4 pieces
            window = [board[row - i][col + i] for i in range(WIN_LENGTH)]
            score += score_mechanism(window, piece)

    return score
