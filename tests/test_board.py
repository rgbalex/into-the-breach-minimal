import unittest
import numpy as np
from itb.board import Board
from itb.tiles import BaseTile

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.map_data = [[1, 2, 3], [3, 2, 1], [0, 0, 0]]

    def test_import_map(self):
        self.board.import_map(self.map_data)
        expected_board = np.array([[BaseTile(1), BaseTile(2), BaseTile(3)],
                                   [BaseTile(3), BaseTile(2), BaseTile(1)],
                                   [BaseTile(0), BaseTile(0), BaseTile(0)]])
        
        # Check if the shapes of the two arrays are equal
        self.assertEqual(self.board._board.shape, expected_board.shape)

        # Check if the types of the elements in the two arrays are equal
        for i in range(self.board._board.shape[0]):
            for j in range(self.board._board.shape[1]):
                self.assertIsInstance(self.board._board[i, j], type(expected_board[i, j]))

    def test_get_tile(self):
        self.board.import_map(self.map_data)
        tile = self.board.get_tile(1, 1)
        self.assertIsInstance(tile, BaseTile)

    # this actually tests nothing?
    def test_set_tile(self):
        self.board.import_map(self.map_data)
        tile = BaseTile()
        self.board.set_tile(0, 0, tile)
        self.assertEqual(self.board._board[0, 0], tile)

if __name__ == '__main__':
    unittest.main()
    