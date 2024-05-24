class Node:
    parent = None  # type: Node
    children = []  # type: list[Node]
    state = None  # type: tuple[tuple[int,int,int,int]]

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def heuristic_value(self):
        # TODO: Implement heuristic value
        pass

    def is_terminal(self):
        return len(self.children) == 0

    def __iter__(self):
        for child in self.children:
            yield child
