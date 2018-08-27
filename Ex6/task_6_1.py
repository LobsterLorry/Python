
# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

Address = input('Enter IP:')
Address = Address.split('.')

if int(Address[0]) in range(1,128):
	print('Class A')
	print('Type: Unicast')
elif int(Address[0]) in range(128,192):
	print('Class B')
	print('Type: Unicast')
elif int(Address[0]) in range(192,224):
	print('Class C')
	print('Type: Unicast')
elif int(Address[0]) in range(224,240):
	print('Class D')
	print('Type: Multicast')
elif int(Address[0])==int(Address[1])==int(Address[2])==int(Address[3])==255:
	print('Type: Local broadcast')
elif int(Address[0])==int(Address[1])==int(Address[2])==int(Address[3])==0:
	print('Type: Unassigned')
else:
	print('Type: Unused')