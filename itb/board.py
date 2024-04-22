import numpy as np

from itb.entities.EntityDictionary import EntityDictionary


class Board:
    # _tiles = np.array(object=BaseTile)
    _tiles = np.array(object=np.int32)
    _entity_dict = EntityDictionary()

    def import_level(self, map_data: list[list[int]], entities: list[tuple[int]]):
        # self._tiles = np.array([[BaseTile(tile) for tile in row] for row in map_data])
        self._tiles = np.array(map_data)
        # LUT for entities
        self._entities = entities

    def get_tile(self, x: int, y: int) -> int:
        return self._tiles[y][x]

    def set_tile(self, x: int, y: int, tile: int):
        self._tiles[y][x] = tile

    def get_entities(self):
        return self._entities

    def add_entity(self, type: int, health: int, x: int, y: int):
        self._entities.append((type, health, x, y))

    def __repr__(self) -> str:
        return "\n".join([str(row) for row in self._tiles])

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._entities:
            output += f"{self._entity_dict.get_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
