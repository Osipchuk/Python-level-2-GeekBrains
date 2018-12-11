# Служебный скрипт запуска/останова нескольких клиентских приложений

from subprocess import Popen, CREATE_NEW_CONSOLE
import os

p_list = []

while True:
    user = input("Запустить клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")

    if user == 'q':
        break
    elif user == 's':
        clients = int(input('Сколько клиентов запустить: '))
        for _ in range(clients):
            # Флаг CREATE_NEW_CONSOLE нужен для ОС Windows,
            # чтобы каждый процесс запускался в отдельном окне консоли
            p_list.append(Popen('python client.py',
                                creationflags=CREATE_NEW_CONSOLE))
            # my_str = raw_input('Your string here: ')
        print(f' Запущено {clients} клиентов')
    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()
