import pytest

all_zeros = """00000000
00000000
00000000
00000000
00000000
00000000
00000000
00000000"""


@pytest.fixture
def map_all_zeros(tmpdir):
    p = tmpdir.join("map_all_zeros.txt")
    p.write(all_zeros)
    return str(p)
