from itb.tiles import *


# To test imports are setup correctly.
def test_grass_tile_instance():
    t = BaseTile()
    t.set_type(TileType.GRASS)
    assert t.get_type() == TileType.GRASS


def test_water_tile_instance():
    t = BaseTile()
    t.set_type(TileType.WATER)
    assert t.get_type() == TileType.WATER


def test_chasm_tile_instance():
    t = BaseTile()
    t.set_type(TileType.CHASM)
    assert t.get_type() == TileType.CHASM


def test_mountain_tile_instance():
    t = BaseTile()
    t.set_type(TileType.MOUNTAIN)
    assert t.get_type() == TileType.MOUNTAIN


def test_undef_tile_instance():
    t = BaseTile()
    t.set_type(TileType(0))
    assert t.get_type() == TileType.UNDEF
    t = BaseTile()
    assert t.get_type() == TileType.UNDEF
