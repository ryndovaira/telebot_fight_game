from pokemon_combat.gender import Gender
from pokemon_combat.state import State
from pokemon_combat.pokemon import Pokemon


def test_init():
    name = "Pika"
    gender = Gender.MALE
    pokemon = Pokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.state == State.INIT


def test_str():
    name = "Pika"
    gender = Gender.MALE
    pokemon = Pokemon(name=name, gender=gender)

    assert str(pokemon) == f"Name: {name} | Gender: {gender} | Level: 0 | HP: 100"
