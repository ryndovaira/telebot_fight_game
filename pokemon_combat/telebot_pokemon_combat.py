import configparser
import telebot
from telebot import types

config = configparser.ConfigParser()
config.read('telebot_config.ini')
token = config['telebot']['token']
bot = telebot.TeleBot(token)    # @My_very_long_username_bot


@bot.message_handler(commands=['start'])
def new_member(message):
    bot.send_message(message.from_user.id, f'Hi, {message.from_user.first_name}!')


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling(none_stop=True, interval=0)
