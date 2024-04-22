import numpy as np

from itb.entities.EntityDictionary import EntityDictionary


class Board:
    # _tiles = np.array(object=BaseTile)
    _tiles = np.array(object=np.int32)
    _entity_dict = EntityDictionary()
    _entities = []

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

    def get_available_moves(self, mode: str):
        states = []
        if mode == "player":
            pass
        elif mode == "enemy":
            for e in self._entities:
                entity = self._entity_dict.get_entity(e)
                if not entity.player:
                    moves = entity.get_available_moves()
                    # Check if the move is valid
                    for move in moves:
                        try:
                            if self._tiles[entity.y + move[1]][entity.x + move[0]] != 0:
                                states.append((entity.x, entity.y, entity.x + move[0], entity.y + move[1]))
                        except IndexError:
                            # Out of bounds
                            pass
        else:
            raise ValueError("Invalid mode")
        return states

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
