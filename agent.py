import math
import random
from copy import deepcopy

from game_functions import *


def is_terminal(board):
    return game_end(board, OPP_PIECE) or game_end(board, AGENT_PIECE) or len(get_all_valid_columns(board)) == 0


def minimax_algorithm(board, depth, maximizing_player):
    valid_columns = get_all_valid_columns(board)

    # terminal_node possibilities: agent wins, opponent wins, out of pieces/moves
    terminal_node = is_terminal(board)

    if depth == 0 or terminal_node:
        if terminal_node:
            if game_end(board, AGENT_PIECE):
                return None, 10000000000
            elif game_end(board, OPP_PIECE):
                return None, -10000000000
            else:  # out of moves , Drawn
                return None, 0
        else:
            return None, calculate_score(board, AGENT_PIECE)

    # algorithm tries to maximize the score by selecting the move that leads to the highest score.
    if maximizing_player:
        score = -math.inf
        best_col = random.choice(valid_columns)

        for col in valid_columns:
            row = get_first_valid_row(board, col)
            board_temp = deepcopy(board)
            drop_piece(board_temp, row, col, AGENT_PIECE)

            # get the first index of the returned
            new_score = minimax_algorithm(board_temp, depth - 1, False)[1]

            if new_score > score:
                score = new_score
                best_col = col

        return best_col, score

    else:

        # minimizing player turn , the algorithm tries to minimize the score by
        # selecting the move that leads to the lowest score.
        score = math.inf
        col = random.choice(valid_columns)

        for col in valid_columns:
            row = get_first_valid_row(board, col)
            board_temp = deepcopy(board)
            drop_piece(board_temp, row, col, OPP_PIECE)
            new_score = minimax_algorithm(board_temp, depth - 1, True)[1]
            if new_score < score:
                score = new_score
                col = col
        return col, score
