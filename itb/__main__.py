from itb.board import Board
from itb.level_importer import LevelImporter
from itb.entities import PlayerType
from itb.serialise import Serialiser


def main():
    s = Serialiser()

    m = LevelImporter()
    m.load_level("itb/maps/test-04.txt")

    b = Board()
    b.import_level(m.get_tiles(), m.get_entities())
    print(b)

    players_turn = False

    print("== Enemy's turn == ")
    s.tree = b.get_available_moves_depth(PlayerType.BUG, 2)
    s.serialise()

    print(f"Current node: \n{s.tree}")


if __name__ == "__main__":
    main()
