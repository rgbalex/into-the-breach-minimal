import unittest
import numpy as np

from itb.state import State
from itb.entities import PlayerType


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.map_data = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
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

    def test_get_single_enemy_entity_moves(self):
        entities = [(4, 0, 0, 0)]
        state = State(self.map_data, entities)
        moves = state.get_available_moves(mode=PlayerType.BUG)

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
        entities = [(4, 0, 0, 0), (4, 0, 2, 2)]
        state = State(self.map_data, entities)
        moves = state.get_available_moves(mode=PlayerType.BUG)

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
        entities = [(1, 0, 2, 0), (4, 0, 0, 0), (4, 0, 2, 2)]
        state = State(self.map_data, entities)
        moves = state.get_available_moves(mode=PlayerType.BUG)
        # moves = set(moves)

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


if __name__ == "__main__":
    unittest.main()
