import numpy as np

from itb.entities import EntityDictionary, PlayerType


class Board:
    _tiles = None
    _entity_dict = EntityDictionary()
    _entities = []

    def import_level(self, map_data: list[list[int]], entities: list[tuple[int]]):
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

    def get_available_moves(self, mode: PlayerType):
        
        if mode not in [PlayerType.MECH, PlayerType.BUG]:
            raise ValueError("Mode must be either MECH or BUG")

        for e in self._entities:
            entity = self._entity_dict.create_entity(e)

            if entity.is_enemy(mode):
                # if the entity is an enemy, dont calculate their moves
                # as it is not their turn
                continue

            # Check if the move is valid
            for move in entity.get_available_moves():
                try:

                    if entity.x + move[0] < 0 or entity.y + move[1] < 0:
                        # Accounts for python allowing negative indexing to loop around
                        raise IndexError

                    if self._tiles[entity.y + move[1]][entity.x + move[0]] in [
                        -1,
                        0,
                    ]:
                        continue

                    # Use of generator statement improves performance
                    # can be optimised with pointer arithmetic if needed
                    yield list(set(self._entities) - set([e])) + [
                        (e[0], e[1], e[2] + move[0], e[3] + move[1])
                    ]

                except IndexError:
                    continue

    # Unsure if used
    # def __repr__(self) -> str:
    #     return "\n".join([str(row) for row in self._tiles])

    def __str__(self) -> str:
        output = "Entities:\n"
        for i in self._entities:
            output += f"{self._entity_dict.create_entity(i)}\n"
        output += "\nTiles:\n"
        output += "\n".join([str(row) for row in self._tiles])
        output += "\n"
        return output
