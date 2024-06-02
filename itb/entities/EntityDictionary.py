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

    def create_entity(self, ctor: tuple[int, int, int, int]):
        return self.entity_dict[EntityType(ctor[0])](ctor)
