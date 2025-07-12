import telebot

bot = telebot.TeleBot('7790340259:AAGfKIrZ8EC0tcW5ZBrtXuC9kY8B3tdm2H0')

@bot.message_handler(['start'])
def send_start(message):
bot.reply_to(message, 'hello man')
bot.polling()

