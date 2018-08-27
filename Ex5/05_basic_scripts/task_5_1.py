# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

IP = input('Type IP-adress:')
Address = IP.split('/')
IP = Address[0]
MASK = int(Address[1])
IP = IP.split('.')
#print(type(IP))
CIDR = {24:[255, 255, 255, 0], 30:[255, 255, 255, 252], 32:[255, 255, 255, 255]}

A = int(IP[0])
B = int(IP[1])
C = int(IP[2])
D = int(IP[3])
#print(type(A))
A1 = (CIDR[MASK])[0]
B1 = (CIDR[MASK])[1]
C1 = (CIDR[MASK])[2]
D1 = (CIDR[MASK])[3]
#print(type(A1))

""" Example 1
OUPUT1 = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

'''
OUPUT2 = '''
Mask:
/{MASK}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(OUPUT1.format(A,B,C,D))
print(OUPUT2.format(A1,B1,C1,D1,MASK = MASK))

#print(A1)
"""

OUPUT1 = ''' # Example 2
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{MASK}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
'''
print(OUPUT1.format(A,B,C,D,A1,B1,C1,D1,MASK = MASK))


