import datetime
import json
import sys
import time
from socket import *


def presence():
    try:
        addr = str(sys.argv[1])
    except IndexError:
        print("Не указан addr")
        addr = "127.0.0.1"

    try:
        port = int(sys.argv[2])
    except IndexError:
        print('Не указан port')
        port = 7777

    s = socket()
    s.connect((addr, port))

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
    s_data_presence = json.dumps(data_presence)

    result = ""
    s.send(s_data_presence.encode("utf-8"))
    data = s.recv(1024)
    result = data.decode("utf-8")
    j_result = json.loads(result)

    return j_result


if __name__ == '__main__':
    presence()
