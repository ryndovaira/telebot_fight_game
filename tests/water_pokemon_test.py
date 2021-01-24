from pokemon_combat.gender import Gender
from pokemon_combat.water_pokemon import WaterPokemon
from pokemon_combat.pokemon_types import PokemonType


def test_init():
    name = "Squirtle"
    gender = Gender.FEMALE
    pokemon = WaterPokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0
    assert pokemon.hp == 100
    assert pokemon.weakness == (PokemonType.ELECTRIC, PokemonType.GRASS)


def test_str():
    name = "Squirtle"
    gender = Gender.MALE
    pokemon = WaterPokemon(name=name, gender=gender)

    assert str(pokemon) == f"Type: Water | Name: {name} | Gender: {gender} | Level: 0 | HP: 100"
