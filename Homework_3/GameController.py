from model import Board, Player
from view import print_board, get_player_move, print_winner, print_tie

class GameController:
    def __init__(self):
        self.board = Board()
        self.players = [Player('X'), Player('O')]
        self.current_player = self.players[0]

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def play_game(self):
        print("Добро пожаловать в игру крестики-нолики!")
        print_board(self.board.get_board())

        while not self.board.is_board_full():
            move = get_player_move()
            if self.board.space_is_free(move):
                self.board.insert_letter(self.current_player.get_letter(), move)
                print_board(self.board.get_board())
                if self.board.is_winner(self.current_player.get_letter()):
                    print_winner(self.current_player)
                    return
                self.switch_player()
            else:
                print("Это поле уже занято.")

        print_tie()