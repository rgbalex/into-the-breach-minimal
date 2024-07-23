from .BaseEntity import BaseEntity, PlayerType


class Building(BaseEntity):
    def get_available_moves(self):
        return [(0, 0)]

    def get_available_attacks(self):
        return []

    def set_defaults(self):
        self.default_health = 2
        self.default_damage = 0
        self.player = PlayerType.MECH
        self.colour = (128, 0, 128)
