import numpy as np
from itb.board import Board
from itb.level_importer import LevelImporter


def main():
    m = LevelImporter()
    m.load_level("itb/maps/test-02.txt")

    b = Board()
    b.import_level(m.get_tiles(), m.get_entities())
    print(b)


if __name__ == "__main__":
    main()
