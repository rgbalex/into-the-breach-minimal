import sys, os, numpy as np

from itb.board import Board, MinimaxResult
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
    b.get_available_moves_depth(PlayerType.BUG, 2)
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

    val: MinimaxResult = None
    i: int = 0
    while i < 1000:
        try:
            val = b.minimax(b.get_root(), PlayerType.BUG, 1)
            # assert val.node._depth == 0
        except AssertionError:
            print(f"Assertion error at depth {i}")
            print(f"Node depth: {val.node._depth}")
            print(f"Node: {val.node}")
            break
        except RecursionError:
            print(f"Recursion error at depth {i}")
        except Exception as e:
            print(f"Error at depth {i}: {e}")
            break
        i += 1

    print(f"\nMinimax value: {val}")


if __name__ == "__main__":
    main()
