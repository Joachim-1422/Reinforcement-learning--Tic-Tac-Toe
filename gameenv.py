#!/usr/bin/env python3

from copy import deepcopy

class TicTacToeEnv(object):

    def __init__(self, board):
        # @board is the boardgame for Tic Tac Toe
        super(TicTacToeEnv, self).__init__()
        self.original_board = deepcopy(board)
        self.board = deepcopy(board)
        self.original_a_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.a_list = deepcopy(self.original_a_list)

    def is_finished(self, state):
        # Check if the game is over @return Boolean
        end = [[0, 0, 0, 1, 0, 2], [1, 0, 1, 1, 1, 2], [2, 0, 2, 1, 2, 2], [0, 0, 1, 0, 2, 0], [0, 1, 1, 1, 2, 1], [0, 2, 1, 2, 2, 2], [0, 0, 1, 1, 2, 2], [0, 2, 1, 1, 2, 0]]
        for p in range(1, 3):
            i = 0
            while i < len(end):
                t = 0
                j = 0
                while j < 6:
                    if state[end[i][j]][end[i][j + 1]] == p:
                        t += 1
                    if t == 3:
                        return 3
                    j += 2
                i += 1
        if not self.a_list:
            return 2
        else:
            return 1

    def reset(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#        self.board = self.original_board
#        self.a_list = self.original_a_list
        self.a_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        return self.board

    def display(self):
        print("%d|%d|%d" % (self.board[0][0], self.board[0][1], self.board[0][2]))
        print('-----')
        print("%d|%d|%d" % (self.board[1][0], self.board[1][1], self.board[1][2]))
        print('-----')
        print("%d|%d|%d" % (self.board[2][0], self.board[2][1], self.board[2][2]))

    def step(self, action, p):
        self.board[action[0]][action[1]] = p
        if self.is_finished(self.board) == 2:
            return deepcopy(self.board), 0.5
        elif self.is_finished(self.board) == 3:
            return deepcopy(self.board), 1
        else:
            return deepcopy(self.board), 0