import pprint

from itb.board import Node


class Serialiser:
    tree = None
    data = None

    def set_tree(self, node: Node):
        self.tree = node

    def set_data(self):
        if self.tree is None:
            raise ValueError("No tree to serialise")
        self.data = pprint.pformat(
            self.tree.to_json(), indent=4, sort_dicts=False
        ).replace("'", '"')

    def serialise(self, file="output.json"):
        self.set
        if self.data is None:
            raise ValueError("No data to serialise")
        with open(file, "w") as f:
            f.write(self.data)
