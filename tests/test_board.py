import unittest
import numpy as np

from itb.board import Board
from itb.entities import PlayerType


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(None)
        self.map_data = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    def test_import_map(self):
        self.board.import_level(self.map_data, [])
        expected_tiles = list(self.map_data)

        # Check if the shapes of the two arrays are equal
        self.assertEqual(len(self.board._tiles), len(expected_tiles))

        # Check if the types of the elements in the two arrays are equal
        for i in range(len(self.board._tiles)):
            for j in range(len(self.board._tiles[i])):
                self.assertIsInstance(
                    self.board._tiles[j][i], type(expected_tiles[j][i])
                )

    def test_get_tile(self):
        self.board.import_level(self.map_data, [])
        tile = self.board.get_tile(1, 1)
        # self.assertIsInstance(tile.__class__, int)
        # self.assertIsInstance(tile, np.int64)
        # This test has proven unreliable and platform specific.
        # Its specifics is commented out for now.
        self.assertEqual(tile, 0)

    # this actually tests nothing?
    def test_set_tile(self):
        self.board.import_level(self.map_data, [])
        self.board.set_tile(0, 0, 1)
        self.assertEqual(self.board._tiles[0][0], 1)

    def test_put_entitiy_on_invalid_tile(self):
        with self.assertRaises(ValueError):
            self.board.import_level(self.map_data, [(1, 0, 1, 1)])


if __name__ == "__main__":
    unittest.main()
