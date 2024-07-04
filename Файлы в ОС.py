import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(__file__)
        print(f'обнаружен файл: {file}, путь: {filepath}, размер: {filesize} байт, '
              f'время изменения: {formatted_time}, родительская директория: {parent_dir}')

