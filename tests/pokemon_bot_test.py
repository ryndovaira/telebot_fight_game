from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon_bot import PokemonBot

import random

from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.state import State
from pokemon_combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses


def test_init():
    random.seed(0)

    bot_name = 'Bot'  # TODO: заменить на случаное имя при seed(0)
    pokemon_type = PokemonType.ROCK  # при seed(0)
    pokemon_bot = PokemonBot()
    assert pokemon_bot.name == bot_name
    assert pokemon_bot.type == pokemon_type
    assert pokemon_bot.defence_weaknesses == weaknesses[pokemon_type]
    assert pokemon_bot.level == 0
    assert pokemon_bot.hp == 100
    assert pokemon_bot.defense == BodyPart.NOTHING
    assert pokemon_bot.attack == BodyPart.NOTHING
    assert pokemon_bot.state == State.READY
