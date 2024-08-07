import os
import itertools

from typing import Optional
from itb.entities import BaseEntity, PlayerType, EntityDictionary


class State:
    # The state of the board can be defined in the most minimal way as follows:
    # 1. The tiles of the board
    # 2. The entities on the board
    _tiles = None
    _entities = None
    _entity_dict = EntityDictionary()

    def __init__(self, tiles: list[list[int]], entities: list[tuple[int]]):
        # Passed by reference for memory efficiency
        self._tiles = tiles
        # Passed by value
        self._entities = []
        for e in entities:
            if self._tiles[e[3]][e[2]] in [-1, 0]:
                raise ValueError("Cannot place entity on wall or empty tile")
            _tuple = (e[0], e[1], e[2], e[3])

            # Adding check for default health
            if e[1] == 0:
                _tuple = (e[0], self._entity_dict.get_default_health(e[0]), e[2], e[3])
                print(
                    f"Entity {e[0]} has been given default health of {self._entity_dict.get_default_health(e[0])}"
                )

            self._entities.append(_tuple)

    def to_json(self):
        # If environment variable verbose is set to true, print the state
        if "verbose" in os.environ:
            if os.environ["verbose"] == "true":
                return (
                    '{"tiles":'
                    + str(self._tiles)
                    + ","
                    + '"entities": '
                    + str(list(self.list_entities()))
                    + "}".replace("'", '"')
                )
        return '{"entities": ' + str(list(self.list_entities())) + "}".replace("'", '"')

    def __iter__(self):
        return iter(self._entities)

    def __str__(self) -> str:
        outstr = f"    State at {hex(id(self))}"
        outstr += f"\n    Tiles:"
        for row in self._tiles:
            outstr += f"\n      {row}"
        outstr += f"\n    Entities:"
        for e in self._entities:
            outstr += f"\n      {e}"
        return outstr

    def list_entities(self):
        for i in self._entities:
            yield [i[0], i[1], i[2], i[3]]

    def get_valid_entity_moves(self, entity: tuple[int]):
        e: BaseEntity = self._entity_dict.create_entity(entity)
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
                    if entity[0] != 7:
                        # If the move would put the entity on a tile with another entity, the move is invalid
                        continue
                    # if the entity is a building, it can move to its own tile on top of itself

                yield (entity[0], entity[1], e.x + move[0], e.y + move[1])

            except IndexError:
                # We get here only when there is a move that goes off the end of the board
                # so we can safely take no action and continue.
                continue

    def get_available_moves(self, mode: PlayerType):
        if mode not in [PlayerType.MECH, PlayerType.BUG]:
            raise ValueError("Mode must be either MECH or BUG")

        moving_entities = []
        no_valid_moves = True
        for e in self._entities:
            entity: BaseEntity = self._entity_dict.create_entity(e)
            # Perhaps map the is_enemy function to a fresh list of entities
            # then check if false is in list then run
            # This avoids the need for the flag and constant check
            if entity.is_enemy(mode):
                # if the entity is an enemy, dont calculate their moves
                # as it is not their turn; just append the current entity.
                moving_entities.append([e])
            else:
                no_valid_moves = False
                moving_entities.append(self.get_valid_entity_moves(e))

        if no_valid_moves:
            # Stops an edge case where the code will return a valid board state of just enemy pieces
            # when there are no valid moves for the moving player.
            return []

        # Solving conditions on product
        # https://stackoverflow.com/questions/27891032/python-cartesian-product-and-conditions
        def process_moves(moves):
            unpacked_moves = [(t[-2], t[-1]) for t in moves]
            return any(unpacked_moves.count(i) > 1 for i in unpacked_moves)

        # Calculate the cartesian product of the lists of moves
        all_moves = itertools.product(*moving_entities)

        # Apply filter to remove extraneous moves
        filtered_moves = itertools.filterfalse(process_moves, all_moves)

        return list(filtered_moves)

    def get_entity_by_coords(self, x: int, y: int) -> Optional[tuple[int]]:
        for e in self._entities:
            if e[2] == x and e[3] == y:
                return e
        return None
