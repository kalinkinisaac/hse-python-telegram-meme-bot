from config import config
import telebot
from meme_generator import generate_meme
import requests
from telebot import types
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.AsyncTeleBot(config['TELEGRAM']['token'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_button = types.KeyboardButton('/meme')
    markup.add(item_button)
    bot.send_message(message.chat.id, ".", reply_markup=markup)
    bot.send_message(message.chat.id, "Type /meme to get a new meme")


@bot.message_handler(commands=['meme'])
def echo_all(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    meme_title, meme_url = generate_meme()
    meme_image = requests.get(meme_url).content
    # bot.send_message(message.chat.id, meme_title)
    bot.send_photo(
        message.chat.id,
        meme_image,
        meme_title
    )
