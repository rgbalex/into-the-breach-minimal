from .BaseEntity import BaseEntity


class MechMelee(BaseEntity):
    def get_available_moves(self):
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 2), (0, -2), (2, 0), (-2, 0)]

    def get_available_attacks(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def set_defaults(self):
        self.default_health = 4
        self.default_damage = 2
