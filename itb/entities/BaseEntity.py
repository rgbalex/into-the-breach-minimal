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
    # Objectives
    BUILDING = 7


class PlayerType(Enum):
    UNDEF = 0
    MECH = 1
    BUG = 2


def get_opponent(player: PlayerType):
    if player == PlayerType.MECH:
        return PlayerType.BUG
    elif player == PlayerType.BUG:
        return PlayerType.MECH
    else:
        return PlayerType.UNDEF


class BaseEntity:
    _type = EntityType.UNDEF
    _health = 0

    x = -1
    y = -1

    # This will raise an error if rendered as colour is not valid
    colour = (-1, -1, -1)

    player = PlayerType.UNDEF
    default_health = -1
    default_damage = -1

    def __init__(self, ctor: tuple[int, int, int, int]):
        (type, health, x, y) = ctor
        self._type = EntityType(type)
        self.set_defaults()
        self._health = self.default_health if health == 0 else health
        self.x = x
        self.y = y

    def is_enemy(self, _type: EntityType):
        return self.player != _type

    def set_defaults(self):
        raise NotImplementedError

    def get_type(self):
        return self._type

    def set_type(self, type: EntityType):
        self._type = type

    def get_health(self):
        return self._health

    def set_health(self, health: int):
        self._health = health

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, position: tuple[int, int]):
        x, y = position
        self.x = x
        self.y = y

    def get_colour(self):
        return self.colour

    def get_available_moves(self):
        raise NotImplementedError

    def get_available_attacks(self):
        raise NotImplementedError

    def __str__(self) -> str:
        return f"Type: {self.get_type()}\t Health: {self.get_health()}\t Position: {self.get_position()}"
