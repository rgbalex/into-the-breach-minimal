import pprint
import json


class Serialiser:
    tree = None

    def serialise(self, file="output.json"):
        if self.tree is None:
            raise ValueError("Cannot serialise an empty tree")

        json_out = self.tree.to_json()
        json_str = json.loads(json_out)

        with open(file, "w") as f:
            f.write(
                pprint.pformat(
                    json_str,
                    indent=4,
                    width=300,
                    sort_dicts=False,
                    compact=False,
                ).replace("'", '"')
            )
