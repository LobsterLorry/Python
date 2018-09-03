# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
IP, MASK = argv[1:]
#IP = input('Type IP-adress:')
#Address = IP.split('/')
IP = IP.split('.')
#MASK = int(Address[1])
#IP = IP.split('.')
#print(type(IP))
CIDR = {24:[255, 255, 255, 0], 30:[255, 255, 255, 252], 32:[255, 255, 255, 255]}


A = int(IP[0])
B = int(IP[1])
C = int(IP[2])
D = int(IP[3])
#print(type(A))
A1 = (CIDR[int(MASK)])[0]
B1 = (CIDR[int(MASK)])[1]
C1 = (CIDR[int(MASK)])[2]
D1 = (CIDR[int(MASK)])[3]
#print(type(A1))

"""
A2 = int(bin(A & A1),2)
B2 = int(bin(B & B1),2)
C2 = int(bin(C & C1),2)
D2 = int(bin(D & D1),2)
#print(A2)
"""

A2 = A & A1
B2 = B & B1
C2 = C & C1
D2 = D & D1

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
print(OUPUT1.format(A2,B2,C2,D2,A1,B1,C1,D1,MASK = MASK))
