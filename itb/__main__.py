import numpy as np
from itb.board import Board
from itb.map_reader import MapReader


def main():
    m = MapReader()
    m.load_map("itb/maps/test-01.txt")

    b = Board()
    b.import_map(m.get_data())

    x = np.array([1, 2, 3])

    def func(x):
        x[0] = 10
        yield x
    
    print(func(x).__next__())

    print(x)

if __name__ == "__main__":
    main()
