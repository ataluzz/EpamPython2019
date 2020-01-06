'''
Задание 2
Написать маленькую утилиту, которая в качестве аргумента принимает путь до директории и sha256 hash

Утилита должна пройти по всем файлам внутри директории и вывести в stdout абсолютный путь до файлов,
хеш которых указан в качестве аргумента

Определить:
1) какой системный вызов будет использоваться чаще всего (strace)
2) какой участок кода "самый горячий" (профилирование)
3) какой системный вызов потребил больше всего времени (strace + анализ логов)
'''

import click
from hashlib import sha256
import os
import sys


def hash_of_file(file):
    with open(file, "rb") as f:
        filehash = sha256(f.read()).hexdigest()
        return filehash
        

def get_path_of_hash_file(dir_path, hash_line):
    path_list = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            file_path = os.path.abspath(root) + '/' + name
            curr_hash = hash_of_file(file_path)
            if curr_hash == hash_line:
                path_list.append(file_path)
    return path_list

@click.command()
@click.argument('dir_path')
@click.argument('hash_line')
def main(dir_path, hash_line):
    """
    This utility takes path to directory and sha256 hash as arguments.
    After that it goes through all files in this directory and writes in stdout
    absolute paths of files with the same hash as the hash in arguments
    """
    result = get_path_of_hash_file(dir_path, hash_line)
    if result:
        print("Got this files: \n")
        for item in result:
            print(item)
    else:
        print("There are no such files in directory")

        
if __name__ == "__main__":
    main()
