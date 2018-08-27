# -*- coding: utf-8 -*-
'''
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.

Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ним делать.

Поэтому в соответствии каждому порту стоит список
и первый (нулевой) элемент списка указывает как воспринимать номера VLAN,
которые идут дальше:
	add - значит VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
	del - значит VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
	only - значит, что на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)

Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

fast_int = {
    'access': {
        '0/12': '10',
        '0/14': '11',
        '0/16': '17',
        '0/17': '150'
    },
    'trunk': {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
}
"""
for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
"""

ADD = (fast_int['trunk']['0/1'])[0]
ONLY = (fast_int['trunk']['0/2'])[0]
DEL = (fast_int['trunk']['0/4'])[0]
VLANS1 = (fast_int['trunk']['0/1'])[1]+' '+(fast_int['trunk']['0/1'])[2]
VLANS2 = (fast_int['trunk']['0/2'])[1]+' '+(fast_int['trunk']['0/2'])[2]
VLANS3 = (fast_int['trunk']['0/4'])[1]
#print(VLANS)

for intf, action in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
       #print(action[0]) 
        if action[0] == ADD and command.endswith('vlan'):
            print('{} add {}'.format(command,VLANS1))
        elif action[0] == DEL and command.endswith('vlan'):
            print('{} remove {}'.format(command,VLANS2))
        elif action[0] == ONLY and command.endswith('vlan'):
            print('{} {}'.format(command,VLANS3))
        else:
            print(' {}'.format(command))
    