from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
import random
from datetime import datetime
import time

vk_session = vk_api.VkApi(token="")#Здесь токен вашего профиля

def initiliziation():
    print("Running the script...")
    print("Login...")
    session_api = vk_session.get_api()
    print("Initializing variables...")
    #Пример. Замените на нужный вам id
    banned_user_1 = 624115175
    #Если нужны ещё пользователи - копируете строчку выше, смените цифру и заменяете на нужный вам id
    print("Initializing session...")
    longpoll = VkLongPoll(vk_session)

    print("Initializing log file...")
    #file = open("", "a", encoding='utf-8') #В начальных кавычках путь к лог-файлу. Пример: "D:/Python/log.txt". По желанию можете убрать логирование
    #file.write("---------------------------------------\n    A new session has started. \n       " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n ---------------------------------------\n")
    #file.close()

    print("Launch successfull.")
    print("-------------------------------")
    blmd_turn_on(longpoll, banned_user_1, vk_session)

def blmd_turn_on(longpoll, banned_user_1, vk_session):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            uid = event.user_id
            msgid = event.message_id
            msgtxt = event.text
            prid = event.peer_id
            if uid == banned_user_1:
                vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
                print("Сообщение от Славы Кравцова успешно удалено.")#Замените на имя вашей жертвы
                print("")
                print("      " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")))
                print(" " + str(event.text))
                print(" ")
                #file = open("", "a", encoding='utf-8') #Здесь точно такой-же путь
                #file.write("Сообщение от Славы Кравцова удалено. \n Дата: " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n" + event.text + "\n")
                #file.close()
            #Раскоментируйте всё это, если добавили второго пользователя. Если нужно ещё больше - перекопируйте и замените цифру на нужную. Соблюдайте количество отступов
            #if uid == banned_user_2:
            #    vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
            #    print("Сообщение от Славы Кравцова успешно удалено.")#Замените на имя вашей жертвы
            #    print("")
            #    print("      " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")))
            #    print(" " + str(event.text))
            #    print(" ")
            #    #file = open("", "a", encoding='utf-8') #Здесь точно такой-же путь
            #    #file.write("Сообщение от Славы Кравцова удалено. \n Дата: " + str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")) + "\n" + event.text + "\n")
            #    #file.close()
                
initiliziation()
