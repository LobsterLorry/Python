# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

O = 'OSPF'
NIL1 = ospf_route.find('1')
PEREM1 = ospf_route[NIL1:21]
NIL21 = ospf_route.find('[')
NIL22 = ospf_route.find(' v')
PEREM2 = ospf_route[NIL21:NIL22]
NIL31 = ospf_route.find('10.0.13')
NIL32 = ospf_route.find(', ')
PEREM3 = ospf_route[NIL31:NIL32]
NIL41 = ospf_route.find('3d')
NIL42 = ospf_route.find(', F')
PEREM4 = ospf_route[NIL41:NIL42]
NIL51 = ospf_route.find('F')
PEREM5 = ospf_route[NIL51::]
#print(PEREM5)
OSPFTemp = '''
Protocol:				{:<8}
Prefix:					{:<8}
AD/Metric:				{:<8}
Next-Hop:				{:<8}
Last update:				{:<8}
Outbound Interface:			{:<8}
'''
print(OSPFTemp.format(O,PEREM1,PEREM2,PEREM3,PEREM4,PEREM5))