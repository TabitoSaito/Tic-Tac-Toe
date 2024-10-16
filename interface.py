import pandas as pd


class Interface:

    def __init__(self, board: pd.DataFrame):
        self.board: pd.DataFrame = board
        self.pretty_board()

    def pretty_board(self) -> str:
        values: list = []
        for row in range(3):
            for col in range(3):
                v = self.board.iloc[row, col]
                if v == "":
                    values.append(" ")
                else:
                    values.append(v)

        pretty = (f"\n   1   2   3\n"
                  f"A  {values[0]} | {values[1]} | {values[2]}\n"
                  f"  -----------\n"
                  f"B  {values[3]} | {values[4]} | {values[5]}\n"
                  f"  -----------\n"
                  f"C  {values[6]} | {values[7]} | {values[8]}")
        print(pretty)
        return pretty
