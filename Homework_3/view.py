def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def get_player_move():
    while True:
        move = input("Введите свой ход (0-8): ")
        try:
            move = int(move)
            if move >= 0 and move <= 8:
                return move
            else:
                print("Ошибка!. Пожалуйста, введите число от 0 до 8.")
        except ValueError:
            print("Ошибка!. Пожалуйста, введите число от 0 до 8.")

def print_winner(player):
    print("Игрок " + "[" + player.get_letter() + "] выиграл игру!")

def print_tie():
    print("Игра окончена в ничью!")
