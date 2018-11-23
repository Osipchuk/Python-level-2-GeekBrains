# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
import json


def write_to_json(item, quantity, price, buyer, date):
    dict_ord = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'w') as f:
        json.dump(dict_ord, f, indent=4)

write_to_json('Book', 500, 599, 'School', '15.12.2020')
