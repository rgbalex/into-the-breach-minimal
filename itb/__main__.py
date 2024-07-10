import sys, os

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
    b.get_available_moves_depth(PlayerType.BUG, 1)
    s.tree = b.get_root()

    print("Serialising...")
    s.serialise()
    print("Output to output.json\n")

    if "verbose" in os.environ:
        if os.environ["verbose"] == "true":
            print("Dumping output...\n")
            with open("output.txt", "w") as log:
                log.write(f"Current node: \n{s.tree}")
            print("Output to output.txt\n")

    b.summary()

    val = b.minimax(b.get_root(), 2, PlayerType.BUG)
    print(f"Minimax value: {val}")


if __name__ == "__main__":
    main()
