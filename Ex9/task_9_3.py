# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config):
	acces_dict= {}
	trunk_dict= {}
	with open(config) as FILE:
		for line in FILE:
			if line.startswith('interface F'):
				intf, ifname = line.split()
			if line.startswith(' switchport access'):
					sw, ace, vlan, vlannum = line.split()
					acces_dict[ifname] = vlannum
	
			if line.startswith(' switchport trunk allowed'):
					sw, tr, alla, vla, vlans = line.split()
					trunk_dict[ifname] = vlans.split(',')


	print(acces_dict)
	print(trunk_dict)

get_int_vlan_map('config_sw1.txt')