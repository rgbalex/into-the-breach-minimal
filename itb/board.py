import numpy as np

from itb.tiles import BaseTile


class Board:
    _board = np.array(object=BaseTile)

    def import_map(self, map_data: list[list[int]]):
        self._board = np.array([[BaseTile(tile) for tile in row] for row in map_data])

    def get_tile(self, x: int, y: int) -> BaseTile:
        return self._board[y][x]

    def set_tile(self, x: int, y: int, tile: BaseTile):
        self._board[y][x] = tile

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self._board])
