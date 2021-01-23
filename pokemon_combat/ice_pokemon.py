from pokemon_combat.pokemon import Pokemon, Gender
from pokemon_combat.pokemon_types import PokemonType


class IcePokemon(Pokemon):
    def __init__(self, name: str, gender: Gender):
        super().__init__(name, gender)

        self.weakness = (PokemonType.FIRE, PokemonType.STEEL, PokemonType.FIGHTING, PokemonType.ROCK)

    def __str__(self):
        return f"Type: Fire | {super().__str__()}"
