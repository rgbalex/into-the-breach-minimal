from unittest.mock import patch
from itb.src.map_reader import MapReader

all_zeros = \
"""000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000"""

def test_load_all_zeros(map_all_zeros):
    m = MapReader()
    m.load_map(map_all_zeros)
    print(map_all_zeros)
    assert m == [[0 for _ in range(8)] for _ in range(8)]
