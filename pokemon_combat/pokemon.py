from random import randint

from pokemon_combat.gender import Gender
from pokemon_combat.state import State
from pokemon_combat.pokemon_type import PokemonType


class Pokemon:
    def __init__(self, name: str, gender: Gender, pokemon_type: PokemonType) -> None:
        self.level = 0  # одна победа = +1 уровень
        self.name = name  # имя покемона
        self.gender = gender  # пол
        self.type = pokemon_type  # тип покемона (вода, огонь ...)
        self.hp = 100  # здоровье или очки жизни (hit points)
        self.state = State.INIT  # текущее состояние (начальное, удар, защита)

    def __str__(self):
        return f"Name: {self.name} | Type: {self.type} | Gender: {self.gender} | Level: {self.level} | HP: {self.hp}"

    def hit(self):
        return randint(self.level + 1, self.level + 5) + (1 if self.gender == Gender.MALE else 0)

    def defense(self):
        return randint(self.level + 1, self.level + 5) + (1 if self.gender == Gender.FEMALE else 0)
