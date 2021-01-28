from enum import Enum, auto


class BodyPart(Enum):
    NOTHING = auto()    # ничего (начальное состояние)
    HEAD = auto()       # голова
    BELLY = auto()      # живот
    LEGS = auto()       # ноги
