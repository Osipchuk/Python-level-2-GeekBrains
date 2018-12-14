# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
# info_3.txt и формирующий новый «отчетный» файл в формате CSV.

import re
import glob

def get_data():

    main_data= ['Изготовитель системы',
                'Название ОС',
                'Код продукта',
                'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for filename in glob.glob('*.txt'):
        with open(filename, 'r', encoding='cp1251') as f:
            for line in f:
                i = 0
                if re.match(r'Изготовитель ОС', line):
                    text = re.sub(r'\s*\n', '', re.sub(r'Изготовитель ОС: *', '', line))
                    os_prod_list.append(text)
                    i += 1
                elif re.match(r'Название ОС', line):
                    text = re.sub(r'\s*\n', '', re.sub(r'Название ОС: *', '', line))
                    os_name_list.append(text)
                    i += 1
                elif re.match(r'Код продукта', line):
                    text = re.sub(r'\s*\n', '', re.sub(r'Код продукта: *', '', line))
                    os_code_list.append(text)
                    i += 1
                elif re.match(r'Тип системы', line):
                    text = re.sub(r'\s*\n', '', re.sub(r'Тип системы: *', '', line))
                    os_type_list.append(text)
                    i += 1
                if i == 4:
                    break
    return [main_data, os_prod_list, os_name_list, os_code_list, os_type_list]


def write_to_csv(data, name='data.csv', delimiter=','):
    with open(name, 'w', encoding='utf-8') as f:
        for i, title in enumerate(data[0]):
            if i != 0:
                f.write(f'{delimiter}{title}')
            else:
                f.write(title)
        f.write('\n')
        LIST_LEN = len(data) - 1
        DATA_LEN = len(data[1])
        index = 0
        while index < DATA_LEN:
            for i, item in enumerate(data[1:]):
                if i != 0:
                    f.write(f'{delimiter}{item[index]}')
                else:
                    f.write(item[index])
            f.write('\n')
            index += 1


write_to_csv(get_data())

