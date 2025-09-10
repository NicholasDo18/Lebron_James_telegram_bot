import os
import random
import telebot 

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

leQuotes = ["I like criticism. It makes you strong.",
"I think, team first. It allows me to succeed, it allows my team to succeed.",
"Don’t be afraid of failure. This is the way to succeed.",
"Commitment is a big part of what I am and what I believe. How committed are you to winning?",
"I always say, decisions I make, I live with them. There’s always ways you can correct them or ways you can do them better.",
"You can’t be afraid to fail. It’s the only way you succeed."]

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "King James said Hi")

@bot.message_handler(commands = ['Motivational-quote'])
def send_welcome(message):
    bot.reply_to(message, random.choice(leQuotes))

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()