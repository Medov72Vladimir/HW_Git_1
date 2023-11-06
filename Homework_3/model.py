class Board:
    def __init__(self):
        self.board = [' ' for x in range(9)]

    def insert_letter(self, letter, pos):
        self.board[pos] = letter

    def space_is_free(self, pos):
        return self.board[pos] == ' '

    def is_winner(self, le):
        return ((self.board[0] == le and self.board[1] == le and self.board[2] == le) or
                (self.board[3] == le and self.board[4] == le and self.board[5] == le) or
                (self.board[6] == le and self.board[7] == le and self.board[8] == le) or
                (self.board[0] == le and self.board[3] == le and self.board[6] == le) or
                (self.board[1] == le and self.board[4] == le and self.board[7] == le) or
                (self.board[2] == le and self.board[5] == le and self.board[8] == le) or
                (self.board[0] == le and self.board[4] == le and self.board[8] == le) or
                (self.board[2] == le and self.board[4] == le and self.board[6] == le))

    def is_board_full(self):
        return ' ' not in self.board

    def get_board(self):
        return self.board

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter