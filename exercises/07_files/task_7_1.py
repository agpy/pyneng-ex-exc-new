# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

out = "\n{:25} {}" * 5


with open('ospf.txt', 'r') as f:
    for line in f:
#         route = line.strip().replace(",", " ").replace("[", "").replace("]", "")
#         route = route.split()
#         print(route)
        _, pref, adm, _, nhop, lupd, outintf = line.replace('[','').replace(']','').replace(',','').split()
        print(out.format('Prefix', pref,
                        'AD/Metric', adm,
                        'Next-Hop', nhop,
                        'Last update', lupd,
                        'Outbound Interface', outintf
        ))

