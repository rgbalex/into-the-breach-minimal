from itb.node import Node


class MinimaxResult:
    def __init__(self, value: float, node: Node):
        self.value = value
        self.node = node

    def __str__(self) -> str:
        return f"Value: {self.value} Node: {self.node}"
