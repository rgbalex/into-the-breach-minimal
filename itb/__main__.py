from itb.board import Board
from itb.map_reader import MapReader

def main():
    m = MapReader()
    m.load_map("itb/maps/test-01.txt")

    b = Board()
    b.import_map(m.get_data())
            
    print(b._board[0][0])
if __name__ == "__main__":
    main()