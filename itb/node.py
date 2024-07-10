from itb.entities import PlayerType, get_opponent
from itb.state import State

inf = float("inf")


class Node:
    # A node is a collection of a state, a parent node, a player type, score, and depth.
    _player: PlayerType = None
    _state: State = None
    _score: float = 0.0
    _depth: int = None
    _parent = None
    _children = None

    string_buff = ""

    def is_enemy_entity_type(self, playerType: int) -> bool:
        if playerType in {1, 2, 3}:
            return True if self._player == PlayerType.MECH else False
        elif playerType in {4, 5, 6}:
            return False if self._player == PlayerType.BUG else True
        raise ValueError(f"Entity type {playerType} is not a defined player type.")

    def __init__(self, state: State, parent, player: PlayerType, depth: int):
        self._state = state
        self._player: PlayerType = player
        self._depth = depth
        self._parent = parent
        self._children = []

        # self._score = self._state.calculate_value()

        if depth > 0:
            # if depth is larger than 0, create children
            # the childeren should contain states that are the result of the available moves
            # self.string_buff += "\nCreating children"
            for new_state in state.get_available_moves(player):
                # new state here is passed by reference since it is coming from a list
                # self.string_buff += f"\n{new_state} + {new_state.__class__}"
                l = []
                for i in new_state:
                    t = tuple([i[0], i[1], i[2], i[3]])
                    l.append(t)
                l = tuple(l)
                s = State(tiles=self._state._tiles, entities=l)
                self._children.append(
                    Node(s, self, get_opponent(self._player), depth - 1)
                )

        self._score = self.calculate_value()

    def calculate_value(self) -> float:
        score: float = 0.0
        for e in self._state.list_entities():
            calculated_score: float = 0.0
            # Entities are in the form of [type, health, x, y]
            # TODO: Implement converter helper for converting type of entity to player type

            # Scoring has some base elements as follows:
            #   Base score for number of entities
            #   Base score for 1/4 health of entities
            calculated_score += 1
            # calculated_score += e[1] / 4

            if self.is_enemy_entity_type(e[0]):
                calculated_score = -1 * calculated_score

            # print(f"Entity: {e} Score: {calculated_score}")
            score += calculated_score

        self._score = score
        print(f"Node score: {score}")
        return score

    def count_nodes(self) -> int:
        count = 1
        for c in self._children:
            count += c.count_nodes()
        return count

    def get_depth(self) -> int:
        return self._depth

    def get_score(self) -> float:
        return self._score

    def count_leaf_nodes(self) -> int:
        count = 0
        if len(self._children) == 0:
            return 1
        for c in self._children:
            count += c.count_leaf_nodes()
        return count

    def is_terminal(self) -> bool:
        return len(self._children) == 0

    def to_json(self):
        return (
            '{"player":"'
            + str(self._player.name)
            + '",'
            + '"depth": '
            + str(self._depth)
            + ","
            + '"score": '
            + str(self._score)
            + ","
            + '"state": '
            + self._state.to_json()
            + ","
            + '"children": '
            + str([c.to_json() for c in self._children]).replace("'", "")
            + "}".replace("'", '"')
        )
        # "\"state\": "+self._state.to_json()+ \

    def __str__(self) -> str:
        outstr = f" Node at {hex(id(self))}"
        outstr += f"\n  Player: {self._player}"
        outstr += f"\n  Depth: {self._depth}"
        outstr += f"\n  Parent: {hex(id(self._parent)) if self._parent is not None else str(None)}"
        outstr += f"\n  Score: {self._score}"
        outstr += f"\n  State:\n{self._state}"
        # outstr += f"\n\nString buffer: {self.string_buff}"

        outstr += f"\n  Children ({len(self._children)})"
        if len(self._children) > 0:
            outstr += f":"
            for c in self._children:
                lines = []
                lines += str(c).split("\n")
                for line in lines:
                    outstr += f"\n  {line}"
        return outstr

    def __iter__(self):
        return iter(self._children)
