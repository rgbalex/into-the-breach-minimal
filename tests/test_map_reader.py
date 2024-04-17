import tempfile
import unittest
from itb.level_importer import LevelImporter


class TestMapReader(unittest.TestCase):
    def setUp(self):
        self.m = LevelImporter()
        self.test_dir = tempfile.TemporaryDirectory()

        self.map_all_zeros = self.test_dir.name + "/all_zeros.txt"
        with open(self.map_all_zeros, "w") as f:
            f.write("00000000\n" * 8)

        self.simple_entity = self.test_dir.name + "/simple_entity.txt"
        with open(self.simple_entity, "w") as f:
            f.write("12340000\n" * 8)
            f.write("*ENTITIES*\n")
            f.write("0 0 3 1\n")

    def test_load_all_zeros(self):
        self.m.load_level(self.map_all_zeros)
        print(self.map_all_zeros)
        # Note: this does not test tile objects
        assert self.m._data == [[0 for _ in range(8)] for _ in range(8)]

    def test_simple_entity(self):
        self.m = LevelImporter()
        self.m.load_level(self.simple_entity)

        self.assertIsInstance(self.m._entities[0], tuple)
        self.assertEqual(len(self.m._entities[0]), 4)
        self.assertEqual(self.m._entities[0], (0, 0, 3, 1))


if __name__ == "__main__":
    unittest.main()
