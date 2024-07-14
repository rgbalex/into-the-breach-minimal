import unittest
import numpy as np

from itb.node import Node
from itb.state import State
from itb.entities import EntityDictionary, PlayerType


class TestNode(unittest.TestCase):
    def setUp(self):
        self.entity_dict = EntityDictionary()
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
        # Despite asking for a depth of 3, the node will be terminal
        # as there are no available moves
        node = Node(state, None, PlayerType.BUG, 3, self.entity_dict)
        print(node)

        self.assertEqual(node.is_terminal(), True)

    def test_get_available_moves_one_enemy_depth_one(self):
        entities = [(1, 0, 0, 0), (4, 0, 7, 7)]
        state = State(self.tiles, entities)
        node = Node(state, None, PlayerType.BUG, 1, self.entity_dict)
        print(node)

        self.assertEqual(node.is_terminal(), False)

        self.assertEqual(len(node._children), 3)

        self.assertEqual(node._children[0].is_terminal(), True)
        self.assertEqual(node._children[1].is_terminal(), True)
        self.assertEqual(node._children[2].is_terminal(), True)

        self.assertEqual(
            len(node._children[0]._state.get_available_moves(PlayerType.BUG)), 5
        )
        self.assertEqual(
            len(node._children[1]._state.get_available_moves(PlayerType.BUG)), 4
        )
        self.assertEqual(
            len(node._children[2]._state.get_available_moves(PlayerType.BUG)), 5
        )

    def test_get_available_moves_one_enemy_depth_two(self):
        entities = [(1, 0, 0, 0), (4, 0, 7, 7)]
        state = State(self.tiles, entities)
        node = Node(state, None, PlayerType.BUG, 2, self.entity_dict)
        print(node)

        self.assertEqual(node.is_terminal(), False)

        self.assertEqual(len(node._children), 3)

        self.assertEqual(node._children[0].is_terminal(), False)
        self.assertEqual(node._children[1].is_terminal(), False)
        self.assertEqual(node._children[2].is_terminal(), False)

        self.assertEqual(
            len(node._children[0]._state.get_available_moves(PlayerType.BUG)), 5
        )
        self.assertEqual(
            len(node._children[1]._state.get_available_moves(PlayerType.BUG)), 4
        )
        self.assertEqual(
            len(node._children[2]._state.get_available_moves(PlayerType.BUG)), 5
        )

        s = node._children[0]
        self.assertEqual(
            len(s._children[0]._state.get_available_moves(PlayerType.BUG)), 5
        )
        self.assertEqual(
            len(s._children[1]._state.get_available_moves(PlayerType.BUG)), 5
        )
        self.assertEqual(
            len(s._children[2]._state.get_available_moves(PlayerType.BUG)), 5
        )

        self.assertEqual(s._children[0].is_terminal(), True)
        self.assertEqual(s._children[1].is_terminal(), True)
        self.assertEqual(s._children[2].is_terminal(), True)


if __name__ == "__main__":
    unittest.main()
