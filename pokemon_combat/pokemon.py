from random import randint

from pokemon_combat.gender import Gender
from pokemon_combat.state import State


class Pokemon:
    def __init__(self, name: str, gender: Gender) -> None:
        self.level = 0  # одна победа = +1 уровень
        self.name = name  # имя покемона
        self.gender = gender  # пол
        self.hp = 100  # здоровье или очки жизни (hit points)
        self.state = State.INIT

    def __str__(self):
        return f"Name: {self.name} | Gender: {self.gender} | Level: {self.level} | HP: {self.hp}"
