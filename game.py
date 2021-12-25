from itertools import cycle

from colorama import Fore

from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board(7, 6)
        self.players = [
            Player(1, "Player 1", Fore.RED),
            Player(2, "Player 2", Fore.YELLOW),
        ]

    def get_move(self):
        while True:
            num = input("Enter a column number (1-7): ")
            if num.isdigit():
                num = int(num)
                if num > 0 and num < 8:
                    return num

    def play(self):
        print("\033c")

        players_text = ""
        for player in self.players:
            players_text += f"{player.colour}{player.name}{Fore.RESET} "

        print(f"{players_text}")

        print(self.board)

        for player in cycle(self.players):
            while True:
                move = self.get_move()
                result = self.board.insert_in_column(move, player)
                if result:
                    break
            print("\033c")

            players_text = ""
            for player in self.players:
                players_text += f"{player.colour}{player.name}{Fore.RESET} "

            print(players_text)

            print(self.board)

            check_if_game_over = self.board.check_if_game_over()
            if check_if_game_over:
                print(f"Game over! {player.name} wins!")
                break
