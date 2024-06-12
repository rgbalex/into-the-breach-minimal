from itb.board import Board
from itb.level_importer import LevelImporter
from itb.entities import PlayerType


def main():
    m = LevelImporter()
    m.load_level("itb/maps/test-03.txt")

    b = Board()
    b.import_level(m.get_tiles(), m.get_entities())
    print(b)

    players_turn = False

    # while True:
    print("Enemy's turn: (all moves to depth 1)")
    x = b.get_available_moves_depth(PlayerType.BUG, 1)
    for move in x:
        print(move)



if __name__ == "__main__":
    main()
