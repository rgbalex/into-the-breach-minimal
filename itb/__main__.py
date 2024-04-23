from itb.board import Board
from itb.level_importer import LevelImporter


def main():
    m = LevelImporter()
    m.load_level("itb/maps/test-03.txt")

    b = Board()
    b.import_level(m.get_tiles(), m.get_entities())
    print(b)

    players_turn = False

    # while True:
    for i in range(1):
        if players_turn:
            print("Player's turn")
            players_turn = False
        else:
            print("Enemy's turn")

            x = b.get_available_moves(mode="enemy")
            for move in x:
                print(move)

            players_turn = True


if __name__ == "__main__":
    main()
