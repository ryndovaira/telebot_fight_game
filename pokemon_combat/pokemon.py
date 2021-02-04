from pokemon_combat.state import State
from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses


class Pokemon:
    def __init__(self, name: str, pokemon_type: PokemonType) -> None:
        self.level = 0  # TODO: как увеличивать уровни?
        self.name = name  # имя покемона
        self.type = pokemon_type  # тип покемона (вода, огонь ...)
        self.defence_weaknesses = weaknesses[pokemon_type]      # слабости при защите для данного типа
        self.hp = 100  # TODO: здоровье или очки жизни (hit points)
        self.defense = BodyPart.NOTHING     # что защищаем?
        self.attack = BodyPart.NOTHING      # куда атакуем?
        self.hit_power = (self.level + 1) * 5    # TODO: рассчитать мощность удара
        self.state = State.READY

    def __str__(self):
        return f"Name: {self.name} | Type: {self.type}\nLevel: {self.level} | HP: {self.hp}\nState: {self.state}"

    def next_step(self, defense_body_part: BodyPart, attack_body_part: BodyPart):
        self.defense = defense_body_part
        self.attack = attack_body_part

    def get_hit(self, opponent_attack_body_part: BodyPart, opponent_hit_power: int, opponent_type: PokemonType):
        if self.defense == opponent_attack_body_part:
            return f"{opponent_attack_body_part} has defensed!"
        else:
            # TODO: Add logic in hit power and types
            self.hp -= opponent_hit_power * (2 if opponent_type in self.defence_weaknesses else 1)
            if self.hp > 0:
                return f"Hurt but not defeated! HP: {self.hp}"
            else:
                self.state = State.DEFEATED
                return f"Defeated!"

