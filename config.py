import os
from dotenv import load_dotenv

# 1. Загружаем переменные из файла .env в переменные окружения
load_dotenv()

# 2. Забираем значения из окружения и сохраняем в переменные Python
VK_TOKEN = os.getenv("VK_TOKEN")
VK_GROUP_ID = os.getenv("VK_GROUP_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")