from Homework_3.GameController import GameController

def main():
    while True:
        controller = GameController()
        controller.play_game()
        answer = input("Желаете сыграть еще раз?? (y/n): ")
        if answer.lower() != 'y':
            break

if __name__ == '__main__':
    main()