import datetime
import json
import sys
import time
from socket import *
from log.client_log_config import client_log
from log.deco_log import log
import threading

ADDRESS = ('localhost', 10000)


# @log('client_log')
def client():
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        sock.connect(ADDRESS)  # Соединиться с сервером
        print('\n')
        t1 = ClientThread(sock, 'w')
        t2 = ClientThread(sock, 'r')

        t1.start()
        t2.start()

        t1.join()
        t2.join()


class ClientThread(threading.Thread):
    def __init__(self, sock, mode):
        super().__init__()
        self.sock = sock
        self.mode = mode


    def run(self):
        while True:
            if self.mode == 'w':
                msg = input('Вы: ')
                if msg.lower() == 'exit':
                    break
                if msg == '':
                    print('\n')
                self.sock.send(msg.encode('ascii'))
            if self.mode == 'r':
                data = self.sock.recv(1024).decode('ascii')
                print('\n', data)


if __name__ == '__main__':
    try:
        client()
    except Exception as e:
        client_log.error(e)