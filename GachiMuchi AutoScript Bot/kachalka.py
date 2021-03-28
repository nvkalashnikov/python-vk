import vk
import time
import random

access_token = "f7b958ffe523f083da4d724c4784d12752c87491a761ce8aa9c3bcf39c2b4e506cf1bf597593c898603f0" # API_KEY
session = vk.Session(access_token=access_token)
api = vk.API(session, v='5.95')
kochka = False

def init(access_token):
    session = vk.Session(access_token=access_token)
    api = vk.API(session, v='5.95')
    kachalka_kalash(api, kochka)

def kachalka_kalash(api, kochka):
    print("Бот запущен.")
    api.messages.send(random_id=random.randint(1,100000),peer_id=2000000333, message="Автокачалка была успешно запущена.")
    while True:
        if kochka:
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000327, message="гачи борьба @alums_ap")
            time.sleep(0.5)
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000327, message="КАЧАТЬСЯ!!!!!")
            print("КАЧАТЬСЯ!!!!!")
            time.sleep(36)
        else:
            ts=api.messages.getLongPollServer(need_pts=1, lp_version=3)
            time.sleep(36)
            response = api.messages.getLongPollHistory(ts=ts['ts'], fields=[""], events_limit=1000, msgs_limit=200, last_n=0)
            for _mes in response['messages']['items']:
                if _mes['peer_id'] == 2000000327 and _mes['text'] == "Чёт ты хилый, тебе бы в качалочку":
                    api.messages.send(random_id=random.randint(1,100000),peer_id=2000000327, message="Ле, внатуре, пойду качаться!")
                    kochka = True
                if _mes['peer_id'] == 2000000327 and _mes['text'] == "Нихуя жоский, остановись пока остановка не стала последней, ежжи":
                    api.messages.send(random_id=random.randint(1,100000),peer_id=2000000327, message="Пацаны, знаете, я решил бросить качалку")
                    kochka = False
            print(response['messages'])
       
try:
    kachalka_kalash(api, kochka)
except:
    print("Работа автокачалки была аварийно прекращена. Перезапуск...")
    api.messages.send(random_id=random.randint(1,100000),peer_id=2000000333, message="Работа автокачалки была аварийно прекращена. Перезапуск...")
    kochka = True
    init(access_token)
