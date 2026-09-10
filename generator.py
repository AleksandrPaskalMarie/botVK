from gigachat import GigaChat
from config import GIGACHAT_AUTH_KEY

def generate_joke():
    """
    Генерирует циничную IT-шутку через GigaChat.
    """
    prompt = """
    Напиши короткую (2-3 предложения), циничную и смешную IT-шутку.
    Стиль: как у "Сеньор на галере" — с сарказмом, про Python, разработку, баги или дедлайны.
    Не используй смайлики.
    """
    
    # ЯВНО УКАЗЫВАЕМ МОДЕЛЬ
    with GigaChat(
        credentials=GIGACHAT_AUTH_KEY,
        model="GigaChat-2",              # ← ДОБАВЬ ЭТУ СТРОЧКУ
        verify_ssl_certs=False
    ) as client:
        response = client.chat(prompt)
        return response.choices[0].message.content

if __name__ == "__main__":
    print(generate_joke())