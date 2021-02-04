from pokemon_combat.state import State
from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses

from pokemon_combat.pokemon import Pokemon


class TestPokemonClass:
    name = "Pika"
    pokemon_type = PokemonType.ELECTRIC

    def test_init(self):
        pokemon = Pokemon(name=self.name, pokemon_type=self.pokemon_type)
        assert pokemon.name == self.name
        assert pokemon.type == self.pokemon_type
        assert pokemon.defence_weaknesses == weaknesses[self.pokemon_type]
        assert pokemon.level == 0
        assert pokemon.hp == 100
        assert pokemon.defense == BodyPart.NOTHING
        assert pokemon.attack == BodyPart.NOTHING
        assert pokemon.state == State.READY

    def test_str(self):
        pokemon = Pokemon(name=self.name, pokemon_type=self.pokemon_type)

        assert str(pokemon) == f"Name: {self.name} | Type: {self.pokemon_type}\n" \
                               f"Level: 0 | HP: 100\n" \
                               f"State: {State.READY}"
