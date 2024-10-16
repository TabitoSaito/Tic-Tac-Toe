from gamebrain import Brain
from player import Players, Player
from interface import Interface


def main():
    test = True
    while test:
        players = Players()
        game = Brain()
        while not game.check_game_end():
            Interface(game.board)
            cur_player: Player = players.next_player()
            print(f"{cur_player.sym} Players turn.")
            cell_input: str = game.input_coordinate()
            game.update_board(cur_player, cell_input)
        Interface(game.board)
        if cur_player.has_won:
            print(f"\n{cur_player.sym} Player won!")
        else:
            print("It's a draw.")
        t = input("\nDo you want to play again? (y/n)\n")
        if t == "n":
            test = False


if __name__ == "__main__":
    main()
