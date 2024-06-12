import unittest
import numpy as np

from itb.state import State
from itb.entities import PlayerType


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.tiles = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def test_get_available_moves_no_enemy(self):
        entities = [(1, 0, 0, 0)]
        state = State(self.tiles, entities)
        moves = state.get_available_moves(PlayerType.BUG)
        print(moves)
        self.assertEqual(len(moves), 0)

    def test_get_available_moves_one_enemy(self):
        entities = [(1, 0, 0, 0), (4, 0, 7, 7)]
        state = State(self.tiles, entities)
        moves = state.get_available_moves(PlayerType.BUG)
        self.assertEqual(len(moves), 3)

    def test_get_available_moves_two_enemies(self):
        entities = [(1, 0, 0, 0), (4, 0, 7, 7), (4, 0, 6, 6)]
        state = State(self.tiles, entities)
        moves = state.get_available_moves(PlayerType.BUG)
        print(moves)
        self.assertEqual(len(moves), 11)


if __name__ == "__main__":
    unittest.main()
