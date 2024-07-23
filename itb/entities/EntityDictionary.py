from itb.entities import *


class EntityDictionary:
    def __init__(self):
        self.entity_dict = {}
        self.entity_dict[EntityType.MECH_MELEE] = MechMelee
        # self.entity_dict[EntityType.MECH_MORTAR] = MechMortar
        # self.entity_dict[EntityType.MECH_TANK] = MechTank
        self.entity_dict[EntityType.BUG_MELEE] = BugMelee
        # self.entity_dict[EntityType.BUG_SHOOTER] = BugShooter
        # self.entity_dict[EntityType.BUG_ELITE] = BugElite
        self.entity_dict[EntityType.BUILDING] = Building

    def create_entity(self, ctor: tuple[int, int, int, int]):
        return self.entity_dict[EntityType(ctor[0])](ctor)

    def get_default_health(self, entity_type: int):
        return self.create_entity((entity_type, 0, 0, 0)).get_health()

    def get_default_colour(self, entity_type: int) -> tuple[int, int, int]:
        return self.create_entity((entity_type, 0, 0, 0)).get_colour()
