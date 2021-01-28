from random import randint

from pokemon_combat.pokemon import Pokemon
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.body_part import BodyPart


class PokemonBot(Pokemon):
    def __init__(self):
        bot_name = 'Bot'  # TODO: выбрать имя покемона
        pokemon_type_rand = PokemonType(randint(PokemonType.min_index(), PokemonType.max_index()))
        super().__init__(name=bot_name, pokemon_type=pokemon_type_rand)

    def next_step(self):
        defence_body_part_rand = BodyPart(randint(BodyPart.min_index(), BodyPart.max_index()))
        attack_body_part_rand = BodyPart(randint(BodyPart.min_index(), BodyPart.max_index()))
        super().next_step(defense_body_part=defence_body_part_rand,
                          attack_body_part=attack_body_part_rand)
