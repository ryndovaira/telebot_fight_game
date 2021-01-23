from pokemon_combat.pokemon import Pokemon, Gender


class FirePokemon(Pokemon):
    def __init__(self, name: str, gender: Gender):
        super().__init__(name, gender)
        ...
