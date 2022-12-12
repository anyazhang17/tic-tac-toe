# author: Anya Zhang
# date: 10/17/22
# file: board.py implements the board of tic-tac-toe
# input: cell, sign
# output: tic-tac-toe board

class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
        self.conversion = ('A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3')

    def get_size(self): 
        # optional, return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)  
        return self.winner  

    def get_board(self):
        return self.board
         
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes 
        # this implementation is up to you 
        index = self.conversion.index(cell)
        self.board[index] = sign


    def isempty(self, cell):
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # return True if the cell is empty (not marked with X or O)
        index = self.conversion.index(cell)   
        return self.board[index] == " "


    def isdone(self):
        done = False
        # check all game terminating conditions (3 in a row or all cells filled), if one of them is present, 
        # assign the var done to True, depending on conditions assign the instance var winner to O or X
        if self.board[0] == self.board[1] == self.board[2] != " " or self.board[0] == self.board[3] == self.board[6] != " " or self.board[0] == self.board[4] == self.board[8] != " ":
            done = True
            self.winner = self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] != " " or self.board[1] == self.board[4] == self.board[7] != " " or self.board[2] == self.board[4] == self.board[6] != " ":
            done = True
            self.winner = self.board[4]
        elif self.board[6] == self.board[7] == self.board[8] != " " or self.board[2] == self.board[5] == self.board[8] != " ":
            done = True
            self.winner = self.board[8]
        # tie, all filled
        else:
            filled_cells = 0
            for cell in self.conversion:
                if not Board.isempty(self, cell):
                    filled_cells += 1
            if filled_cells == 9:
                done = True
                self.winner = ""
        return done


    def show(self):
        # draw the board
        print("\n   A   B   C  ")
        print(" +---+---+---+")
        print("1| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2]))
        print(" +---+---+---+")
        print("2| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
        print(" +---+---+---+")
        print("3| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
        print(" +---+---+---+")