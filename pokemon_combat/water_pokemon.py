from pokemon_combat.pokemon import Pokemon, Gender
from pokemon_combat.pokemon_types import PokemonType


class WaterPokemon(Pokemon):
    def __init__(self, name: str, gender: Gender):
        super().__init__(name, gender)

        self.weakness = (PokemonType.ELECTRIC, PokemonType.GRASS)

    def __str__(self):
        return f"Type: Water | {super().__str__()}"
