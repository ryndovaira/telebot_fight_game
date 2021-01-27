import configparser
import telebot
from telebot import types

from pokemon_combat.pokemon_type import PokemonType

config = configparser.ConfigParser()
config.read('telebot_config.ini')
token = config['telebot']['token']
bot = telebot.TeleBot(token)  # @My_very_long_username_bot

# {user_id: {'user_pokemon': pokemon_obj, 'rand_pokemon': rand_player_obj}}
bot_state = {}

hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def new_member(message):
    bot.send_message(message.from_user.id, f'Hi, {message.from_user.first_name}!')

    yes_no_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True,
                                                row_width=2)
    yes_no_keyboard.row("Да", "Нет")
    bot.send_message(message.chat.id,
                     "Do you want to start the game?",
                     reply_markup=yes_no_keyboard)

    bot.register_next_step_handler(message, start_game)


def start_game(message):
    if message.text == 'Да':
        pokemon_markup = types.InlineKeyboardMarkup()
        for pokemon_type in PokemonType:
            pokemon_markup.add(types.InlineKeyboardButton(text=pokemon_type.name,
                                                          callback_data=f"pokemon_type_{pokemon_type.value}"))
        bot.send_message(message.chat.id,
                         "Choose a pokemon type:",
                         reply_markup=pokemon_markup)

    elif message.text == 'Нет':
        bot.send_message(message.chat.id,
                         "Ok, I'll wait!",
                         reply_markup=hideBoard)
    else:
        bot.send_message(message.chat.id,
                         "You must choose option on keyboard")

    bot.register_next_step_handler(message, start_game)


# True можно заменить на любое логическое условие (можно использовать данные из объекта call)
@bot.callback_query_handler(func=lambda call: "pokemon_type_" in call.data)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id,
                              text='You choose a type!')
    ...


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    ...


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling(none_stop=True, interval=0)
