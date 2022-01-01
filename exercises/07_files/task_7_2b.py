# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

fconfig = argv[1]
foutput = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open('fconfig', 'r') as src, open('foutput', 'w') as dst:
    for command in ignore:
        for line in src:
            if line.startswith('!'):
                continue
            else:
                if command not in line:
                    dst.write(line.rstrip())