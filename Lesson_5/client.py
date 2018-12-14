import datetime
import json
import sys
import time
from socket import *
from log.client_log_config import client_log


def presence():
    try:
        addr = str(sys.argv[1])
    except IndexError:
        client_log.warning("Не указан addr")
        addr = "127.0.0.1"

    try:
        port = int(sys.argv[2])
    except IndexError:
        client_log.warning('Не указан port')
        port = 7777

    s = socket()
    s.connect((addr, port))
    client_log.info(f'Подключение к {addr} : {port}')
    dt = datetime.datetime.now()
    value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))

    data_presence = {
        "action": "presence",
        "time": value.strftime('%H:%M:%S'),
        "type": "status",
        "user": {
            "account_name": "Guest",
            "status": "Online"
        }

    }
    client_log.info(f'Сформирован пакет данных')
    s_data_presence = json.dumps(data_presence)

    result = ""
    s.send(s_data_presence.encode("utf-8"))
    client_log.info(f'Данные отправлены на сервер')
    data = s.recv(1024)
    client_log.info(f'Получен ответ')
    result = data.decode("utf-8")
    j_result = json.loads(result)

    return j_result


if __name__ == '__main__':
    try:
        presence()
    except Exception as e:
        client_log.error(e)
