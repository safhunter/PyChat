import csv
import re
import itertools


file_names = ['info_1.txt', 'info_2.txt', 'info_3.txt']
param_names_to_find = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data(data_file_names: list, param_names: list) -> list:
    find_param_list = []
    param_regexps = []
    for num, param_name in enumerate(param_names):
        param_regexps.append(re.compile(rf'(?<={re.escape(param_name)}:)\s+.+$', re.MULTILINE))
        find_param_list.append([])
    for file_name in data_file_names:
        try:
            with open(file_name, 'r', encoding='cp1251') as data_file:
                data = data_file.read()
                for num, value_list in enumerate(find_param_list):
                    value_list.extend(list(map(lambda x: x.lstrip(), re.findall(param_regexps[num], data))))
        except OSError:
            print(f'Cant open file: {file_name}')

    find_param_list = list(map(list, itertools.zip_longest(*find_param_list, fillvalue='')))
    find_param_list.insert(0, param_names)
    return find_param_list


def write_to_csv(file_name):
    try:
        data_to_write = get_data(file_names, param_names_to_find)
    except Exception as ex:
        print(f'Cant get data to write, cause:\n{ex}')
        raise ex

    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            for item in data_to_write:
                writer.writerow(item)
    except OSError:
        print(f'Cant open file to write: {file_name}')


write_to_csv('task_1_data.csv')
