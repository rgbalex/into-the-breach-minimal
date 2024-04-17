import BaseEntity


class MechMelee(BaseEntity):
    def __init__(self, health: int, type: int, position: tuple[int, int]):
        self.set_health(health)
        self.set_type(type)
        self.set_position(position)

        self.default_health = 4
        self.default_damage = 2

    def get_available_moves(self):
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 2), (0, -2), (2, 0), (-2, 0)]

    def get_available_attacks(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]
