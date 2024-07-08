import sys

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

    print("== Enemy's turn == ")
    s.tree = b.get_available_moves_depth(PlayerType.BUG, 3)
    s.serialise()

    # filehandle for print output
    # quick and dirty
    save_stdout = sys.stdout
    sys.stdout = open("output.txt", "w")
    print(f"Current node: \n{s.tree}")
    sys.stdout.close()
    sys.stdout = save_stdout
    print("Output to output.txt")


if __name__ == "__main__":
    main()
