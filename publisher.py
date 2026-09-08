import vk_api
from config import VK_TOKEN, VK_GROUP_ID

def post_to_vk(text):
    """
    Публикует переданный текст на стене группы VK.
    """
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    vk.wall.post(
        owner_id=VK_GROUP_ID,
        message=text,
        from_group=1
    )
    print("[✅] Пост опубликован!")

# Для проверки, если запустить этот файл напрямую
if __name__ == "__main__":
    test_text = "Тестовый пост! Бот работает!"
    post_to_vk(test_text)