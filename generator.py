from gigachat import GigaChat
from config import GIGACHAT_AUTH_KEY
from prompts import get_random_prompt

def generate_joke():
    """
    Генерирует циничную IT-шутку через GigaChat.
    Использует случайный промпт из prompts.py.
    """
    prompt = get_random_prompt()

    with GigaChat(
        credentials=GIGACHAT_AUTH_KEY,
        model="GigaChat-2",
        verify_ssl_certs=False
    ) as client:
        response = client.chat(prompt)
        return response.choices[0].message.content

if __name__ == "__main__":
    print(generate_joke())