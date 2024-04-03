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

    def set_type(self, type: TileType):
        self._type = type

    def get_type(self):
        return self._type

    # TODO: Define types for tile content entities
    def set_contents(self, contents):
        self._contents = contents

    def get_contents(self):
        return self._contents


# TODO: Separate tile types into separate files


class GrassTile(BaseTile):
    def __init__(self):
        self.set_type(TileType.GRASS)


class WaterTile(BaseTile):
    def __init__(self):
        self.set_type(TileType.WATER)


class ChasmTile(BaseTile):
    def __init__(self):
        self.set_type(TileType.CHASM)


class MountainTile(BaseTile):
    def __init__(self):
        self.set_type(TileType.MOUNTAIN)
