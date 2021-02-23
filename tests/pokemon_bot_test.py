import random

from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon_bot import PokemonBot

from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.pokemon_state import State
from pokemon_combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses


class TestPokemonBotClass:
    bot_name = 'Gigalith'  # при seed(0)
    pokemon_type = PokemonType.ROCK  # при seed(0)

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        random.seed(0)

    def test_init(self):
        pokemon_bot = PokemonBot()

        assert pokemon_bot.name == self.bot_name
        assert pokemon_bot.type == self.pokemon_type
        assert pokemon_bot.defence_weaknesses == weaknesses[self.pokemon_type]
        assert pokemon_bot.hp == 100
        assert pokemon_bot.defense == BodyPart.NOTHING
        assert pokemon_bot.attack == BodyPart.NOTHING
        assert pokemon_bot.state == State.READY

    def test_str(self):
        pokemon = PokemonBot()

        assert str(pokemon) == f"Name: {self.bot_name} | Type: {self.pokemon_type}\n" \
                               f"HP: 100\n" \
                               f"State: {State.READY}"
