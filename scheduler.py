import schedule
import time
from generator import generate_joke
from publisher import post_to_vk

def job():
    print("[⏳] Генерирую шутку...")
    joke = generate_joke()
    print("[📤] Отправляю в VK...")
    post_to_vk(joke)
    print("[✅] Задача выполнена!")

schedule.every().day.at("10:00").do(job)

if __name__ == "__main__":
    print("[⏳] Бот запущен и ждёт расписания...")
    while True:
        schedule.run_pending()
        time.sleep(60)