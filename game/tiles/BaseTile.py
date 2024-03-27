from enum import Enum


class TileType(Enum):
    UNDEF = 0
    GRASS = 1
    WATER = 2
    CHASM = 3


class BaseTile:
    _type = TileType.UNDEF
    _contents = None

    def set_type(self, type: TileType):
        self._type = type

    def get_type(self):
        return self._type

    # TODO: Define types for tile content entities
    def set_contents(self, contents):
        self._contents = contents

    def get_contents(self):
        return self._contents
