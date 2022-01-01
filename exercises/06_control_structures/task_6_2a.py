# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ipaddr = input('Enter ip address: ')
    ipad_lst = ipaddr.split('.')
    ipvalid = True

    if len(ipad_lst) == 4:
        for i in ipad_lst:
            if not (i.isdigit() and int(i) in range(256)):
                ipvalid = False
                break
    else:
        ipvalid = False

    if ipvalid:
        break

    print("Bad ip!")


oct1 = int(ipaddr.split('.')[0])
if oct1 in range(1, 224):
    print('Unicast')
elif oct1 in range(224, 240):
    print('Multicast')
elif ipaddr == '255.255.255.255':
    print('Local broadcast')
elif ipaddr == '0.0.0.0':
    print('Unassigned')
else:
    print('Unused')