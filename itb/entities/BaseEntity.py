from enum import Enum


class EntityType(Enum):
    UNDEF = 0
    # Good Guys
    MECH_MELEE = 1
    MECH_MORTAR = 2
    MECH_TANK = 3
    # Bad Guys
    BUG_MELEE = 4
    BUG_SHOOTER = 5
    BUG_ELITE = 6


class BaseEntity:
    _type = EntityType.UNDEF
    _health = 0
    _position = (-1, -1)

    default_health = -1
    default_damage = -1

    def get_type(self):
        return self._type

    def set_type(self, type: EntityType):
        self._type = type

    def get_health(self):
        return self._health

    def set_health(self, health: int):
        self._health = health

    def get_position(self):
        return self._position

    def set_position(self, position: tuple[int, int]):
        self._position = position

    def get_available_moves(self):
        raise NotImplementedError

    def get_available_attacks(self):
        raise NotImplementedError

    def __str__(self) -> str:
        return f"Entity of type {self.get_type()} with health {self.get_health()} at position {self.get_position()}"
