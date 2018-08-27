# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

NUMBERS = int(input('Enter number from list:'))
WORDS = input('Enter word from list:')

REVERSE1 = {0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1, 9:0}
REVERSE2 = {0:7, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1, 7:0}

reverse_num = (num_list[::-1].index(NUMBERS))
reserse_word= word_list[::-1].index(WORDS)

Position1 = REVERSE1[reverse_num]
Position2 = REVERSE2[reserse_word]
#Index_numb = num_list(reverse_num)
print(Position1, Position2)
