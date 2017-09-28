'''
Данный класс позволяет удобно работать с файлами. Реализованы такие функции:
-Сложение файлов(создастся новый объект, содержание которого равно содержанием двух предыдущих
-Итерация по строкам файла, а не по словам
-При печати объекта выводится его путь
'''
import tempfile
import os

class File:
    def __init__(self, filename):
        self.filename = filename
        self.counter = 0

    def write(self,text):
        with open(self.filename, 'w') as f:
            f.write(text)
        return None

    def __iter__(self):
        return self

    def __next__(self):
        f = open(self.filename,'r')
        if(self.counter < len(f.readlines())):
            f.seek(0)
            for i in range(self.counter):
                f.readline()
            self.counter += 1
            text = f.readline().strip("\n")
            return text
        else:
            raise StopIteration
                    
    def __str__(self):
        return self.filename

    def __add__(self, another_object):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(self.filename, 'r') as f1:
            first_file_data = f1.read()
        with open(another_object.filename, 'r') as f2:
            second_file_data = f2.read()
        with open(storage_path, 'w') as temp_file:
            temp_file.write(first_file_data)
            temp_file.write(second_file_data)
        return File(storage_path)
