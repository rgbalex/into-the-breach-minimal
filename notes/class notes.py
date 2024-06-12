class Board:
    _tiles = None
    _entity_dict = EntityDictionary()
    # the root of the state tree
    _state = None


class State:
    _entities = []

    def get_entities(self):
        return self._entities

    def add_entity(self, type: int, health: int, x: int, y: int):
        pass


class Node:
    state: State = None
    parent = None
    children: list[State] = []
    depth: int = -1
    score: float = -inf

    def __init__(self, state, parent, depth) -> None:
        self.state = state
        self.parent = parent

        # Give the node a score
        self.score = self.evaluate(self.state)

        # populate childeren
        if depth > 0:
            for states in self.state.get_available_moves():
                self.add_child(states, self, depth - 1)
