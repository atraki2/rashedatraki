import os
os.system('pip install pytelegrambotapi')
import telebot

# Replace with your bot token
TOKEN = '7790340259:AAGfKIrZ8EC0tcW5ZBrtXuC9kY8B3tdm2H0'

bot = telebot.TeleBot(TOKEN)

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من بات تلگرام شما هستم 🤖")

# Text message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"گفتی: {message.text}")

# Start polling (keep the bot running)
bot.polling()
