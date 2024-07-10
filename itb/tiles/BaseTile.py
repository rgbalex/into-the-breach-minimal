from enum import Enum


class TileType(Enum):
    UNDEF = 0
    GRASS = 1
    WATER = 2
    CHASM = 3
    MOUNTAIN = 4


class BaseTile:
    _type = TileType.UNDEF
    _contents = None

    def __init__(self, type: TileType = TileType.UNDEF, contents=None):
        self._type = type
        self._contents = contents

    def __init__(self, type: int = 0, contents=None):
        # to handle integer TileType values
        self._type = TileType(type)
        self._contents = contents

    def set_type(self, type: TileType):
        self._type = type

    def get_type(self):
        return self._type

    # DEPRECIATED: Define types for tile content entities
    def set_contents(self, contents):
        self._contents = contents

    def get_contents(self):
        return self._contents

    def __str__(self) -> str:
        return f"Tile of type {self.get_type()} with contents {self.get_contents()}"
