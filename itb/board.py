import numpy as np

from itb.tiles import BaseTile
from itb.map_reader import MapReader


class Board:
    _board = np.array(object=BaseTile)

    def import_map(self, map_data: list[list[int]]):
        self._board = np.array([[BaseTile(tile) for tile in row] for row in map_data])
        