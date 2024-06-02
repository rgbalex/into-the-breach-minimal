import unittest
from itb.tiles import *


class TestTiles(unittest.TestCase):
    def test_grass_tile_instance(self):
        t = BaseTile()
        t.set_type(TileType.GRASS)
        self.assertEqual(t.get_type(), TileType.GRASS)

    def test_water_tile_instance(self):
        t = BaseTile()
        t.set_type(TileType.WATER)
        self.assertEqual(t.get_type(), TileType.WATER)

    def test_chasm_tile_instance(self):
        t = BaseTile()
        t.set_type(TileType.CHASM)
        self.assertEqual(t.get_type(), TileType.CHASM)

    def test_mountain_tile_instance(self):
        t = BaseTile()
        t.set_type(TileType.MOUNTAIN)
        self.assertEqual(t.get_type(), TileType.MOUNTAIN)

    def test_undef_tile_instance(self):
        t = BaseTile()
        t.set_type(TileType(0))
        self.assertEqual(t.get_type(), TileType.UNDEF)
        t = BaseTile()
        self.assertEqual(t.get_type(), TileType.UNDEF)


if __name__ == "__main__":
    unittest.main()
