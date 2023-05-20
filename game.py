from board import Board
import time
import math
from game_functions import *
from agent import minimax_algorithm,alpha_beta_algorithm
import numpy as np

# GAME LINK
# http://kevinshannon.com/connect4/

def play(algorithm,depth):
    board = Board()
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        reversed_board = game_board[::-1]

        if(len(get_all_valid_columns(reversed_board))==0):
            break

        if algorithm == "Minimax":
            col = minimax_algorithm(reversed_board, depth, True)[0]
        else:
            col = alpha_beta_algorithm(reversed_board, depth, -math.inf, math.inf, True)[0]

        print(col)
        print()

        board.select_column(col)
        time.sleep(2)