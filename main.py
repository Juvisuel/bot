
import pyTelegramBotAPI

main_url = f'https:api.telegram.org/bot{5512357481:AAGfWTAy0h9A8AUSGOqHZ-mNYK1JsKV38DM}'

bot = telebot.TeleBot('5512357481:AAGfWTAy0h9A8AUSGOqHZ-mNYK1JsKV38DM')

bot.get_me
#
# @bot.message_handler(content_types ='text')
# def simple_ansver(message):
#     text = message.text
#     bot.reply_to(message, text)




bot.poll()
