from random import randint

from pokemon_combat.pokemon import Pokemon
from pokemon_combat.pokemon_type import PokemonType


class PokemonBot(Pokemon):
    def __init__(self):
        bot_name = 'Bot'  # TODO: выбрать имя покемона
        pokemon_type_rand = PokemonType(randint(PokemonType.min_index(), PokemonType.max_index()))
        super().__init__(name=bot_name, pokemon_type=pokemon_type_rand)
        ...
