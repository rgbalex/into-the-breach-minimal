import unittest
import numpy as np

from itb.board import Board
from itb.entities import PlayerType


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.board.import_level(
            self.map_data, [(1, 0, 2, 0), (4, 0, 0, 0), (4, 0, 2, 2)]
        )


if __name__ == "__main__":
    unittest.main()
