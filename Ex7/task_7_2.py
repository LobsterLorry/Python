# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


from sys import argv
config = argv[1]
FILE = open(config)
FILE = FILE.read().split('\n')


for elem in FILE:
	if elem.startswith('!  '):	
		#FILE.remove(elem)
		pass
	elif elem.startswith(' '):
		print(elem[1::])
	elif elem.startswith('! '):
		#FILE.remove(elem)
		pass
	elif len(elem) > 2:
		print(elem) 
	