from pokemon_combat.pokemon import Pokemon, Gender


def test_init():
    name = "Pika"
    gender = Gender.MALE
    pokemon = Pokemon(name=name, gender=gender)
    assert pokemon.name == name
    assert pokemon.gender == gender
    assert pokemon.level == 0


def test_str():
    name = "Pika"
    gender = Gender.MALE
    pokemon = Pokemon(name=name, gender=gender)

    assert str(pokemon) == f"Name: {name} | Gender: {gender} | Level: 0"
