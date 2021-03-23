from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
import random
from datetime import datetime

print("Running the script...")
print("Login...")
vk_session = vk_api.VkApi(token="f7b958ffe523f083da4d724c4784d12752c87491a761ce8aa9c3bcf39c2b4e506cf1bf597593c898603f0")
print("Initializing variables...")
banned_user_1 = 624115175
banned_user_2 = 417083283
print("Initializing session...")
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print("Initializing log file...")
file = open("C:/Users/NVKalashnikov/Documents/Black List Messaged Removed/log.txt", "a", encoding='utf-8')
file.write("---------------------------------------\n    A new session has started. \n       " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n ---------------------------------------\n")
file.close()

print("Launch successfull.")
print("-------------------------------")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        uid = event.user_id
        msgid = event.message_id
        msgtxt = event.text
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
            
        if msgtxt == "BLMD состояние":
            vk_session.method('messages.send', {'peer_id': 2000000333, 'random_id': random.randint(1,100000), 'message': 'BLMD is working.'})