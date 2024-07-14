import numpy as np

from itb.entities import EntityDictionary, PlayerType
from itb.state import State
from itb.node import Node


class Board:
    _tiles = None
    _entity_dict = EntityDictionary()
    _state = None
    _root = None

    def import_level(self, map_data: list[list[int]], entities: list[tuple[int]]):
        self._tiles = map_data
        s = State(self._tiles, entities)
        print(entities)
        self._state = s
        # print(f"SHOULD NOT BE THE SAME {id(self._state._entities[1])} {id(entities[1])}",)

    def summary(self):
        if self._root is None:
            print("No root node")
            return

        # print the depth of the tree
        print(f"Depth of the tree: {self._root.get_depth()}")
        # print number of nodes in the tree
        print(f"Number of nodes in the tree: {self._root.count_nodes()}")
        # print the number of leaf nodes in the tree
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

    def minimax(self, node, depth: int, maximisingPlayer: PlayerType):
        # TODO: Implement minimax
        # see https://en.wikipedia.org/wiki/Minimax
        if node.is_terminal():
            # TODO: the heuristic value of the node
            return node.get_score()

        if maximisingPlayer == PlayerType.BUG:
            value = float("-inf")
            for child in node:
                value = max(value, self.minimax(child, depth - 1, PlayerType.BUG))
            return value
        elif maximisingPlayer == PlayerType.MECH:  # Minimising player
            value = float("inf")
            for child in node:
                value = min(value, self.minimax(child, depth - 1, PlayerType.MECH))
            return value

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._state:
            output += f"{self._entity_dict.create_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
