from pokemon_combat.gender import Gender
from pokemon_combat.state import State
from pokemon_combat.pokemon_type import PokemonType

from pokemon_combat.pokemon import Pokemon


def test_init():
    name = "Pika"
    gender = Gender.MALE
    pokemon_type = PokemonType.ELECTRIC
    pokemon = Pokemon(name=name, gender=gender, pokemon_type=pokemon_type)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.type == pokemon_type
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.state == State.INIT


def test_str():
    name = "Pika"
    gender = Gender.MALE
    pokemon_type = PokemonType.ELECTRIC

    pokemon = Pokemon(name=name, gender=gender, pokemon_type=pokemon_type)

    assert str(pokemon) == f"Name: {name} | Type: {pokemon_type} | Gender: {gender} | Level: 0 | HP: 100"
