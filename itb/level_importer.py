class LevelImporter:
    def __init__(self):
        self._data = [[None for _ in range(8)] for _ in range(8)]
        self._entities = []

    def load_level(self, filename: str) -> list[list[int]]:
        with open(filename, "r") as f:
            print("Processing tiles...")
            processing_tiles = True
            for y, line in enumerate(f):
                # in the whole file:
                if line.strip() == "*ENTITIES*":
                    print("Processing entities...")
                    processing_tiles = False
                    continue

                if processing_tiles:
                    for x, tile in enumerate(line.strip()):
                        self._data[y][x] = int(tile)
                else:
                    self._entities.append(tuple([int(n) for n in line.split()]))
        print("Done processing level file.\n")

    def get_tiles(self) -> list[list[int]]:
        return self._data

    def get_entities(self) -> list[tuple[int]]:
        return self._entities
