from enum import Enum, auto


class BodyPart(Enum):
    NOTHING = auto()  # ничего (начальное состояние)
    HEAD = auto()  # голова
    BELLY = auto()  # живот
    LEGS = auto()  # ноги

    @classmethod
    def min_index(cls):
        return cls.HEAD.value

    @classmethod
    def max_index(cls):
        return cls.LEGS.value

    @classmethod
    def has_item(cls, name):
        return name in cls._member_names_
