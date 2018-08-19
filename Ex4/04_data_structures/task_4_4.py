# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
NIL1 = command1.find('1') # find position of 1
VLANS1 = command1[NIL1::] # extraction of vlans

NIL2 = command2.find('1') # find position of 1
VLANS2 = command2[NIL2::] # extraction of vlans
#print(VLANS1)
#print(VLANS2)
VLANS1 = VLANS1.split(',')
#print(VLANS1)
VLANS2 = VLANS2.split(',')
#print(VLANS2)
SetVL1 = set(VLANS1)
SetVL2 = set(VLANS2)
SetVL = SetVL1.intersection(SetVL2)
ListVL = list(SetVL)
ListVLAN = [int(ListVL[0]),int(ListVL[1]),int(ListVL[2])]
print(ListVLAN)