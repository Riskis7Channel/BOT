#botreplypesan
#riskis7

import telebot

API_TOKEN = '< YOUR API KEY >'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, "Pesan balasan")

bot.polling()


#-1001191378446
