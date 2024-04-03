from unittest.mock import patch, mock_open

from itb.src.map_reader import MapReader
from .utils import map_all_zeros


def test_load_all_zeros(map_all_zeros):
    m = MapReader()
    m.load_map(map_all_zeros)
    print(map_all_zeros)
    # Note: this does not test tile objects
    assert m._data == [[0 for _ in range(8)] for _ in range(8)]
