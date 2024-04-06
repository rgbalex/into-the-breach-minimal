class MapReader:
    def __init__(self):
        self._data = [[None for _ in range(8)] for _ in range(8)]

    def load_map(self, filename: str) -> list[list[int]]:
        with open(filename, "r") as f:
            for y, line in enumerate(f):
                for x, tile in enumerate(line.strip()):
                    self._data[y][x] = int(tile)

    def get_data(self) -> list[list[int]]:
        return self._data
    