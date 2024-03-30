from itb.src.board import Board

class MapReader:
    def __init__(self):
        self._data = [[None for _ in range(8)] for _ in range(8)]

    def load_map(self, filename: str):
        with open(filename, 'r') as f:
            for y, line in enumerate(f):
                for x, tile in enumerate(line.split()):
                    self._data[y][x] = tile
        print(self._data)

