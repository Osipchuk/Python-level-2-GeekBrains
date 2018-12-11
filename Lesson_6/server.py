import argparse
import datetime
import json
import time
from socket import *
from log.server_log_config import server_log
from log.deco_log import log


@log('server_log')
def presence_response():
    dt = datetime.datetime.now()
    value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))

    data_response_200 = {
        "response": 200,
        "time": value.strftime('%H:%M:%S'),
        "alert": "message for client"
    }

    return data_response_200


@log('server_log')
def server():
    parser = argparse.ArgumentParser(description='TCP Server Settings')
    parser.add_argument('-p', dest='port', type=int,
                        default=7777,
                        help='TCP-port for work (default 7777)')
    parser.add_argument('-a', dest='addr', type=str,
                        default='',
                        help='ip-address for listening (default "")')

    args = parser.parse_args()

    s = socket()
    s.bind((args.addr, args.port))
    s.listen(1)

    s_data_response_200 = json.dumps(presence_response())
    print(s_data_response_200)
    while True:
        client, addr = s.accept()
        server_log.info(f"Получен запрос на соединение от {str(addr)}")
        while True:
            clientAnswer = client.recv(1024)
            if not clientAnswer:
                server_log.warning('Клиент не отвечает')
                break
            clientUser = json.loads(clientAnswer)
            server_log.info(f"Получено {addr}:{clientUser}")
            client.send(s_data_response_200.encode("utf-8"))
            server_log.info('Сообщение отправлено клиенту')
        client.close()


if __name__ == '__main__':
    try:
        server()
    except Exception as e:
        server_log.error(e)
