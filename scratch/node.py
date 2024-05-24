# Generated code here for reference only. Not to be used in the final project.
from math import sqrt, log


class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.utility = 0
        self.visits = 0
        self.untried_actions = state.get_legal_actions()

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def is_terminal(self):
        return self.state.is_terminal()

    def expand(self):
        action = self.untried_actions.pop()
        new_state = self.state.get_successor(action)
        child = Node(new_state, self, action)
        self.children.append(child)
        return child

    def backpropagate(self, utility):
        self.visits += 1
        self.utility += utility
        if self.parent:
            self.parent.backpropagate(utility)

    def best_child(self, c_param=1.4):
        return max(
            self.children,
            key=lambda c: c.utility / c.visits
            + c_param * sqrt(2 * log(self.visits) / c.visits),
        )

    def best_action(self):
        return max(self.children, key=lambda c: c.visits).action

    def uct_search(self, n):
        for _ in range(n):
            node = self
            while not node.is_terminal():
                if not node.is_fully_expanded():
                    node = node.expand()
                    break
                else:
                    node = node.best_child()
            utility = node.state.get_utility()
            node.backpropagate(utility)
        return self.best_action()
