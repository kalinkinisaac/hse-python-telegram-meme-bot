from config import config
import telebot
from content_generator import generate_content
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
    bot.send_message(message.chat.id,
                     "Type /meme to get a new meme, or a keyword for search",
                     reply_markup=markup)


@bot.message_handler(commands=['meme'])
def meme(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    meme_title, meme_url = generate_content(subreddit='memes')
    bot.send_photo(
        message.chat.id,
        meme_url,
        meme_title
    )


@bot.message_handler(content_types=['text'])
def content_by_keyword(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    content = generate_content(keyword=message.text)
    if content:
        title, url = generate_content(keyword=message.text)
        bot.send_photo(
            message.chat.id,
            url,
            title
        )
    else:
        bot.send_message(message.chat.id,
                         'Failed to find content. Try another request')
