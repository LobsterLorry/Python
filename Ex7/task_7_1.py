# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
FILE = open('ospf.txt')
FILE = FILE.read()
FILE = FILE.split('\n')
FILE.pop(-1)
for A in range(0,8):
	FILE[A] = FILE[A].split(' ')
	for i in range(1,5):
		FILE[A].pop(i)
	for i in range(1,3):
		FILE[A].pop(i)
	FILE[A].pop(1)
#print(FILE[5][6])
O = 'OSPF'


OSPFTemp = '''
Protocol:				{0:<8}
Prefix:					{1:<8}
AD/Metric:				{2:<8}
Next-Hop:				{3:<8}
Last update:				{4:<8}
Outbound Interface:			{5:<8}
'''


for i in range(0,8):
	#for m in range(1,3):
	print(OSPFTemp.format(O,FILE[i][1],FILE[i][2],FILE[i][4][0:-1],FILE[i][5][0:-1],FILE[i][6]))


