from math import inf

class Node:
    # Current state for this node
    state: list = []
    # Parent node
    parent = None
    # Child nodes
    children = []
    # Depth of this node (used during evaluation)
    depth: int = None
    # Calculated score for this node
    score: float = -inf

    def __init__(self, state: list, parent, mode, depth: int = -1):
        if parent is None:
            # Yes it can it is the root node.
            # raise ValueError("Parent cannot be none")
            pass
        if state is None or len(state) == 0:
            raise ValueError("State cannot be none/empty")    
        if depth == -1:
            raise  ValueError("Depth cannot be -1")
        
        self.state = state
        self.parent = parent

        # Give the node a score 
        self.score = self.evaluate(self.state)

        # populate childeren
        if depth > 0:
            for states in 

        return

    def evaluate(self, state: list) -> float:
        return 0.0
    
    def add_child(self, state, parent, depth):
        child = Node(state, parent, depth)
        self.children.append(child)

    def heuristic_value(self):
        # TODO: Implement heuristic value
        pass

    def is_terminal(self):
        return len(self.children) == 0

    def __iter__(self):
        for child in self.children:
            yield child

    def __str__(self):
        return f"Node: {self.state} with score {self.score} with {len(self.children)} children"
    