import numpy as np

from itb.tiles import BaseTile


class Board:
    # _tiles = np.array(object=BaseTile)
    _tiles = np.array(object=np.int32)

    def import_map(self, map_data: list[list[int]]):
        # self._tiles = np.array([[BaseTile(tile) for tile in row] for row in map_data])
        self._tiles = np.array(map_data)
        # LUT for entities
        self._entities = {}

    def get_tile(self, x: int, y: int) -> int:
        return self._tiles[y][x]

    def set_tile(self, x: int, y: int, tile: int):
        self._tiles[y][x] = tile

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self._tiles])
