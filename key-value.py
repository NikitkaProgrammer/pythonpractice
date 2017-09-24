'''Сохраняет данные по ключу. Можно сохранять несколько записей по одному ключу. В таком случае они будут выводится через запятую. Наглядно показана работа:
argparse - работа с агрументами командной строки
tempfile - работа с временными файлами
json - работа с файлами, где информация хранится в виде словарей'''

import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser() #работа с аргументами командной строки
parser.add_argument('--key') #добавление аргументов
parser.add_argument('--val')
args = parser.parse_args()#получение их списка
if(args.val == None):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')#временный файл, вшитый в прогу
    try:
        with open(storage_path, 'r') as f:
            data = json.load(f) # загружаем в виде словаря
            print(data[args.key])
    except:
        with open(storage_path, 'w') as f:
            print("")
else:
    data = {}
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    try:
        with open(storage_path, 'r') as f:
                data = json.load(f)
                if(args.key in data):
                    quick_save = str(data[args.key]) + ", " + str(args.val)#можно добавлять несколько значений по ключу. Будут выводится через запятую
                    del data[args.key]
                    data[args.key] = quick_save
        with open(storage_path, 'w+') as f:
            if(not (args.key in data)):
                data[args.key] = args.val
            json.dump(data,f)# сохраняем в виде словаря
    except:
        with open(storage_path, 'w') as f:
            json.dump({args.key:args.val},f)
