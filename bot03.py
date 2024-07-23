import os
from dotenv import load_dotenv
import telebot
from openai import OpenAI

# Загрузка переменных окружения из файла .env
load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")
TOKEN_GPT = os.getenv("TOKEN_GPT")
BASE_URL = os.getenv("BASE_URL")

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key=TOKEN_GPT,
    base_url=BASE_URL,
)

# Инициализация бота
bot = telebot.TeleBot(TOKEN_BOT)

# Список для хранения истории разговора
conversation_history = []

def get_ai_response(user_input):
    # Добавление ввода пользователя в историю разговора
    conversation_history.append({"role": "user", "content": user_input})

    # Отправка запроса в нейронную сеть
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history
    )

    # Извлечение и вывод ответа нейронной сети
    ai_response_content = chat_completion.choices[0].message.content

    # Добавление ответа нейронной сети в историю разговора
    conversation_history.append({"role": "system", "content": ai_response_content})

    return ai_response_content

@bot.message_handler(commands=['start'])
def send_welcome(message):
    help_message = ("Привет! Я бот, который может отвечать на любые вопросы с помощью нейронной сети.\n\n"
                    "Доступные команды:\n"
                    "/start - Начать работу с ботом\n"
                    "/help - Показать это сообщение\n\n"
                    "Просто задайте мне любой вопрос, и я постараюсь ответить.")
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    help_message = ( "Теперь ваш Telegram - бот будет отвечать на любые вопросы с помощью нейронной сети OpenAI.\n"
    "Пользователи могут отправлять сообщения боту, и он будет отвечать, используя модель GPT - 3.5."
                    "Доступные команды:\n"
                    "/start - Начать работу с ботом\n"
                    "/help - Показать это сообщение\n\n"
                    "Просто задайте мне любой вопрос, и я постараюсь ответить.")
    bot.reply_to(message, help_message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_input = message.text
    ai_response = get_ai_response(user_input)
    bot.reply_to(message, ai_response)

# Запуск бота
bot.polling()

if __name__ == "__main__":
    print("Бот запущен и готов к работе!")