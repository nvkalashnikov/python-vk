import vk
import time
import random

access_token = "de09c3cbe73d5c0c8cc33c6a0940b82fdd5c4ecb6d7d9ef6eca0f43bd89b0fce033f09967ca34ac55e277" # API_KEY
session = vk.Session(access_token=access_token)
api = vk.API(session, v='5.95')

kochka = False

def kachalka_alums():
    while True:
        ts=api.messages.getLongPollServer(need_pts=1, lp_version=3)
        time.sleep(36)
        response = api.messages.getLongPollHistory(ts=ts['ts'], fields=[""], events_limit=1000, msgs_limit=200, last_n=0 )
        for _mes in response['messages']['items']:
            if _mes['peer_id'] == 2000000024 and _mes['text'] == "Чёт ты хилый, тебе бы в качалочку":
                api.messages.send(random_id=random.randint(1,100000),peer_id=2000000024, message="Ле, внатуре, пойду качаться!")
                kochka = True
            if _mes['peer_id'] == 2000000024 and _mes['text'] == "Нихуя жоский, остановись пока остановка не стала последней, ежжи":
                api.messages.send(random_id=random.randint(1,100000),peer_id=2000000024, message="Пацаны, знаете, я решил бросить качалку")
                kochka = False
        if kochka:
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000024, message="гачи борьба @nvkalashnikov")
            time.sleep(0.5)
            api.messages.send(random_id=random.randint(1,100000),peer_id=2000000024, message="КАЧАТЬСЯ!!!!!")
        print(response['messages'])
try:
    kachalka_alums()
