# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
#AAAA = bin(int('AAAA',16))
NIL11 = MAC.find('A')
NIL12 = MAC.find(':B')
AAAA = MAC[NIL11:NIL12]
NIL21 = MAC.find('B')
NIL22 = MAC.find(':C')
BBBB = MAC[NIL21:NIL22]
NIL31 = MAC.find('C')
CCCC = MAC[NIL31::]
A = bin(int(AAAA,16))
B = bin(int(BBBB,16))
C = bin(int(CCCC,16))
print(A+B+C)

MAC = MAC.split(':')
#print(MAC[0])
A1 = bin(int(MAC[0],16))
B1 = bin(int(MAC[1],16))
C1 = bin(int(MAC[2],16))
print(A1+B1+C1)
