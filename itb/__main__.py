import json
import pprint

from itb.board import Board
from itb.level_importer import LevelImporter
from itb.entities import PlayerType


def main():
    m = LevelImporter()
    m.load_level("itb/maps/test-04.txt")

    b = Board()
    b.import_level(m.get_tiles(), m.get_entities())
    print(b)

    players_turn = False

    # while True:
    print("== Enemy's turn == ")
    x = b.get_available_moves_depth(PlayerType.BUG, 2)

    print(f"Current node: \n{x}")
    json_out = x.to_json()
    json_str = json.loads(json_out)

    with open("dump.json", "w") as f:
        f.write(
            pprint.pformat(
                json_str,
                indent=4,
                width=230,
                sort_dicts=False,
                compact=False,
                depth=10000,
            ).replace("'", '"')
        )


if __name__ == "__main__":
    main()
