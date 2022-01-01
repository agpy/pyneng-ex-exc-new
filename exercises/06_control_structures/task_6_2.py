# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#ipaddr = input('Enter ip address: ')
#oct1 = ipaddr.split('.')

while True:
    ipaddr = input('Enter ip address: ')
    oct1 = int(ipaddr.split('.')[0])
    if 1 <= oct1 <=223:
        print('Unicast')
    elif 224 <= oct1 <=239:
        print('Multicast')
    elif ipaddr == '255.255.255.255':
        print('Local broadcast')
    elif ipaddr == '0.0.0.0':
        print('Unassigned')
    else:
        print('Unused')
        break