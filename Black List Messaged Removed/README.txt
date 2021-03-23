Инфаструктура скрипта:

Получение списка запрещённых id в виде
blckid1 = "{id}"
blckid2 = "{id}"

Активация while=True
Получение нового сообщения
Запись определённых значений в переменные
msgid = {event.message_id}
uid = {event.user_id}

Сравнение uid с blckid-переменными:
if uid == blckid1:
	vk.message.remove(id=uid, delete_for_all=0)
	print("Сообщение от {user_name} успешно удалено.")
if uid == blckid2:
	vk.message.remove(id=uid, delete_for_all=0)
	print("Сообщение от {user_name} успешно удалено.")