from .BaseEntity import BaseEntity, PlayerType


class MechMelee(BaseEntity):
    def get_available_moves(self):
        # For now this does not consider that the mech can't move through walls
        # this can be fixed by setting a numeric value for distance and traversing the board.
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 2), (0, -2), (2, 0), (-2, 0)]

    def get_available_attacks(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def set_defaults(self):
        self.default_health = 4
        self.default_damage = 2
        self.player = PlayerType.MECH
        self.colour = (109, 112, 117)
