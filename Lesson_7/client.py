import datetime
import json
import sys
import time
from socket import *
from log.client_log_config import client_log
from log.deco_log import log


ADDRESS = ('localhost', 10000)

#@log('client_log')
def client():
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        sock.connect(ADDRESS)  # Соединиться с сервером
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'exit':
                break
            sock.send(msg.encode('ascii'))
            data = sock.recv(1024).decode('ascii')
            print('Ответ:', data)


if __name__ == '__main__':
    try:
        client()
    except Exception as e:
        client_log.error(e)
