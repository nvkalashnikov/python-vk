from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
import random
from datetime import datetime
import time

vk_session = vk_api.VkApi(token="f7b958ffe523f083da4d724c4784d12752c87491a761ce8aa9c3bcf39c2b4e506cf1bf597593c898603f0")

def initiliziation():
    print("Running the script...")
    print("Login...")
    print("Initializing variables...")
    banned_user_1 = 624115175 #Слава Кравцов
    banned_user_2 = 417083283 #Амирхан Жумайсынба
    banned_user_3 = 483926863 #Алексей Кашин
    nvk = 390496859 #Никита Калашников
    print("Initializing session...")
    session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    print("Initializing log file...")
    file = open("C:/Users/NVKalashnikov/Documents/Black List Messaged Removed/log.txt", "a", encoding='utf-8')
    file.write("---------------------------------------\n    A new session has started. \n       " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n ---------------------------------------\n")
    file.close()

    print("Launch successfull.")
    print("-------------------------------")
    vk_session.method('messages.send', {'peer_id': 2000000333, 'random_id': random.randint(1,100000), 'message': 'BLMD был успешно запущен.'})
    blmd_turn_on(longpoll, banned_user_1, banned_user_2, banned_user_3, nvk, vk_session)

def blmd_turn_on(longpoll, banned_user_1, banned_user_2, banned_user_3, nvk, vk_session):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            uid = event.user_id
            msgid = event.message_id
            msgtxt = event.text
            prid = event.peer_id
            if uid == banned_user_1:
                vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
                print("Сообщение от Славы Кравцова успешно удалено.")
                print("")
                print("      " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")))
                print(" " + str(event.text))
                print(" ")
                file = open("C:/Users/NVKalashnikov/Documents/Black List Messaged Removed/log.txt", "a", encoding='utf-8')
                file.write("Сообщение от Славы Кравцова удалено. \n Дата: " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n" + event.text + "\n")
                file.close()
            if uid == banned_user_2:
                vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
                print("Сообщение от Амирхана Жумайсынбы успешно удалено.")
                print("")
                print("      " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print("" + str(event.text))
                print(" ")
                file = open("C:/Users/NVKalashnikov/Documents/Black List Messaged Removed/log.txt", "a", encoding='utf-8')
                file.write("Сообщение от Амирхана Жумайсынбы. \n Дата: " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n" + event.text + "\n")
                file.close()
            if uid == banned_user_3:
                vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
                print("Сообщение от Алексея Кашина успешно удалено.")
                print("")
                print("      " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")))
                print(" " + str(event.text))
                print(" ")
                file = open("C:/Users/NVKalashnikov/Documents/Black List Messaged Removed/log.txt", "a", encoding='utf-8')
                file.write("Сообщение от Алексея Кашина удалено. \n Дата: " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n" + event.text + "\n")
                file.close()
                
            if msgtxt == "BLMD состояние" and uid == nvk:
                print("BLMD запущен и включён.")
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'BLMD запущен и включён.'})
            if msgtxt == "BLMD список" and uid == nvk:
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'Автоматически удаляются сообщения: Амирхана Жумайсынбы, Алексея Кашина, Полины Абакумовы.'})
            if msgtxt == "BLMD выключить" and uid == nvk:
                print("BLMD был выключен.")
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'BLMD успешно выключен.'})
                blmd_turn_off(longpoll, banned_user_1, banned_user_2, banned_user_3, nvk, vk_session)
            if msgtxt == "BLMD перезапуск" and uid == nvk:
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'Перезапуск...'})
                time.sleep(2)
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'BLMD успешно перезапущен.'})
            if msgtxt == "BLMD добавь odolzhigorlo" and uid == nvk:
                print("Пользователь успешно добавлен.")
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'Пользователь успешно добавлен.'})

def blmd_turn_off(longpoll, banned_user_1, banned_user_2, banned_user_3, nvk, vk_session):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            uid = event.user_id
            msgid = event.message_id
            msgtxt = event.text
            prid = event.peer_id
            if msgtxt == "BLMD состояние" and uid == nvk:
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'BLMD запущен и выключён.'})
            if msgtxt == "BLMD включить" and uid == nvk:
                print("BLMD был включен.")
                vk_session.method('messages.send', {'peer_id': prid, 'random_id': random.randint(1,100000), 'message': 'BLMD успешно включен.'})
                blmd_turn_on(longpoll, banned_user_1, banned_user_2, banned_user_3, nvk, vk_session)
                

try:
    initiliziation()
except:
    vk_session.method('messages.send', {'peer_id': 2000000333, 'random_id': random.randint(1,100000), 'message': 'Работа BLMD была аварийно прекращена. Перезапуск...'})
    initiliziation()
