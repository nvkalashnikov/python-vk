from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data

vk_session = vk_api.VkApi(token="f7b958ffe523f083da4d724c4784d12752c87491a761ce8aa9c3bcf39c2b4e506cf1bf597593c898603f0")

banned_user_1 = 624115175
banned_user_2 = 233435454

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print("Launche successfully.")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        uid = event.user_id
        msgid = event.message_id
        if uid == banned_user_1:
            vk_session.method('messages.delete', {'message_ids': msgid, 'spam': 0, 'delete_for_all': 0})
            print("Сообщение от Славы Кравцова успешно удалено.")