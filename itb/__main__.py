from itb.board import Board
from itb.entities import PlayerType
from itb.serialise import Serialiser
from itb.minimax_result import MinimaxResult
from itb.level_importer import LevelImporter
from itb.gui.isometric_grid import IsometricGrid


class Main:

    SCREEN_WIDTH = 1027 // 2 * 3
    SCREEN_HEIGHT = 1000 // 4 * 5
    level_to_load = "itb/maps/test-04.txt"

    verbose = False
    serialise = True
    dump_output_txt = False

    board = Board(level_to_load)
    grid = IsometricGrid(SCREEN_WIDTH, SCREEN_HEIGHT, board)
    serialiser = Serialiser()
    level_importer = LevelImporter()

    def print(s, *args):
        if s.verbose:
            print(*args)

    def run(s):
        # s.grid.run()

        s.print(s.board)

        s.print("== Enemy's turn == ")
        s.board.get_available_moves_depth(PlayerType.BUG, 3)
        s.serialiser.tree = s.board.get_root()

        if s.serialise:
            s.print("Serialising tree...")
            s.serialiser.serialise()
            s.print("Output to output.json\n")

        if s.dump_output_txt:
            print("Dumping output...\n")
            with open("output.txt", "w") as log:
                log.write(f"Current node: \n{s.serialiser.tree}")
            print("Output to output.txt\n")

        s.board.summary()

        val: MinimaxResult = s.board.minimax(
            s.board.get_root(), s.board.get_root()._player
        )

        s.print(f"\nMinimax value: {val}")

        print("\n")
        print(s.board)
        print("Selected Move Tree:")
        n = val.node

        # Collect the nodes in the path from the root to the selected node
        out = {}
        max_depth = s.board.get_root().get_depth()
        out[0] = (
            f"leaf {max_depth - n._depth} {n._player} {n._state._entities} {n._score}"
        )
        while n != None:
            n = n.get_parent()
            if n != None:
                out[n._depth] = (
                    f"{max_depth - n._depth} {n._player} {n._state._entities} {n._score}"
                )

        # Print the nodes in the path from the root to the selected node
        for i in range(len(out) - 1, -1, -1):
            print(out[i])


if __name__ == "__main__":
    m = Main()
    m.run()
