from itb.entities import PlayerType
from itb.state import State

inf = float("inf")


class Node:
    # A node is a collection of a state, a parent node, a player type, score, and depth.
    _player: PlayerType = None
    _state: State = None
    _score: float = -inf
    _depth: int = None
    _parent = None
    _children = None

    string_buff = ""

    def __init__(self, state: State, parent, player: PlayerType, depth: int):
        self._state = state
        self._player = player
        self._depth = depth
        self._parent = parent
        self._children = list()

        self._score = self._state.heuristic_value()

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
                self._children.append(Node(s, self, player, depth - 1))

    def count_nodes(self) -> int:
        count = 1
        for c in self._children:
            count += c.count_nodes()
        return count

    def get_depth(self) -> int:
        return self._depth

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
