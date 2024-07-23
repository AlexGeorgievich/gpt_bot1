from dotenv import load_dotenv
import os
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

# Список для хранения истории разговора
conversation_history = []
def chat_with_ai(intial_message="Hello my friend"):

    conversation_history.append({"role": "user", "content": intial_message})
    while True:
        # Отправка запроса в нейронную сеть
        chat_completion = client.chat.completions.create(
            # model="gpt-4o",
            model="gpt-3.5-turbo-1106",
            messages=conversation_history
        )

        # Извлечение и вывод ответа нейронной сети
        ai_response_content = chat_completion.choices[
            0].message.content  # Предполагаемый правильный способ доступа к содержимому ответа
        print("AI:", ai_response_content)

        # Запрос ввода пользователя
        user_input = input("Вы: ")

        # Опционально: условие для выхода из цикла (например, если пользователь ввел 'exit')
        if user_input.lower() == 'exit':
            break

        # Добавление ввода пользователя в историю разговора
        conversation_history.append({"role": "user", "content": user_input})

        # Добавление ответа нейронной сети в историю разговора
        conversation_history.append({"role": "system", "content": ai_response_content})

chat_with_ai("Привет! ")