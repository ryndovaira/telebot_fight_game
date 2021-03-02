import configparser
import os
import pickle
import logging

# pip install pyTelegramBotAPI
import telebot
from telebot import types

from pokemon_combat.body_part import BodyPart
from pokemon_combat.pokemon import Pokemon
from pokemon_combat.pokemon_bot import PokemonBot
from pokemon_combat.pokemon_by_type import pokemon_by_type
from pokemon_combat.pokemon_type import PokemonType
from pokemon_combat.pokemon_state import State
from pokemon_combat.game_result import GameResult

# прочитать Токен из конфига
config = configparser.ConfigParser()
config.read('telebot_config.ini')
token = config['telebot']['token']
bot = telebot.TeleBot(token)  # @My_very_long_username_bot

# {user_id: {'user_pokemon': pokemon_obj, 'rand_pokemon': rand_player_obj}}
bot_state = {}

# {user_id: {'wins': 0, 'losses': 0, 'standoff': 0}}
game_statistics = {}

hideBoard = types.ReplyKeyboardRemove()

# полный путь к файлу для статистики игр
game_statistics_filename = 'game_statistics.pkl'


def load_statistics():
    logging.info('Try to load statistics.')

    global game_statistics

    try:
        with open(game_statistics_filename, 'rb') as game_statistics_file:
            game_statistics = pickle.load(game_statistics_file)
    except FileNotFoundError:
        logging.warning(f"File {game_statistics_filename} not found!")
    else:
        logging.info('Success!')


def update_and_save_statistics(user_id, result: GameResult):
    global game_statistics

    if game_statistics.get(user_id) is None:
        game_statistics[user_id] = {}

    if result is GameResult.WIN:
        game_statistics[user_id]['wins'] = game_statistics[user_id].get('wins', 0) + 1
    elif result is GameResult.LOSE:
        game_statistics[user_id]['losses'] = game_statistics[user_id].get('losses', 0) + 1
    elif result is GameResult.STANDOFF:
        game_statistics[user_id]['standoff'] = game_statistics[user_id].get('standoff', 0) + 1

    # сохранять в историю только результаты (без прогресса)
    with open(game_statistics_filename, 'wb') as game_statistics_file:
        pickle.dump(game_statistics, game_statistics_file)


@bot.message_handler(commands=['results'])
def print_stats(message):
    user_results = game_statistics.get(message.chat.id)
    if user_results:
        user_results_str = ""
        for res_type, res_count in user_results.items():
            user_results_str += f"\n    {res_type}: {res_count}"
    else:
        user_results_str = "\n    (empty)"
    bot.send_message(message.chat.id, f'You results:{user_results_str}')


@bot.message_handler(commands=['start'])
def new_game(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}!')

    yes_no_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True,
                                                row_width=2)
    yes_no_keyboard.row("Yes", "No")
    bot.send_message(message.chat.id,
                     "Do you want to start the game?",
                     reply_markup=yes_no_keyboard)

    bot.register_next_step_handler(message, start_game_answer)


def start_game_answer(message):
    if message.text == 'Yes':
        try:
            create_bot_pokemon(message)
        except Exception as ex:
            # Emoji https://apps.timwhitlock.info/emoji/tables/unicode
            bot.send_message(message.chat.id,
                             f"Error: {ex}\t\U0001F631\n"
                             f"Sorry!\n"
                             f"We'll fix it!\n"
                             f"\U0000274CThe game is unavailable!\U0000274C")
        else:
            start_game(message)

    elif message.text == 'No':
        bot.send_message(message.chat.id,
                         "Ok, I'll wait!",
                         reply_markup=hideBoard)
    else:
        bot.send_message(message.chat.id,
                         "You must choose option on keyboard")


def start_game(message, fail_pokemon_type=None, fail_pokemon_type_list=[]):
    if fail_pokemon_type:
        fail_pokemon_type_list.append(fail_pokemon_type)

    pokemon_markup_buttons = []
    pokemon_markup_buttons_row = []
    row_helper = 1
    row_button_size = 3

    for pokemon_type in PokemonType:
        if pokemon_type in fail_pokemon_type_list:
            continue

        pokemon_markup_buttons_row.append(types.InlineKeyboardButton(text=pokemon_type.name,
                                                                     callback_data=f"pokemon_type_{pokemon_type.value}"))

        if row_helper % row_button_size == 0:
            pokemon_markup_buttons.append(pokemon_markup_buttons_row)
            pokemon_markup_buttons_row = []

        row_helper += 1

    if pokemon_markup_buttons_row:
        pokemon_markup_buttons.append(pokemon_markup_buttons_row)

    pokemon_markup = types.InlineKeyboardMarkup(pokemon_markup_buttons)
    bot.send_message(message.chat.id,
                     "Choose a pokemon type:",
                     reply_markup=pokemon_markup)


def create_bot_pokemon(message):
    global bot_state
    # {user_id: {'user_pokemon': pokemon_obj, 'rand_pokemon': rand_player_obj}}

    random_pokemon = PokemonBot()

    bot_state[message.chat.id] = {'rand_pokemon': random_pokemon}

    bot.send_message(message.chat.id,
                     f"<b>Bot's choose</b>\n{bot_state[message.chat.id]['rand_pokemon']}",
                     parse_mode='html')

    random_pokemon_img = pokemon_by_type[random_pokemon.type][random_pokemon.name]
    img = open(f"../images/{random_pokemon_img}", 'rb')
    bot.send_photo(message.chat.id, img)


@bot.callback_query_handler(func=lambda call: "pokemon_type_" in call.data)
def query_handler(call):
    call_data_split = call.data.split('_')
    if len(call_data_split) < 2 or not call_data_split[2].isdigit():
        bot.send_message(call.message.chat.id,
                         "Sorry, something wrong!\nPlease reset session /start")
    else:
        pokemon_type_id = int(call_data_split[2])
        bot.answer_callback_query(callback_query_id=call.id,
                                  text="Let's choose your pokemon!")

        bot.send_message(call.message.chat.id,
                         "Choose a pokemon:")

        ask_to_chose_pokemon_by_typeid(pokemon_type_id, call.message)


def ask_to_chose_pokemon_by_typeid(pokemon_type_id, message):
    chosen_pokemon_type = PokemonType(pokemon_type_id)
    pokemons_with_chosen_type = pokemon_by_type.get(chosen_pokemon_type)

    if pokemons_with_chosen_type:
        for pokemon_name, pokemon_img in pokemons_with_chosen_type.items():
            img_file_path = f"../images/{pokemon_img}"
            if os.path.isfile(img_file_path):
                img = open(img_file_path, 'rb')
                pokemon_markup = types.InlineKeyboardMarkup(
                    keyboard=[[types.InlineKeyboardButton(
                        text=pokemon_name,
                        callback_data=f"pokemon_name_{pokemon_name}_{pokemon_type_id}")]]
                )
                bot.send_photo(message.chat.id, img, reply_markup=pokemon_markup)
            else:
                logging.error(f"File {img_file_path} doesn't exist!")
    else:
        bot.send_message(message.chat.id,
                         'Sorry, there is no pokemon in this type!\nPlease, choose something else.')
        start_game(message, fail_pokemon_type=chosen_pokemon_type)


@bot.callback_query_handler(func=lambda call: "pokemon_name_" in call.data)
def query_handler(call):
    call_data_split = call.data.split('_')
    if len(call_data_split) < 3 or not call_data_split[3].isdigit():
        bot.send_message(call.message.chat.id,
                         "Sorry, something wrong!\nPlease reset session /start")
    else:
        bot.answer_callback_query(callback_query_id=call.id,
                                  text="Pokemon has chosen!")
        pokemon_name, pokemon_type_id = call_data_split[2], int(call_data_split[3])

        create_user_pokemon(call.message, pokemon_name=pokemon_name,
                            pokemon_type=PokemonType(pokemon_type_id))


def create_user_pokemon(message, pokemon_name: str, pokemon_type: PokemonType):
    global bot_state

    bot_state[message.chat.id].update({'user_pokemon': Pokemon(name=pokemon_name,
                                                               pokemon_type=pokemon_type)})

    bot.send_message(message.chat.id,
                     f"<b>Your choose</b>\n{bot_state[message.chat.id]['user_pokemon']}",
                     parse_mode='html')
    bot.send_message(message.chat.id, "Starting game...")
    game_next_step_defend(message)


def game_next_step_defend(message):
    body_part_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
    body_part_keyboard.row(*[types.KeyboardButton(body_part.name) for body_part in BodyPart])

    bot.send_message(message.chat.id,
                     "What pokemon's body part do you want to defend?",
                     reply_markup=body_part_keyboard)

    bot.register_next_step_handler(message, game_get_defend_answer_and_next_step_attack)


def game_get_defend_answer_and_next_step_attack(message):
    if not BodyPart.has_item(message.text):
        bot.send_message(message.chat.id,
                         "You should use keyboard for an answer!")
        game_next_step_defend(message)
    else:
        next_step_attack(message, defenced_body_part=message.text)


def next_step_attack(message, defenced_body_part: str):
    body_part_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
    body_part_keyboard.row(*[types.KeyboardButton(body_part.name) for body_part in BodyPart])

    bot.send_message(message.chat.id,
                     "What pokemon's body part do you want to attack?",
                     reply_markup=body_part_keyboard)

    bot.register_next_step_handler(message, game_next_step, defenced_body_part=defenced_body_part)


def game_next_step(message, defenced_body_part: str):
    if not BodyPart.has_item(message.text):
        bot.send_message(message.chat.id,
                         "You should use keyboard for an answer!")
        next_step_attack(message, defenced_body_part=defenced_body_part)
    else:
        attack_body_part = message.text

        global bot_state
        user_pokemon = bot_state[message.chat.id]['user_pokemon']
        rand_pokemon = bot_state[message.chat.id]['rand_pokemon']

        user_pokemon.next_step(defense_body_part=BodyPart[defenced_body_part],
                               attack_body_part=BodyPart[attack_body_part])
        rand_pokemon.next_step()

        # player's pokemon is always the first attacker
        rand_pokemon_hit_comments = rand_pokemon.get_hit(opponent_attack_body_part=user_pokemon.attack,
                                                         opponent_hit_power=user_pokemon.hit_power,
                                                         opponent_type=user_pokemon.type)
        bot.send_message(message.chat.id, f"<b>Bot's pokemon</b>:\n{rand_pokemon_hit_comments}", parse_mode='html')

        user_pokemon_hit_comments = user_pokemon.get_hit(opponent_attack_body_part=rand_pokemon.attack,
                                                         opponent_hit_power=rand_pokemon.hit_power,
                                                         opponent_type=user_pokemon.type)
        bot.send_message(message.chat.id, f"<b>Your pokemon</b>:\n{user_pokemon_hit_comments}", parse_mode='html')

        check_players_state(user_pokemon, rand_pokemon, message)


def check_players_state(user_pokemon, rand_pokemon, message):
    commands_str = "\n\n/start for a new game\n/results for your results"
    if user_pokemon.state != State.READY and rand_pokemon.state == State.READY:
        bot.send_message(message.chat.id, f"\U0001F44EYou lose...{commands_str}")
        update_and_save_statistics(message.chat.id, GameResult.LOSE)

    elif user_pokemon.state == State.READY and rand_pokemon.state != State.READY:
        bot.send_message(message.chat.id, f"\U0001F44DYou win!{commands_str}")
        update_and_save_statistics(message.chat.id, GameResult.WIN)

    elif user_pokemon.state != State.READY and rand_pokemon.state != State.READY:
        bot.send_message(message.chat.id, f"\U0001F91DStandoff!{commands_str}")
        update_and_save_statistics(message.chat.id, GameResult.STANDOFF)

    elif user_pokemon.state == State.READY and rand_pokemon.state == State.READY:
        game_next_step_defend(message)


if __name__ == '__main__':
    # настройка логирования
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    load_statistics()

    logging.info('Starting the bot...')
    bot.polling(none_stop=True, interval=0)
    logging.info('The bot has stopped!')
