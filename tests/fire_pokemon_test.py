from pokemon_combat.fire_pokemon import FirePokemon
from pokemon_combat.pokemon import Gender
from pokemon_combat.pokemon_types import PokemonType


def test_init():
    name = "Charmander"
    gender = Gender.MALE
    pokemon = FirePokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0
    assert pokemon.weakness == (PokemonType.WATER, )
    assert pokemon.strength == (PokemonType.ICE, PokemonType.GROUND, PokemonType.ROCK)


def test_str():
    name = "Charmander"
    gender = Gender.MALE
    pokemon = FirePokemon(name=name, gender=gender)

    assert str(pokemon) == f"Type: Fire | Name: {name} | Gender: {gender} | Level: 0"
