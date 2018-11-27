import datetime
import json
import sys
import time
from socket import *

print(sys.argv)
try:
    addr = str(sys.argv[1])
except IndexError:
    print("Не указан addr")
    addr = "127.0.0.1"

try:
    port = int(sys.argv[2])
except IndexError:
    port = 7777
print(addr, port)

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

print(j_result['response'])

s.close()

print(j_result)
