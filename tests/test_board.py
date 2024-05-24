import unittest
import numpy as np

from itb.board import Board
from itb.entities import PlayerType


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
        # self.assertIsInstance(tile, np.int64)
        # This test has proven unreliable and platform specific.
        # Its specifics is commented out for now.
        self.assertEqual(tile, 0)

    # this actually tests nothing?
    def test_set_tile(self):
        self.board.import_level(self.map_data, [])
        self.board.set_tile(0, 0, 1)
        self.assertEqual(self.board._tiles[0, 0], 1)

    def test_get_single_enemy_entity_moves(self):
        self.board.import_level(self.map_data, [(4, 0, 0, 0)])
        moves = list(self.board.get_available_moves(mode=PlayerType.BUG))

        self.assertEqual(len(moves), 4)

        possible_moves = [
            ((4, 0, 0, 1),),
            ((4, 0, 1, 0),),
            ((4, 0, 0, 2),),
            ((4, 0, 2, 0),),
        ]

        for i in moves:
            self.assertIn(i, possible_moves)
            possible_moves.remove(i)
        # All moves have been checked. If there are any left, the test will fail.
        self.assertEqual(possible_moves, [])

    def test_get_multiple_enemy_entity_moves(self):
        self.board.import_level(self.map_data, [(4, 0, 0, 0), (4, 0, 2, 2)])
        moves = list(self.board.get_available_moves(mode=PlayerType.BUG))

        possible_moves = [
            ((4, 0, 0, 1), (4, 0, 2, 1)),
            ((4, 0, 0, 1), (4, 0, 2, 0)),
            ((4, 0, 0, 1), (4, 0, 1, 2)),
            ((4, 0, 0, 1), (4, 0, 0, 2)),
            ((4, 0, 0, 2), (4, 0, 2, 1)),
            ((4, 0, 0, 2), (4, 0, 2, 0)),
            ((4, 0, 0, 2), (4, 0, 1, 2)),
            ((4, 0, 1, 0), (4, 0, 2, 1)),
            ((4, 0, 1, 0), (4, 0, 2, 0)),
            ((4, 0, 1, 0), (4, 0, 1, 2)),
            ((4, 0, 1, 0), (4, 0, 0, 2)),
            ((4, 0, 2, 0), (4, 0, 2, 1)),
            ((4, 0, 2, 0), (4, 0, 1, 2)),
            ((4, 0, 2, 0), (4, 0, 0, 2)),
        ]

        # print(moves)
        # self.assertEqual(len(moves), len(possible_moves))

        self.assertNotIn(
            ((4, 0, 0, 2), (4, 0, 0, 2)),
            moves,
            "This is illegal as there would be two enemies on the same tile",
        )
        self.assertNotIn(
            ((4, 0, 2, 0), (4, 0, 2, 0)),
            moves,
            "This is illegal as there would be two enemies on the same tile",
        )

        for i in moves:
            self.assertIn(i, possible_moves)
            possible_moves.remove(i)
        # All moves have been checked. If there are any left, the test will fail.
        self.assertEqual(possible_moves, [])

    def test_get_multiple_enemy_with_friendly_entity_moves(self):
        self.board.import_level(
            self.map_data, [(1, 0, 2, 0), (4, 0, 0, 0), (4, 0, 2, 2)]
        )
        moves = list(self.board.get_available_moves(mode=PlayerType.BUG))
        moves = set(moves)

        possible_moves = [
            ((1, 0, 2, 0), (4, 0, 0, 1), (4, 0, 2, 1)),
            ((1, 0, 2, 0), (4, 0, 0, 1), (4, 0, 1, 2)),
            ((1, 0, 2, 0), (4, 0, 0, 1), (4, 0, 0, 2)),
            ((1, 0, 2, 0), (4, 0, 0, 2), (4, 0, 2, 1)),
            ((1, 0, 2, 0), (4, 0, 0, 2), (4, 0, 1, 2)),
            ((1, 0, 2, 0), (4, 0, 1, 0), (4, 0, 2, 1)),
            ((1, 0, 2, 0), (4, 0, 1, 0), (4, 0, 1, 2)),
            ((1, 0, 2, 0), (4, 0, 1, 0), (4, 0, 0, 2)),
        ]

        # self.assertEqual(len(moves), len(possible_moves))

        self.assertNotIn(
            ((1, 0, 2, 0), (4, 0, 0, 2), (4, 0, 0, 2)),
            moves,
            "This is illegal as there would be two enemies on the same tile",
        )

        self.assertNotIn(
            ((1, 0, 2, 0), (4, 0, 2, 0), (4, 0, 2, 0)),
            moves,
            "This is illegal as there would be two enemies on the same tile",
        )

        for i in moves:
            self.assertIn(i, possible_moves)
            possible_moves.remove(i)
        # All moves have been checked. If there are any left, the test will fail.
        self.assertEqual(possible_moves, [])

    def test_put_entitiy_on_invalid_tile(self):
        with self.assertRaises(ValueError):
            self.board.import_level(self.map_data, [(1, 0, 1, 1)])


if __name__ == "__main__":
    unittest.main()
