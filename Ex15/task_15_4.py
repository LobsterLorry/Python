# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
import re
def parse_sh_ip_int_br(config):
	LIST = []
	with open(config) as FILE:
		for line in FILE:
			result = re.finditer('(^\S+) +((?:\d+\.\d+\.\d+\.\d+)|(?:unassigned)) +YES (?:manual|unset) *(up|\D+) +(up|down)',line)
			for match in result:
				LIST.append(match.groups())
		print(LIST)
parse_sh_ip_int_br('sh_ip_int_br_2.txt')