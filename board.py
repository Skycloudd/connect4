from colorama import Fore

from player import Player


class Board:
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        self.board = [[None for i in range(columns)] for j in range(rows)]

    def __str__(self) -> str:
        output = "-" * ((self.columns * 4) + 1) + "\n"
        for row in self.board[::-1]:
            for col in row:
                if col is None:
                    output += f"|   "
                else:
                    output += f"| {col.colour}*{Fore.RESET} "
            output += "|\n"
            output += "-" * ((self.columns * 4) + 1) + "\n"

        for i in range(1, self.columns + 1):
            output += f"  {i} "

        return output

    def insert_in_column(self, column: int, player: Player) -> bool:
        column -= 1
        for i in range(self.rows):
            if self.board[i][column] is None:
                self.board[i][column] = player
                return True
        return False

    def check_if_game_over(self) -> bool:
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] is not None:
                    try:
                        if (
                            self.board[i][j]
                            == self.board[i][j + 1]
                            == self.board[i][j + 2]
                            == self.board[i][j + 3]
                        ):
                            return True
                    except IndexError:
                        pass

                    try:
                        if (
                            self.board[i][j]
                            == self.board[i + 1][j]
                            == self.board[i + 2][j]
                            == self.board[i + 3][j]
                        ):
                            return True
                    except IndexError:
                        pass

                    try:
                        if (
                            self.board[i][j]
                            == self.board[i + 1][j + 1]
                            == self.board[i + 2][j + 2]
                            == self.board[i + 3][j + 3]
                        ):
                            return True
                    except IndexError:
                        pass

                    try:
                        if (
                            self.board[i][j]
                            == self.board[i + 1][j - 1]
                            == self.board[i + 2][j - 2]
                            == self.board[i + 3][j - 3]
                        ):
                            return True
                    except IndexError:
                        pass

        return False
