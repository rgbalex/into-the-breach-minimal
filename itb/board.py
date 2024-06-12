import numpy as np

from itb.entities import EntityDictionary, PlayerType
from itb.state import State
from itb.node import Node


class Board:
    _tiles = None
    _entity_dict = EntityDictionary()
    _state = None

    def import_level(self, map_data: list[list[int]], entities: list[tuple[int]]):
        self._tiles = np.array(map_data)
        self._state = State(self._tiles)
        # LUT for entities
        for i in entities:
            self._state.add_entity(i[0], i[1], i[2], i[3])

    def get_tile(self, x: int, y: int) -> int:
        return self._tiles[y][x]

    def set_tile(self, x: int, y: int, tile: int):
        self._tiles[y][x] = tile

    def get_available_moves_depth(self, mode: PlayerType, depth: int):
        root = Node(self._state, None, mode, 1)
        return root

    
    def minimax(self, node, depth: int, maximisingPlayer: PlayerType):
        # TODO: Implement minimax
        # see https://en.wikipedia.org/wiki/Minimax
        if depth == 0 or node.is_terminal():
            # TODO: the heuristic value of the node
            return node.heuristic_value()

        if maximisingPlayer:
            value = float("-inf")
            for child in node:
                # TODO: Wrapper for playertype flip flop
                value = max(value, self.minimax(child, depth - 1, False))
            return value
        else:  # Minimising player
            value = float("inf")
            for child in node:
                value = min(value, self.minimax(child, depth - 1, True))
            return value

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._state.get_entities():
            output += f"{self._entity_dict.create_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
