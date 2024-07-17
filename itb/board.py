from typing import Optional
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
    _ramdomise = False

    def __init__(self, level_to_load: str, randomise: bool = False):
        if level_to_load is not None:
            self._l.load_level(level_to_load)
            self.import_level(self._l.get_tiles(), self._l.get_entities())
        self._ramdomise = randomise

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

    def get_entity_by_coords(self, x: int, y: int) -> Optional[tuple[int]]:
        return self._state.get_entity_by_coords(x, y)

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

    def minimax(self, node: Node, maximisingPlayer: PlayerType, depth=-1):
        node.calculate_value()
        # see https://en.wikipedia.org/wiki/Minimax
        if (depth == 0) or node.is_terminal():
            return MinimaxResult(node.get_score(), node)

        if depth > node.get_depth():
            raise ValueError("Depth cannot be greater than the depth of the node")

        return_value: MinimaxResult = None
        current_value: MinimaxResult = None

        if node.get_player() == maximisingPlayer:
            return_value = MinimaxResult(-np.inf, None)
            for child in node:
                current_value = self.minimax(child, maximisingPlayer, depth - 1)
                if (current_value.value == return_value.value) and self._ramdomise:
                    if np.random.choice([True, False]):
                        return_value = current_value
                if current_value.value > return_value.value:
                    return_value = current_value
        else:
            return_value = MinimaxResult(np.inf, None)
            for child in node:
                current_value = self.minimax(child, maximisingPlayer, depth - 1)
                if (current_value.value == return_value.value) and self._ramdomise:
                    if np.random.choice([True, False]):
                        return_value = current_value
                if current_value.value < return_value.value:
                    return_value = current_value
        return return_value

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._state:
            output += f"{self._entity_dict.create_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
