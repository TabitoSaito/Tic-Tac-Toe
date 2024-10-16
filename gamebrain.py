import pandas as pd
import numpy as np
from player import Player


def gen_empty_field() -> pd.DataFrame:
    empty_array: np.ndarray = np.empty((3, 3), dtype=str)
    board: pd.DataFrame = pd.DataFrame(data=empty_array, columns=[1, 2, 3], index=["A", "B", "C"])
    return board


class Brain:

    def __init__(self) -> None:
        self.board: pd.DataFrame = gen_empty_field()
        self.cur_player = Player(sym=None)

    def update_board(self, player: Player, cell: str):
        self.cur_player = player
        sym: str = self.cur_player.sym
        self.board.loc[cell[0], int(cell[1])] = sym

    def check_game_end(self) -> bool:
        if "" not in self.board.values:
            return True
        else:
            return self.check_win()

    def check_win(self) -> bool:
        if self.check_diagonals() or self.check_row_col():
            self.cur_player.has_won = True
        return self.check_diagonals() or self.check_row_col()

    def check_row_col(self) -> bool:
        row_count: pd.Series = self.board[self.board == self.cur_player.sym].count(axis=1)
        col_count: pd.Series = self.board[self.board == self.cur_player.sym].count()

        if 3 in row_count.values:
            return True
        elif 3 in col_count.values:
            return True
        else:
            return False

    def check_diagonals(self) -> bool:
        right_top: str = self.board[1]["C"]
        right_bot: str = self.board[3]["C"]
        left_top: str = self.board[1]["A"]
        left_bot: str = self.board[3]["A"]
        middle: str = self.board[2]["B"]

        diagonal_left_right: list[str] = [left_top, middle, right_bot]
        diagonal_right_left: list[str] = [right_top, middle, left_bot]

        if diagonal_left_right.count(self.cur_player.sym) == 3:
            return True
        elif diagonal_right_left.count(self.cur_player.sym) == 3:
            return True
        else:
            return False

    def input_coordinate(self) -> str:
        no_valid_input: bool = True
        while no_valid_input:
            cor: str = input("Type a coordinate (e.g A1).\n").upper()
            try:
                if not self.board[int(cor[1])][cor[0]] == "":
                    print("Already filled.")
                else:
                    return cor
            except KeyError:
                print("Not a valid coordinate.")
            except IndexError:
                print("Not a valid coordinate.")
            except ValueError:
                try:
                    if not self.board[int(cor[0])][cor[1]] == "":
                        print("Already filled.")
                    else:
                        return cor[::-1]
                except KeyError:
                    print("Not a valid coordinate.")
                except IndexError:
                    print("Not a valid coordinate.")