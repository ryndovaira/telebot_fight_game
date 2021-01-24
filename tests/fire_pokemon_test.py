from pokemon_combat.gender import Gender
from pokemon_combat.state import State
from pokemon_combat.pokemon_types import PokemonType
from pokemon_combat.fire_pokemon import FirePokemon


def test_init():
    name = "Charmander"
    gender = Gender.MALE
    pokemon = FirePokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.state == State.INIT
    assert pokemon.weakness == (PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK)


def test_str():
    name = "Charmander"
    gender = Gender.MALE
    pokemon = FirePokemon(name=name, gender=gender)

    assert str(pokemon) == f"Type: Fire | Name: {name} | Gender: {gender} | Level: 0 | HP: 100"
