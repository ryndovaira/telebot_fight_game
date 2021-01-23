from pokemon_combat.ice_pokemon import IcePokemon
from pokemon_combat.pokemon import Gender
from pokemon_combat.pokemon_types import PokemonType


def test_init():
    name = "Glalie"
    gender = Gender.FEMALE
    pokemon = IcePokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.weakness == (PokemonType.FIRE, PokemonType.STEEL, PokemonType.FIGHTING, PokemonType.ROCK)


def test_str():
    name = "Glalie"
    gender = Gender.MALE
    pokemon = IcePokemon(name=name, gender=gender)

    assert str(pokemon) == f"Type: Fire | Name: {name} | Gender: {gender} | Level: 0 | HP: 100"
