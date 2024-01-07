"""
запускается из командной строки и получает на вход путь до директории на ПК.
Собирает информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.

сохраняет данные в текстовый файл используя логирование.
"""
import logging
import os
from collections import namedtuple
import sys

Entry = namedtuple('Entry', ['name', 'ext', 'is_dir', 'parent'])
format = '%(asctime)s \t\t %(message)s'
datefmt='%m/%d/%Y\t%I:%M %p'
logging.basicConfig(level=logging.INFO, 
                    filename='mylog.log',  
                    encoding='utf-8', 
                    filemode='w', 
                    format = format, 
                    datefmt=datefmt)



def crawl(work_dir):
    entries = []
    for parent, dirs, files in list(os.walk(work_dir)):
        for dir in dirs:
            elem = Entry(dir, '', True, parent)
            entries.append(elem)
            logging.info(f'dirname:\t{elem.name}, \t parentdir {elem.parent}')
 
        for file in files:
            first = file[0]
            name_string = file[1:].split('.')
            ext = ''
            name_string[0] = first+name_string[0]
            if len(name_string)>1:
                ext = name_string.pop()
            name = '.'.join(name_string)    
            elem = Entry(name,ext, False, parent)
            entries.append(elem)
            logging.info(f'filename:\t{elem.name}.{elem.ext}, \t parentdir {elem.parent}')
    return entries


if __name__ == '__main__':  
    if len(sys.argv) > 1:
         arg1 = sys.argv[1]
         crawl(arg1)
    else:
        print("No arguments were passed. Need path to crawl")
