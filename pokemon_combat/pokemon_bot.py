from random import randint
import random
from pokemon_combat.pokemon import Pokemon
from pokemon_combat.pokemon_by_type import pokemon_by_type
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.body_part import BodyPart


class PokemonBot(Pokemon):
    def __init__(self):

        # пытаться получить покемона не более 100 раз (если будет не найти покемонов определенного типа)
        max_errors = 100
        error_counter = 0
        while True:
            try:
                pokemon_type_rand = PokemonType(randint(PokemonType.min_index(), PokemonType.max_index()))
                bot_pokemon_name = random.choice(list(pokemon_by_type[pokemon_type_rand].keys()))
            except Exception as ex:
                print(ex)
                error_counter += 1

                if error_counter > max_errors:
                    print("Can't create PokemonBot object!")
                    raise RuntimeError("Can't create PokemonBot object!")
            else:
                super().__init__(name=bot_pokemon_name,
                                 pokemon_type=pokemon_type_rand)
                break

    def next_step(self):
        defence_body_part_rand = BodyPart(randint(BodyPart.min_index(), BodyPart.max_index()))
        attack_body_part_rand = BodyPart(randint(BodyPart.min_index(), BodyPart.max_index()))
        super().next_step(defense_body_part=defence_body_part_rand,
                          attack_body_part=attack_body_part_rand)
