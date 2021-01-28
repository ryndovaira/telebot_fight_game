from enum import Enum, auto


class PokemonType(Enum):
    """
    Information from https://pokemondb.net/type
    """
    NORMAL = auto()
    FIRE = auto()
    WATER = auto()
    ELECTRIC = auto()
    GRASS = auto()
    ICE = auto()
    FIGHTING = auto()
    POISON = auto()
    GROUND = auto()
    FLYING = auto()
    PSYCHIC = auto()
    BUG = auto()
    ROCK = auto()
    GHOST = auto()
    DRAGON = auto()
    DARK = auto()
    STEEL = auto()
    FAIRY = auto()

    @classmethod
    def min_index(cls):
        return cls.NORMAL.value

    @classmethod
    def max_index(cls):
        return cls.FAIRY.value
