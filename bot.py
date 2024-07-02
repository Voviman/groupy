import telebot
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

import app

TOKEN = "941800361:AAHYJTfLPHPFqsT6cA42L_g_0OeDsu0Yvck"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message, client):
	app.club(message=message, client=client)




if __name__ == '__main__':
	bot.polling()