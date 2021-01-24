from pokemon_combat.gender import Gender
from pokemon_combat.pokemon import Pokemon
from pokemon_combat.pokemon_types import PokemonType


class FirePokemon(Pokemon):
    def __init__(self, name: str, gender: Gender):
        super().__init__(name, gender)

        self.weakness = (PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK)

    def __str__(self):
        return f"Type: Fire | {super().__str__()}"

