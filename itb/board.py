import itertools
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

    def get_valid_entity_moves(self, entity: tuple[int]):
        e = self._entity_dict.create_entity(entity)
        for move in e.get_available_moves():
            try:

                if e.x + move[0] < 0 or e.y + move[1] < 0:
                    # Accounts for python allowing negative indexing to loop around
                    raise IndexError

                if self._tiles[e.y + move[1]][e.x + move[0]] in [
                    -1,
                    0,
                ]:
                    # If the tile is a wall or empty, the move is invalid
                    continue

                if any(
                    [
                        e.x + move[0] == x and e.y + move[1] == y
                        for x, y in [
                            (entity[2], entity[3]) for entity in self._entities
                        ]
                    ]
                ):
                    # If the move would put the entity on a tile with another entity, the move is invalid
                    continue

                yield (entity[0], entity[1], e.x + move[0], e.y + move[1])
            except IndexError:
                # We get here only when there is a move that goes off the end of the board
                # so we can safely take no action and continue.
                continue

    def get_available_moves(self, mode: PlayerType):
        if mode not in [PlayerType.MECH, PlayerType.BUG]:
            raise ValueError("Mode must be either MECH or BUG")

        moving_entities = []

        for e in self._entities:
            entity = self._entity_dict.create_entity(e)

            if entity.is_enemy(mode):
                # if the entity is an enemy, dont calculate their moves
                # as it is not their turn
                continue

            moving_entities.append(self.get_valid_entity_moves(e))

        # Calculate the cartesian product of the lists of moves
        return itertools.product(*moving_entities)

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
