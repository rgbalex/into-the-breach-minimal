import numpy as np

from itb.minimax_result import MinimaxResult
from itb.entities import EntityDictionary, PlayerType
from itb.state import State
from itb.node import Node
from itb.level_importer import LevelImporter


class Board:
    _tiles = None
    _entity_dict = EntityDictionary()
    _l = LevelImporter()
    _state = None
    _root = None

    def __init__(self, level_to_load: str):
        if level_to_load is not None:
            self._l.load_level(level_to_load)
            self.import_level(self._l.get_tiles(), self._l.get_entities())

    def import_level(self, map_data: list[list[int]], entities: list[tuple[int]]):
        self._tiles = map_data
        s = State(self._tiles, entities)
        print(entities)
        self._state = s

    def summary(self):
        if self._root is None:
            print("No root node")
            return

        print(f"Depth of the tree: {self._root.get_depth()}")
        print(f"Number of nodes in the tree: {self._root.count_nodes()}")
        print(f"Number of leaf nodes in the tree: {self._root.count_leaf_nodes()}")

    def get_root(self):
        return self._root

    def get_tile(self, x: int, y: int) -> int:
        return self._tiles[y][x]

    def set_tile(self, x: int, y: int, tile: int):
        self._tiles[y][x] = tile

    def get_available_moves_depth(self, mode: PlayerType, depth: int):
        root = Node(self._state, None, mode, depth, self._entity_dict)
        self._root = root
        return root

    def minimax(self, node, maximisingPlayer: PlayerType, depth=-1):
        # see https://en.wikipedia.org/wiki/Minimax
        if (depth == 0) or node.is_terminal():
            return MinimaxResult(node.get_score(), node)

        if depth > node.get_depth():
            raise ValueError("Depth cannot be greater than the depth of the node")

        carry: MinimaxResult = None

        if maximisingPlayer == PlayerType.BUG:
            value = float("-inf")
            for child in node:
                carry = self.minimax(child, PlayerType.BUG, depth - 1)
                if (carry.value == value) and np.random.choice([True, False]):
                    print("Carry.value == value && random and BUG")
                    print(
                        f"Maximising player: {maximisingPlayer}, Node Player: {node._player}"
                    )
                    # Add a random element to the choice
                    # This is to prevent the same move being chosen every time
                    # and to add some randomness to the AI
                    value = carry.value
                elif carry.value > value:
                    value = carry.value
            return carry
        elif maximisingPlayer == PlayerType.MECH:  # Minimising player
            value = float("inf")
            for child in node:
                carry = self.minimax(child, PlayerType.MECH, depth - 1)
                if (carry.value == value) and np.random.choice([True, False]):
                    print("Carry.value == value && random and MECH")
                    value = carry.value
                    carry.node = child
                elif carry.value < value:
                    value = carry.value
                    carry.node = child
            return carry

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._state:
            output += f"{self._entity_dict.create_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
