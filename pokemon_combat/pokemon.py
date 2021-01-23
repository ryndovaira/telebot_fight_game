from enum import Enum


class Gender(Enum):
    GENDERLESS = 0
    MALE = 1
    FEMALE = 2


class Pokemon:
    def __init__(self, name: str, gender: Gender) -> None:
        self.level = 0          # одна победа = +1 уровень
        self.name = name        # имя покемона
        self.gender = gender    # пол

    def __str__(self):
        return f"Name: {self.name} | Gender: {self.gender} | Level: {self.level}"
