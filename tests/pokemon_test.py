from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses

from pokemon_combat.pokemon import Pokemon


def test_init():
    name = "Pika"
    pokemon_type = PokemonType.ELECTRIC
    pokemon = Pokemon(name=name, pokemon_type=pokemon_type)
    assert pokemon.name == name
    assert pokemon.type == pokemon_type
    assert pokemon.defence_weaknesses == weaknesses[pokemon_type]
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.defense == BodyPart.NOTHING
    assert pokemon.attack == BodyPart.NOTHING


def test_str():
    name = "Pika"
    pokemon_type = PokemonType.ELECTRIC

    pokemon = Pokemon(name=name, pokemon_type=pokemon_type)

    assert str(pokemon) == f"Name: {name} | Type: {pokemon_type} | Level: 0 | HP: 100"
