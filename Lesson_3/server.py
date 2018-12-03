import argparse
import datetime
import json
import time
from socket import *

parser = argparse.ArgumentParser(description='TCP Server Settings')
parser.add_argument('-p', dest='port', type=int,
                    default=7777,
                    help='TCP-port for work (default 7777)')
parser.add_argument('-a', dest='addr', type=str,
                    default='',
                    help='ip-address for listening (default "")')

args = parser.parse_args()

dt = datetime.datetime.now()
value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))

s = socket()
s.bind((args.addr, args.port))
s.listen(1)

data_response_200 = {
    "response": 200,
    "time": value.strftime('%H:%M:%S'),
    "alert": "message for client"
}

s_data_response_200 = json.dumps(data_response_200)

while True:
    client, addr = s.accept()
    print(f"Получен запрос на соединение от {str(addr)}")
    while True:
        clientAnswer = client.recv(1024)
        if not clientAnswer:
            break
        clientUser = json.loads(clientAnswer)
        print(f"Получено {addr}:{clientUser}")
        client.send(s_data_response_200.encode("utf-8"))

    client.close()
