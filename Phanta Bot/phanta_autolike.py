import vk
import time
import random
from datetime import datetime

access_token = "f7b958ffe523f083da4d724c4784d12752c87491a761ce8aa9c3bcf39c2b4e506cf1bf597593c898603f0" # API_KEY

last_post = 62580

def init(access_token, last_post):
    print("Запуск скрипта. Иницилизация входа...")
    session = vk.Session(access_token=access_token)
    api = vk.API(session, v='5.95')
    last_post=last_post
    print("Скрипт успешно запущен.")
    api.messages.send(random_id=random.randint(1,100000),peer_id=2000000337, message="Скрипт успешно запущен.")
    main(api, last_post)
    
def main(api, last_post):
    while True:
        time.sleep(60)
        response = api.wall.get(owner_id=-183503775, offset=1, count=1)
        print("\n" +    str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")))
        print(last_post)
        for _wall in response['items']:
            if _wall['id'] > last_post:
                print("Обнаружен новый пост. Ожидаю одну минуту...")
                time.sleep(60)
                api.likes.add(type="post", owner_id=-183503775, item_id=_wall['id'])
                api.messages.send(random_id=random.randint(1,100000),peer_id=2000000337, message="Новый пост был лайкнут. Советую оставить комментарий.")
                last_post = _wall['id']
                print("\nНовый пост был лайкнут.")
                print(last_post)
            

try:
    init(access_token, last_post)
except:
    init(access_token, last_post)