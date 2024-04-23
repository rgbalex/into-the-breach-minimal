import unittest
import numpy as np
from itb.board import Board
from itb.tiles import BaseTile


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.map_data = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    def test_import_map(self):
        self.board.import_level(self.map_data, [])
        expected_tiles = np.array(self.map_data)

        # Check if the shapes of the two arrays are equal
        self.assertEqual(self.board._tiles.shape, expected_tiles.shape)

        # Check if the types of the elements in the two arrays are equal
        for i in range(self.board._tiles.shape[0]):
            for j in range(self.board._tiles.shape[1]):
                self.assertIsInstance(
                    self.board._tiles[i, j], type(expected_tiles[i, j])
                )

    def test_get_tile(self):
        self.board.import_level(self.map_data, [])
        tile = self.board.get_tile(1, 1)
        # self.assertIsInstance(tile.__class__, int)
        self.assertIsInstance(tile, np.int32)

    # this actually tests nothing?
    def test_set_tile(self):
        self.board.import_level(self.map_data, [])
        self.board.set_tile(0, 0, 1)
        self.assertEqual(self.board._tiles[0, 0], 1)

    def test_get_single_enemy_entity_moves(self):
        self.board.import_level(self.map_data, [(4, 0, 0, 0)])
        moves = list(self.board.get_available_moves(mode="enemy"))
        self.assertEqual(
            moves, [[(4, 0, 0, 1)], [(4, 0, 1, 0)], [(4, 0, 0, 2)], [(4, 0, 2, 0)]]
        )

    def test_get_multiple_enemy_entity_moves(self):
        self.board.import_level(self.map_data, [(4, 0, 0, 0), (4, 0, 2, 2)])
        moves = list(self.board.get_available_moves(mode="enemy"))
        self.assertEqual(
            moves,
            # never diagonal move
            [
                [(4, 0, 2, 2), (4, 0, 0, 1)],
                [(4, 0, 2, 2), (4, 0, 1, 0)],
                [(4, 0, 2, 2), (4, 0, 0, 2)],
                [(4, 0, 2, 2), (4, 0, 2, 0)],
                [(4, 0, 0, 0), (4, 0, 2, 1)],
                [(4, 0, 0, 0), (4, 0, 1, 2)],
                [(4, 0, 0, 0), (4, 0, 2, 0)],
                [(4, 0, 0, 0), (4, 0, 0, 2)],
            ],
        )

    def test_get_multiple_enemy_with_friendly_entity_moves(self):
        self.board.import_level(
            self.map_data, [(1, 0, 2, 0), (4, 0, 0, 0), (4, 0, 2, 2)]
        )
        moves = list(self.board.get_available_moves(mode="enemy"))
        self.assertEqual(
            moves,
            # never diagonal move
            [
                [(1, 0, 2, 0), (4, 0, 2, 2), (4, 0, 0, 1)],
                [(1, 0, 2, 0), (4, 0, 2, 2), (4, 0, 1, 0)],
                [(1, 0, 2, 0), (4, 0, 2, 2), (4, 0, 0, 2)],
                [(1, 0, 2, 0), (4, 0, 2, 2), (4, 0, 2, 0)],
                [(4, 0, 0, 0), (1, 0, 2, 0), (4, 0, 2, 1)],
                [(4, 0, 0, 0), (1, 0, 2, 0), (4, 0, 1, 2)],
                [(4, 0, 0, 0), (1, 0, 2, 0), (4, 0, 2, 0)],
                [(4, 0, 0, 0), (1, 0, 2, 0), (4, 0, 0, 2)],
            ],
        )


if __name__ == "__main__":
    unittest.main()
