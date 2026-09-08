import openai
import google.generativeai as genai
from config import DEEPSEEK_API_KEY, GEMINI_API_KEY

# --- 1. НАСТРОЙКА DEEPSEEK (основной) ---
deepseek_client = openai.OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

# --- 2. НАСТРОЙКА GEMINI (запасной) ---
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.0-flash")
else:
    gemini_model = None

def generate_joke():
    """
    Генерирует циничную IT-шутку.
    Сначала пробует DeepSeek, если он не доступен — Gemini.
    """
    prompt = """
    Напиши короткую, циничную и смешную IT-шутку в стиле "Сеньор на галере".
    Тема: Python, разработка, баги, дедлайны, легаси-код.
    """

    # --- СНАЧАЛА ПРОБУЕМ DEEPSEEK ---
    try:
        response = deepseek_client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Ты — циничный IT-блогер."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"[⚠️] DeepSeek не ответил: {e}. Пробуем Gemini...")
        
        # --- ЕСЛИ DEEPSEEK НЕ РАБОТАЕТ, ПРОБУЕМ GEMINI ---
        if gemini_model:
            try:
                response = gemini_model.generate_content(prompt)
                return response.text.strip()
            except Exception as e2:
                print(f"[❌] Ошибка Gemini: {e2}")
                return "Сегодня без шуток. Сервер упал."

if __name__ == "__main__":
    print(generate_joke())