# author: Anya Zhang
# date: 10/17/22
# file: player.py implements the Players of the tic-tac-toe game, 
# including the user, random AI, and MiniMax AI
# input: name, sign, board
# output: updates the board based on moves chosen by the specified Player

import random
from random import choice
from board import Board

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        valid_letters = ['A', 'B', 'C']
        valid_numbers = ['1', '2', '3']
        while True:
            cell = input("\n{}, {}: Enter a cell [A-C][1-3]: \n".format(self.name, self.sign))
            # valid input and cell empty
            if len(cell) == 2 and cell[0] in valid_letters and cell[1] in valid_numbers and board.isempty(cell):
                board.set(cell, self.sign)
                break
            print("You did not choose correctly.")
            

# AI is subclass of Player
class AI(Player):

    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board
        self.cells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

    def choose(self, board):
        while True:
            rand_cell = random.choice(self.cells)
            if board.isempty(rand_cell):
                board.set(rand_cell, self.sign)
                self.cells.remove(rand_cell)
                return


class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        if self.sign == 'O':
            self.opponent_sign = 'X'
        else:
            self.opponent_sign = 'O'

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        #cell = MiniMax.minimax(self, board, 0, True)
        cell = MiniMax.minimax(self, board, True, True)
        board.set(cell, self.sign)
    
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # self is a loser (opponent is a winner)
            elif board.get_winner() == self.opponent_sign:
                return -1
            # tie
            else:
                return 0
                
        min_score = float('inf')
        max_score = float('-inf')
        # Choose a cell (or make a move)
        for i in range(9):
            cell = self.cells[i]
            # empty cell
            if board.isempty(cell):
                if self_player: 
                    board.set(cell, self.sign)
                    score = MiniMax.minimax(self, board, False, False)
                    # unmark the cell
                    board.set(cell, " ")
                    if score > max_score:
                        max_score = score
                        move = self.cells[i]
                        #print(i, move)
                        
                else:
                    board.set(cell, self.opponent_sign)
                    #print(i)
                    score = MiniMax.minimax(self, board, True, False)
                    # unmark the cell
                    board.set(cell, " ")
                    if score < min_score:
                        min_score = score
                        move = self.cells[i]
                        #print(i, move)
        if start:
            return move
        elif self_player:
            return max_score
        else: 
            return min_score