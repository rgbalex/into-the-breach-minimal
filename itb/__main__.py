from itb.minimax_result import MinimaxResult
from itb.board import Board
from itb.level_importer import LevelImporter
from itb.entities import PlayerType
from itb.serialise import Serialiser
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
        s.print(s.board)
        s.grid.run()

        s.print("== Enemy's turn == ")
        s.board.get_available_moves_depth(PlayerType.BUG, 2)
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

        val: MinimaxResult = s.board.minimax(s.board.get_root(), PlayerType.BUG)
        s.print(f"\nMinimax value: {val}")


if __name__ == "__main__":
    m = Main()
    m.run()
