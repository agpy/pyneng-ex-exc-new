# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

r1 = {'access': access_template, 'trunk': trunk_template}
dict_mod = {'trunk': 'Enter trunk vlans', 'access': 'Enter access vlan'}
intf_mode = input('Enter interface mode (access/trunk): ')
intf = input('Enter type and number of interface (Fa0/7): ')
vlans = input(dict_mod[intf_mode] + ': ')

str_out = '\n'.join(r1[intf_mode])
print("interface {}".format(intf) + '\n' + str_out.format(vlans))