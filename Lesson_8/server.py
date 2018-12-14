import argparse
import datetime
import json
import time
from socket import *
from log.server_log_config import server_log
from log.deco_log import log
import select


#@log('server_log')
def read_requests(r_clients, all_clients):
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('ascii')
            name = sock.getpeername()
            responses[sock] = (name, data)
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all_clients.remove(sock)
    return responses


#@log('server_log')
def write_responses(requests, w_clients, all_clients):
    for message in requests:
        resp = f'Message from {requests[message][0]}: {requests[message][1]}'.encode('ascii')
        for sock in w_clients:
            if sock.getpeername() == requests[message][0]:
                continue
            try:
                sock.send(resp.upper())
                print(sock.getpeername())
            except:
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
                sock.close()
                all_clients.remove(sock)


#@log('server_log')
def server():
    address = ('', 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print(f"Получен запрос на соединение от {str(addr)}")
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    try:
        server()
    except Exception as e:
        server_log.error(e)
