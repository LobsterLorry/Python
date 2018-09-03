# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


#print(type(FILE))


def parse_cdp_neighbors(command):
	command = command.split('\n')
	DICT={}
	for item in command:
		if item.startswith('S') and item[3] =='>':
			pass

		elif item.startswith('R') and item[2] =='>':
			pass

		elif item.startswith('R'):
			router, intf1, intf11 , *words, intf2, intf22 = item.split()
			LIST1 = [command[1][:3], intf1+intf11]
			LIST2 = [router, intf2+intf22,]
			TUPL1=tuple(LIST1)
			TUPL2=tuple(LIST2)
			DICT[TUPL1]=TUPL2
		elif item.startswith('S'):
			router, intf1, intf11 , *words, intf2, intf22 = item.split()
			LIST1 = [command[0][:2], intf1+intf11]
			LIST2 = [router, intf2+intf22,]
			TUPL1=tuple(LIST1)
			TUPL2=tuple(LIST2)
			DICT[TUPL1]=TUPL2	
			
	return DICT
		
	

FILE = open('sh_cdp_n_sw1.txt')
FILE = FILE.read()

if __name__ == "main":
	parse_cdp_neighbors(FILE)