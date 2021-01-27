from pokemon_combat.pokemon_type import PokemonType

pokemon_defence_weaknesses_by_type = {
    # https://pokemondb.net/type/normal
    PokemonType.NORMAL: (PokemonType.FIGHTING,),

    # https://pokemondb.net/type/fire
    PokemonType.FIRE: (PokemonType.WATER,
                       PokemonType.GROUND,
                       PokemonType.ROCK),

    # https://pokemondb.net/type/water
    PokemonType.WATER: (PokemonType.ELECTRIC,
                        PokemonType.GROUND),

    # https://pokemondb.net/type/electric
    PokemonType.ELECTRIC: (PokemonType.GROUND,),

    # https://pokemondb.net/type/grass
    PokemonType.GRASS: (PokemonType.FIRE,
                        PokemonType.ICE,
                        PokemonType.POISON,
                        PokemonType.FLYING,
                        PokemonType.BUG),

    # https://pokemondb.net/type/ice
    PokemonType.ICE: (PokemonType.FIRE,
                      PokemonType.FIGHTING,
                      PokemonType.ROCK,
                      PokemonType.STEEL),

    # https://pokemondb.net/type/fighting
    PokemonType.FIGHTING: (PokemonType.FLYING,
                           PokemonType.PSYCHIC,
                           PokemonType.FAIRY),

    # https://pokemondb.net/type/poison
    PokemonType.POISON: (PokemonType.GROUND,
                         PokemonType.PSYCHIC),

    # https://pokemondb.net/type/ground
    PokemonType.GROUND: (PokemonType.WATER,
                         PokemonType.GRASS,
                         PokemonType.ICE),

    # https://pokemondb.net/type/flying
    PokemonType.FLYING: (PokemonType.ELECTRIC,
                         PokemonType.ICE,
                         PokemonType.ROCK),

    # https://pokemondb.net/type/psychic
    PokemonType.PSYCHIC: (PokemonType.BUG,
                          PokemonType.GHOST,
                          PokemonType.DARK),

    # https://pokemondb.net/type/bug
    PokemonType.BUG: (PokemonType.FIRE,
                      PokemonType.FLYING,
                      PokemonType.ROCK),

    # https://pokemondb.net/type/rock
    PokemonType.ROCK: (PokemonType.WATER,
                       PokemonType.GRASS,
                       PokemonType.FIGHTING,
                       PokemonType.GROUND,
                       PokemonType.STEEL),

    # https://pokemondb.net/type/ghost
    PokemonType.GHOST: (PokemonType.GHOST,
                        PokemonType.DARK),

    # https://pokemondb.net/type/dragon
    PokemonType.DRAGON: (PokemonType.ICE,
                         PokemonType.DRAGON,
                         PokemonType.FAIRY),

    # https://pokemondb.net/type/dark
    PokemonType.DARK: (PokemonType.FIGHTING,
                       PokemonType.BUG,
                       PokemonType.FAIRY),

    # https://pokemondb.net/type/steel
    PokemonType.STEEL: (PokemonType.FIRE,
                        PokemonType.FIGHTING,
                        PokemonType.GROUND),

    # https://pokemondb.net/type/fairy
    PokemonType.FAIRY: (PokemonType.POISON,
                        PokemonType.STEEL)
}
