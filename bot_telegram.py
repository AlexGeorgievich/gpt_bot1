import telebot
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")

# Замените 'your_token' на токен вашего бота
bot = telebot.TeleBot(TOKEN_BOT)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот. Введите /help для получения списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Список команд:\n/start - Начать общение\n/help - Получить список команд\n/revers - Инвертировать текст")

@bot.message_handler(commands=['revers'])
def handle_revers(message):
    # if len(message.text.split()) < 2:
    #     bot.reply_to(message, "Введите текст после команды /revers для инвертирования.")
    # else:
    #     text = ' '.join(message.text.split()[1:])[::-1]
    #     bot.reply_to(message, f"Инвертированный текст: {text}")
    original_text = message.text[len("/revers "):]
    reversed_text = original_text[::-1]
    bot.send_message(message.chat.id, reversed_text)

bot.polling()