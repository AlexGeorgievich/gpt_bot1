# gpt_bot
Учебный проект по освоению взаимодействия с OpenAI, Telegram
### bot_telegram
Чат бот для общения с Telegram в simple виде,
команды /start -перезапуск, /help- справка, /revers - переворот сообщения в строке после команды /revers

### bot01.py , bot02.py
Чат бот работает в режиме терминала , для подключению к ChatGPT  необходимо пройти регистрацию
и получить ключ API , в корне пакета в файле .env в формате TOKEN_GPT = os.getenv("TOKEN_GPT")
BASE_URL = os.getenv("BASE_URL") хранятся ключ и url доступа к модели  model="gpt-3.5-turbo-1106".
