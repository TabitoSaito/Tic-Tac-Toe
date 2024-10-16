from dataclasses import dataclass


@dataclass
class Player:
    sym: str
    has_won: bool = False


class Players:

    def __init__(self, sym1: str = "x", sym2: str = "o"):
        self.player1 = Player(sym=sym1)
        self.player2 = Player(sym=sym2)
        self.players = iter([self.player1, self.player2])

    def next_player(self):
        try:
            return next(self.players)
        except StopIteration:
            self.players = iter([self.player1, self.player2])
            return next(self.players)

